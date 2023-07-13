---
title: Data Modeling Projects
layout: post
---

## Cargo Data Analysis - Interactive EDA

For this project, the client had a **data challenge** to quickly analyze a dataset of
**sites where cargo accumulates over time and is picked up according to different signals**
--a mixture of automatic pickups and scheduled pickups.

We needed to visualize if there was room for improvement in the scheduling of
cargo pickup times.

The **interactive visualization** (done entierely with `matplotlib` and Jupyter
IPywidgets, after some data analysis with `pandas`) shows that a lot of
**pickup times are either quite delayed or too early**
in contrast with the scheduled times. If a
maximum cargo capacity of the site is plotted at 200K, we can see that almost all pickup
schedules could be delayed a bit, until more cargo is accumulated.


The information is evidently noisy, but a pattern emerges and there seems to be
**room for improvement of the pickup scheduling**.

This challenge --both the analysis and the interactive prototpye--
was completed in around three days of work:

<!--
<video width="90%" muted autoplay controls>
    <source src="/images/cargo/cargo-interactive-demo.webm" type="video/webm">
</video>
-->

<div class="showcase-img half-width">
  <a href="/images/cargo/cargo-github-heatmap.png">
    <img class="with-border" src="/images/cargo/cargo-analysis-1.png">
  </a>
</div>
<div class="showcase-img half-width">
  <a href="/images/cargo/cargo-github-heatmap.png">
    <img class="with-border" src="/images/cargo/cargo-analysis-4.png">
  </a>
</div>
<div class="showcase-img half-width">
  <a href="/images/cargo/cargo-github-heatmap.png">
    <img class="with-border" src="/images/cargo/cargo-analysis-6.png">
  </a>
</div>
<div class="showcase-img half-width">
  <a href="/images/cargo/cargo-github-heatmap.png">
    <img class="with-border" src="/images/cargo/cargo-analysis-7.png">
  </a>
</div>

Another useful visualization was provided: a **calendar heatmap**,
where we can see the number of measurements per day at each cargo site.
A very irregular pattern of data availability emerges, with whole days when we
have no new information:

<div class="showcase-img half-width">
  <a href="/images/cargo/cargo-github-heatmap.png">
    <img class="with-border" src="/images/cargo/cargo-github-heatmap.png">
  </a>

  <div class="caption">
     Number of measurements per day at Site number 1.
  </div>
</div>

## Catch a user based on their web visits

This data challenge was to model the behavior of one specific user (named Joe) based on
his web visits: sites visited, time of visit, location, locale, OS, browser.

Exploratory data analysis revealed mixed visits from Linux and Windows servers
and from Chrome and Firefox browsers, while the locale was exclusively `ru-RU`.
The locations varied across cities, so he seemed to be a nomadic user:

[EDA 01: Web sessions notebook](https://github.com/jmberros/jmberros.github.io/blob/main/images/catch-user/EDA-01__Sessions.ipynb)

<div class="showcase-img half-width">
  <a href="/images/catch-user/OS-browser.png">
    <img class="with-border" src="/images/catch-user/OS-browser.png">
  </a>

  <div class="caption">
      Joe visits mainly from Windows/Ubuntu, Chrome/Firefox.
  </div>
</div>

<div class="showcase-img">
  <a href="/images/catch-user/locale.png">
    <img class="with-border" src="/images/catch-user/locale.png">
  </a>

  <div class="caption">
      Joe visits always with ru-RU locale.
  </div>
</div>

<div class="showcase-img">
  <a href="/images/catch-user/cities.png">
    <img class="with-border" src="/images/catch-user/cities.png">
  </a>

  <div class="caption">
      Joe visits from multiple cities across the world.
  </div>
</div>

Auxiliary exploratory analysis on the websites revealed a small
set of sites favorite to this user.

[EDA 02: Websites visits notebook](https://github.com/jmberros/jmberros.github.io/blob/main/images/catch-user/EDA-02__Sites.ipynb)

<div class="showcase-img">
  <a href="/images/catch-user/frequent-sites.png">
    <img class="with-border" src="/images/catch-user/frequent-sites.png">
  </a>

  <div class="caption">
     Joe most frequented sites.
  </div>
</div>

<div class="showcase-img">
  <a href="/images/catch-user/frequent-sites-2.png">
    <img class="with-border" src="/images/catch-user/frequent-sites-2.png">
  </a>

  <div class="caption">
     Joe most frequented sites that were *not frequent* for other users.
  </div>
</div>

[Model selection notebook](https://github.com/jmberros/jmberros.github.io/blob/main/images/catch-user/Model_Selection.ipynb)

We compared several models, mostly ensemble types: Bagging DTs and Random Forests with
different parametrizations, and two types of logistic regressions. The clear winner was
the Bagging DTs as implemented by `sci-kit learn`. We kept a Bagging DTs model with 100
decision trees as the main hyperparameter.

<div class="showcase-img">
  <a href="/images/catch-user/models.png">
    <img class="with-border" src="/images/catch-user/models.png">
  </a>

  <div class="caption">
     Comparison of the performance of several models, mostly ensembles of decision trees (DTs).
  </div>
</div>

A confusion matrix, together with precision, recall, and F1-score were provided for
multiple probability thresholds <em>t</em>.

<div class="showcase-img">
  <a href="/images/catch-user/confusion-matrices.png">
    <img class="with-border" src="/images/catch-user/confusion-matrices.png">
  </a>

  <div class="caption">
     Confusion matrix for the chosen threshold of probability to predict that a user is Joe.
  </div>
</div>

<div class="showcase-img">
  <a href="/images/catch-user/precision-vs-recall.png">
    <img class="with-border" src="/images/catch-user/precision-vs-recall.png">
  </a>

  <div class="caption">
    Several thresholds of probability and the resulting precision and recall values.
  </div>
</div>

A **feature importance** analysis revelaed that the locale and site of visit was the
most informative piece of information, while the hour and some URLs came afterwards:

<div class="showcase-img">
  <a href="/images/catch-user/feature-importance.png">
    <img class="with-border" src="/images/catch-user/feature-importance.png">
  </a>
</div>
