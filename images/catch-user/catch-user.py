#!/usr/bin/env python
"""
Usage:
  catch_joe.py [--input-json=FILE --output-csv=FILE
  --prob-threshold=P --probabilities --threads=N --force --quiet]

Options:
  --input-json=FILE    The JSON file with recorded sessions.
                       [default: verify.json]
  --output-csv=FILE    The desired path for the results CSV.
                       [default: results.csv]
  --prob-threshold=P   The probability to use as threshold during
                       classification. Only accepts values in {0.04,..,0.99}.
                       The chosen value will affect the precision and recall.
                       [default: 0.34]
  --probabilities      Output probability values instead of 0s and 1s.
  --threads=N          Number of threads to use for the prediction.
                       [default: 1]
  --force              Overwrite the output file if it already exists.
  --quiet              Do not print messages of what the script is doing.
"""

import pickle
from datetime import datetime
from operator import itemgetter
from os import makedirs
from os.path import isfile, dirname, isdir
import sys
import psutil
import warnings

import numpy as np
import pandas as pd
from docopt import docopt


def warn(*args, **kwargs): pass
# Supress UserWarnings during the model unpcliking in case there is an older
# version of sklearn. Taken from: https://stackoverflow.com/questions/32612180
warnings.warn = warn


SCRIPT_DIR = sys.path[0]
MODEL_PATH = f"{SCRIPT_DIR}/aux/model.pickle"
FEATURES_LIST = f"{SCRIPT_DIR}/aux/features.list"
IMPUTATION_CSV = f"{SCRIPT_DIR}/aux/imputation_values.csv"
THRESHOLDS_CSV = f"{SCRIPT_DIR}/aux/model.thresholds.csv"


def load_model(threads):
    """
    Loads the fitted sklearn model and sets its n_jobs to *threads*.
    """
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)

    available_threads = psutil.cpu_count()
    if threads > available_threads:
        print(f"Chosen threads ({threads}) exceeds "
              f"available threads ({available_threads}).")
        exit_the_script()

    model.n_jobs = threads
    return model


def exit_the_script():
    print("Exiting the program")
    sys.exit()


def read_dataset(path):
    """
    Reads a JSON dataset of user sessions as a pd.DataFrame.
    """
    if not isfile(path):
        print(f"File not found: {path}")
        exit_the_script()

    try:
        data = pd.read_json(path)
    except ValueError:
        print("ERROR: I was expecting an array in JSON format.")
        exit_the_script()
    data.index.name = "session_id"
    return data


def check_na_ratio(sessions):
    """
    Checks the proportion of cells with missing data.
    """
    na_cells = sessions.isnull().sum().sum()
    n, m = sessions.shape
    na_ratio = na_cells/(n * m)

    if na_ratio > 0.5:
        print(f"ERROR: {na_ratio:.2%} missing data, is the input ok?")
        exit_the_script()

    return na_ratio


def read_feature_list():
    """
    Returns the list of features in the order that the model expects.
    """
    with open(FEATURES_LIST) as f:
        features = [line.strip() for line in f]
    return features


def get_url_features():
    """
    Returns the list of features that correspond to a URL.
    """
    features = read_feature_list()
    return [f for f in features if f.startswith("url_")]


def get_selected_urls():
    """
    Returns the list URLs that are used as features.
    """
    url_features = get_url_features()
    return [f.replace("url_", "") for f in url_features]


def get_precision_recall(thr):
    """
    Given a probability threshold *thr*, return a pd.Series with the
    expected precision and recall.
    """
    if not isfile(THRESHOLDS_CSV):
        return

    pr_data = pd.read_csv(THRESHOLDS_CSV, index_col="threshold")

    if thr not in pr_data.index:
        print(f"ERROR: chosen threshold {thr} is not available.")
        exit_the_script()

    return pr_data.loc[thr]


def sanitize_colname(col):
    return col.replace(" ", "_").replace("/", "-")


