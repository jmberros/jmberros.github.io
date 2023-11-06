---
title: Streamlit Data Explorations
layout: post
---

This work for a client involved rapid prototyping of internal data exploration apps
leveraging on a huge Snowflake database as resource and Streamlit as a tool to produce
interactive visualizations.

One exploration involved diving deep into a dataset of socioeconomic, demographics,
personal, and consumer information ([Infutor](https://batchdocs.infutor.com/)). The
Snowflake table had 250m rows, so random samples were extracted and processed in real
time, from user interaction, with the help of `polars`, a dataframe library that can be
many times faster than `pandas`.

<div class="showcase-img">
  <a href="/images/sfra/infutor-insights.png">
    <img class="with-border" src="/images/sfra/infutor-insights.png" width="80%">
  </a>

  <div class="caption">
  Fast interactive exploration of the top consumer interests of any combination
  of demographics and geographic categories.
  </div>
</div>

Another exploration involved a collection of tables from
[Cybersyn](https://www.cybersyn.com/), comprising multiple timeseries from the Bureau of
Labor Statistics, the Federal Reserver Economic Data, USPS addresses and address
changes. Here, the solution involved interactively querying Snowflake to produce
up-to-date plots with several parameters that the user could modify --i.e. normalized or
unnormalized variables, seasonal adjustment, custom aggregation of industry types and
geographic locations like arbitrary combinations of cities, metropolitan areas, or
state


<div class="showcase-img">
  <a href="/images/sfra/page-01.png">
    <img class="with-border" src="/images/sfra/page-01.png" width="80%">
  </a>
  <div class="caption">
  Timeseries of normalized employment for a selection of industries.
  </div>
</div>
<div class="showcase-img">
  <a href="/images/sfra/page-03.png">
    <img class="with-border" src="/images/sfra/page-03.png" width="80%">
  </a>
  <div class="caption">
  Stacked barplot of selected industries and their share of non-farm payrolls over
  the years.
  </div>
</div>
<div class="showcase-img">
  <a href="/images/sfra/page-04.png">
    <img class="with-border" src="/images/sfra/page-04.png" width="80%">
  </a>
  <div class="caption">
  Timeseries of net migration in a chosen city with the detail of inbound and outbound
  address  changes.
  </div>
</div>

