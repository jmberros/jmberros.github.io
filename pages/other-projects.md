---
title: Other Projects
layout: post
---

# Cargo Data Analysis

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

<video width="90%" muted autoplay controls>
    <source src="/images/cargo/cargo-interactive-demo.webm" type="video/webm">
</video>

Another useful visualization was provided: a **calendar heatmap**,
where we can see the number of measurements per day at each cargo site.
A very irregular pattern of data availability emerges, with whole days when we
have no new information:

<div class="showcase-img">
  <a href="/images/cargo/cargo-github-heatmap.png">
    <img class="with-border" src="/images/cargo/cargo-github-heatmap.png" width="80%">
  </a>

  <div class="caption">
     Number of measurements per day at Site number 1.
  </div>
</div>