def extract_site_visits_as_df(sessions):
    """
    Produces a new pd.DataFrame from the 'sites' columns of *sessions*, with
    one site visit and its duration per row.
    """
    if "sites" not in sessions:
        print("ERROR: The input data has no 'sites' key.")
        exit_the_script()

    # In case some "sites" are NA
    na_sites = sessions["sites"].isnull()
    for ix in sessions[na_sites].index:
        sessions.at[ix, "sites"] = []

    visits = []

    for session_id, session in sessions.iterrows():
        for site in session["sites"]:
            visits.append({
                "session_id": session_id,
                "site": site["site"],
                "visit_duration": site["length"],
            })

    return pd.DataFrame(visits)


def parse_sessions_data_inplace(sessions, visits):
    """
    Adds new columns to the *sessions* dataframe.
    """
    time_parts = sessions["time"].str.split(":")
    sessions["hour"] = time_parts.map(itemgetter(0), na_action="ignore")
    sessions.drop("time", axis=1, inplace=True)

    sessions["n_sites"] = sessions["sites"].map(len)

    sessions["year"] = sessions["date"].dt.year
    sessions["month"] = sessions["date"].dt.month
    sessions["day"] = sessions["date"].dt.day
    sessions["weekday"] = sessions["date"].dt.strftime("%A")
    sessions.drop("date", axis=1, inplace=True)

    total_session_times = visits.groupby("session_id")["visit_duration"].sum()
    sessions["duration"] = sessions.index.map(total_session_times)
    sessions["duration_min"] = (sessions["duration"]/60).round()
    sessions.drop("duration", axis=1, inplace=True)


def keep_only_selected_site_visits(visits, say):
    """
    Makes a new dataframe keeping only the rows from *visits* that belong to
    sites selected as features.
    """
    say(f" -> {len(visits):,} total visits")
    selected_urls = set(get_selected_urls())

    unique_sites = set(visits["site"].unique())
    say(f" -> {len(unique_sites):,} unique sites found")

    kept_sites = unique_sites & selected_urls
    say(f" -> {len(kept_sites):,} of them will be features")

    mask = visits["site"].isin(selected_urls)
    filtered_visits = visits[mask].reset_index(drop=True)

    say(f" -> {len(filtered_visits):,} visits to selected sites")
    return filtered_visits


def add_sites_visited_to_sessions(sessions, visits):
    """
    Given the dataframe of *visits* with one session visit per row, add the
    visit durations as new columns in the *sessions* dataframe.
    """
    visits_wide = visits.pivot_table(
        values="visit_duration",
        index="session_id",
        columns="site"
    )
    visits_wide = visits_wide.fillna(0).astype(int)
    visits_wide.columns = [f"url_{col}" for col in visits_wide]

    return sessions.join(visits_wide, on="session_id")


def get_imputation_values():
    """
    Returns a dictionary of values per feature to fill missing data.
    """
    imputation_values = pd.read_csv(IMPUTATION_CSV)
    return imputation_values.set_index("feature")["value"].to_dict()


def impute_missing_features(sessions, say):
    """
    Imputes missing values with values found in the IMPUTATION_CSV.
    Will impute a whole column if it's missing.
    """
    features = read_feature_list()
    imputation_values = get_imputation_values()

    missing_cols = []
    n = len(sessions)

    for feature in features:
        imputed_val = imputation_values[feature]

        # If the whole column is missing:
        if feature not in sessions:
            imputed_col = pd.Series(np.repeat(imputed_val, n))
            imputed_col.name = feature
            imputed_col.index = sessions.index
            missing_cols.append(imputed_col)

        # In case only some values are missing:
        else:
            null_indices = sessions[feature].isnull()
            sessions.loc[null_indices, feature] = imputed_val

    if missing_cols:
        missing_cols = pd.concat(missing_cols, axis=1).astype(int)
        sessions = sessions.join(missing_cols)

    return sessions


def match_the_model_features(sessions):
    """
    Reorder and filter the columns to match the model fetaures.
    Assumes that all necessary features are already present as columns.
    """
    features = read_feature_list()
    return sessions[features]


def add_dummies_from_categoricals(sessions):
    """
    Replaces some categorical variables with dummy variables.
    """
    categorical_variables = [
        "browser",
        "os",
        "locale",
        "gender",
        "location",
        "weekday",
    ]
    dummy_columns = pd.get_dummies(sessions[categorical_variables])
    dummy_columns.columns = [sanitize_colname(c)
                             for c in dummy_columns.columns]
    sessions = pd.concat([
        sessions.drop(categorical_variables, axis=1),
        dummy_columns
    ], axis=1)
    return sessions


