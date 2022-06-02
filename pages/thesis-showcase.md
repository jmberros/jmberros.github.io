---
title: Thesis showcase
layout: post
---

This thesis was presented in the Faculty of Exact and Natural Sciences of the
University of Buenos Aires (UBA) in 2022. It's a Bioinformatics and
Biostatistics analysis of several kinds of genetic scores associated to
disease, mainly utilised to diagnose embryos during <em>in vitro</em> fertilization.

Some results and figures are showcased here.

## Theoretical description of genetic data under different disorders

We described the expected distribution of a genetic data statistic called BAF
under different disorders and levels of mosaicism, which means different
percentages of mutated cells in a sample.

<div class="showcase-img">
  <img src="/images/thesis-showcase/monosomy-densities.png" width="60%">
  <img src="/images/thesis-showcase/trisomy-densities.png" width="60%">

  <div class="caption">
  Theoretical distribution of a statistic called BAF (B allele frequency)
  under different levels of mosaicism $m$, in monosomy and in trisomy.
  </div>

</div>

We described the expected behavior of a single measure $\theta$ that helped
designing statistical tests to easily detect these disorders.

## Simulation genetic data with different degrees of mosaicism

We simulated genetic data for different levels mosaicism, based on the
theoretical framework developed for the thesis.

<div class="showcase-img">
  <img src="/images/thesis-showcase/monosomy-simu.png" width="80%">
  <img src="/images/thesis-showcase/trisomy-simu.png" width="80%">

  <div class="caption">
  Simulated BAF ("B" allele frequency) for different levels of mosaicism $m$ in
  two different cases: monosomy (top) and trisomy (bottom).
  </div>

</div>

## Performance and empirical distribution of a new statistic

We developed and described a new statistic to detect aneuploidies in embryos,
leveraging on a robust measure of dispersion called median absolute deviation
(MAD).

<div class="showcase-img">
  <img src="/images/thesis-showcase/gMAD-performance.png" width="70%">
  <br/>
  <img src="/images/thesis-showcase/T3-empirical-percentiles.png" width="70%">

  <div class="caption">
  Performance of a new statistic $T_3$ for the detection of genetic disorders
  under several scenarios (top). Empirical distribution of this statistic under
  the null hypothesis of a healthy embryo, to decide the threshold of detection
  (bottom).
  </div>

</div>

## Performance of testing with overlapping-windows of data

We described a problem with non-overlapping windows of data when searching
for genetic disorders that span few megabases in a chromosome (that means,
mutations that span a relatively small region).

<div class="showcase-img">
  <img src="/images/thesis-showcase/windows-overlap.png" width="70%">

  <div class="caption">
  In orange, a small region of a chromosome affected by a disorder called
  monosomy. The test statistic $T_1$ is maximized with overlapping windows
  (blue), favoring detection.
  </div>

</div>

## Estimator performance evaluation

We evaluated the performance of a new estimator of the level of mosaicism
with simulated embryo samples.

<div class="showcase-img">
  <img src="/images/thesis-showcase/estimators-performance.png" width="80%">

  <div class="caption">
    Performance of the estimator $\hat{m}$ under different values of $m$ in
    two settings, trisomy and monosomy.
  </div>

</div>

## Complex patterns of DNA contamination

We analyzed the BAF statistic under different levels of DNA mixture (or
"contamination") between mother and embryo.

<div class="showcase-img">
  <img src="/images/thesis-showcase/mother-dna-contamination.png" width="70%">

  <div class="caption">
  Patterns of BAF under different levels of mother-embryo DNA mixture.
  In colors the possible genotype combinations.
  </div>
</div>

## Genomic panel target distribution

We analyzed the distribution of "probes" or targets in a genomic panel,
with emphasis in the distribution of the size of the gaps with no data left by
the panel.

<div class="showcase-img">
  <img src="/images/thesis-showcase/panel-snps.png" width="70%">

  <div class="caption">
  Schematic design of a panel of genomic targets (top).
  Distribution of the size of gaps left by the panel design (bottom).
  </div>
</div>

## Anticorrelation between Polygenic Risk Scores

We analyzed the correlation of [Polygenic Risk
Scores](https://en.wikipedia.org/wiki/Polygenic_score) (PRS), a kind of genetic
score computed from hundreds or thousands of mutations in the genome. We found
several pairs of diseases, like rheumatoid arthritis and multiple sclerosis,
with negatively correlated scores. An example is given in the figure below.

<div class="showcase-img">
  <img src="/images/thesis-showcase/PRS-anticorrelation.png" width="80%">

  <div class="caption">
    Rheumatoid Arthritis and Multiple Sclerosis have anticorrelated scores.
    We still see the correlation when converting the PRS to absolute risk (RA).
    A Student's $t$ test of paired samples shows a significant increase in risk
    when selecting individuals of low PRS.
  </div>

</div>

## Variance trajectories of sub-scores

We analyzed the proportion of variance $\mathcal{V}_{(k)}$ captured by the
genetic scores when keeping sub-selections of the $k$ strongest-effect
mutations. These captured-variance trajectories help quantify the degree of
<strong>polygenicity</strong> of a given disease. Low polygenicity means that
few mutations determine most of the risk.

<div class="showcase-img">
  <img src="/images/thesis-showcase/variance-trajectories.png" width="70%">

  <div class="caption">
    Highlighted phenotypes in blue have pronounced captured-variance
    trajectories, this means they have low polygenicity.
  </div>
</div>

## Graph of diseases with correlated genetic risk

We found a surprising "natural" grouping of autoimmune diseases based on the
correlation between their polygenic scores.

<div class="showcase-img">
  <img src="/images/thesis-showcase/diseases-graph.png" width="50%">

  <div class="caption">
  Directed graph of polygenic score correlations. The diseases naturally
  form two groups (left vs. right), with correlations only found inter-group
  and never intra-group.
  </div>
</div>

## Simulation of embryos and performance of embryo-selection strategies

We simulated genetic data from embryos and analyzed the results of selecting
embryos based on their genetic scores. A potential problem was described where
embryos with low genetic score of one disease might have increased risk of
a correlated disease.

<div class="showcase-img">
  <img src="/images/thesis-showcase/embryo-strategies.png" width="70%">

  <div class="caption">
  The whole set of simulated embryos is shown in grey, with the embryos of
  parents in the first quintile of PRS in orange. Blue dots are the low-risk
  embryos as selected by different strategies. The subgroup of selected
  embryos based on one score (X axis) has an increased absolute risk of a
  different disease (Y axis) under some strategies.
  </div>
</div>

## Relation between increase in risk and number needed to harm

A knwon metric in epidemiology called Number Needed to Harm (NNH) is plotted
against the increase in absolute risk (IRA) for several pairs of anticorrelated
diseases. This illustrates that between 250 and 1250 couples applying a
PRS-based embryo selection might be enough to produce unwanted new cases of
some diseases.

<div class="showcase-img">
  <img src="/images/thesis-showcase/IRA-NNH.png" width="50%">

  <div class="caption">
  Relation between increase in absolute risk (IRA) and number needed to harm
  (NNH) for several pairs of diseases found to be anticorrelated in the thesis.
  </div>
</div>