def main(in_filepath, out_filepath, prob_threshold, predict_probabilities,
         threads, overwrite, quiet):
    """
    Runs the pipeline to predict which sessions correspond to Joe.
    Writes a CSV with one prediction (0 = Joe, 1 = not Joe) per line.

    - in_filepath: path to a JSON of recorded sessions.
    - out_filepath: path to write the CSV of predicted values.
    - prob_threshold: threshold to decide if a session belongs to Joe.
    - predict_probabilities: output probabilities instead of 0s and 1s.
    - threads: number of threads to use for the prediction.
    - overwrite: overwrites the out_filepath if it exists.
    - quiet: supress the printing of the pipeline steps.
    """

    def say(msg):
        if not quiet:
            print(msg)

    if isfile(out_filepath) and not overwrite:
        print(f"File exists: {out_filepath}")
        print("Use --force to overwrite it")
        exit_the_script()

    out_dir = dirname(out_filepath)
    if out_dir and not isdir(out_dir):
        makedirs(out_dir, exist_ok=True)

    start_time = datetime.now()
    say(f"Started at {start_time}\n---")

    say(f"\nRead the dataset: {in_filepath}")
    sessions = read_dataset(in_filepath)
    say(f" -> n, m = {sessions.shape}")

    if sessions.empty:
        print("The dataset looks empty.")
        exit_the_script()

    na_ratio = check_na_ratio(sessions)
    if na_ratio > 0:
        say(f" -> {na_ratio:.2%} missing data")

    say("\nExtract selected sites visits per session")
    visits = extract_site_visits_as_df(sessions)
    visits = keep_only_selected_site_visits(visits, say)

    say("\nParse the input data")
    parse_sessions_data_inplace(sessions, visits)
    say(f" -> n, m = {sessions.shape}")

    say("  Add the sites visited as new variables")
    sessions = add_sites_visited_to_sessions(sessions, visits)
    say(f" -> n, m = {sessions.shape}")

    say("  Make dummy variables from categoricals")
    sessions = add_dummies_from_categoricals(sessions)
    say(f" -> n, m = {sessions.shape}")

    say("  Keep only (or add if missing) the necessary features")
    sessions = impute_missing_features(sessions, say)
    sessions = match_the_model_features(sessions)
    say(f" -> n, m = {sessions.shape}")

    say("\nMake the predictions")
    model = load_model(threads)
    say(" -> Model loaded")
    thr = get_precision_recall(prob_threshold)
    if thr is not None and not predict_probabilities:
        say(f"    Using probability threshold = {prob_threshold}")
        say(f"    Expect precision = {thr.precision} | recall = {thr.recall}")

    probabilities = model.predict_proba(sessions)[:, 1]
    # ^ model.predict_proba outputs an n x 2 array
    # The probabilities of being Joe are in the second column
    # We keep that column as a 1-dim array

    if predict_probabilities:
        predictions = probabilities
        say(" -> Output probabilities instead of 0s and 1s")
    else:
        predictions = (probabilities >= prob_threshold) * 1  # converts to int

        say(f"    Caught Joe in {predictions.sum()} "
            f"({predictions.mean():.2%}) of the sessions")

        # NOTE:
        #
        # In the training of the models, the response variable Y was
        # coded like this: 0 = is not Joe (null hypothesis), 1 = is Joe.
        #
        # The desired output code is the reverse: 0 = is Joe, 1 = is not Joe.
        # We invert here the predictions to match this code.
        predictions = [1 - y for y in predictions]

    say(f" -> Write the predictions to: {out_filepath}")
    with open(out_filepath, "w+") as f_out:
        for y_val in predictions:
            f_out.write(f"{y_val}\n")

    end_time = datetime.now()
    say("\n---")
    say(f"Finished at {end_time}")
    say(f"Took {(end_time - start_time).seconds} seconds")


if __name__ == "__main__":
    args = docopt(__doc__)
    main(
        in_filepath=args["--input-json"],
        out_filepath=args["--output-csv"],
        prob_threshold=float(args["--prob-threshold"]),
        predict_probabilities=args["--probabilities"],
        threads=int(args["--threads"]),
        overwrite=args["--force"],
        quiet=args["--quiet"],
    )
