---
title: Scoring of 23m geocoding results
layout: post
---

My last project at **Grata Inc.** involved the development of an **automatic evaluation
method** to determine if **geocoding results** from external APIs (Geocode Earth,
Mapbox) looked wrong and needed revision. Geocoding means that a raw address is
converted into structured data of a location: the city, the state, the country, etc.

With this purpose, I designed a **scoring method for US geocoding results** that leveraged
on on public data from the ZIP codes present in the raw addresses. A simple
score where the correctness of the state and city weighed differently 
was combined with the distance in kilometers between the ZIP data and the geocoding
result, which included latitude and longitude. A couple of decision rules with
**thresholds tuned after analysis of a large sample** proved effective to quickly decide if
a given API result was trustworthy, highlighting a tail of bad results that those APIs
gave for some corner cases of noisy addresses.


<div class="showcase-img">
  <a href="/images/grata-locations/evaluation.png">
    <img class="with-border" src="/images/grata-locations/evaluation.png" width="80%">
  </a>

  <div class="caption">
  Sample of ~5K geocoding results evaluated levaraging on the ZIP code data found in the
  input address. The color scale represents a score based on the number of fields
  that are correct. Geocoding results farther from the ZIP reference tend to be wrong by
  this scoring method. A threshold-based rule using the score and the distance from the
  ZIP reference lets us easily highlight --and reject-- API results that are wrong
  </div>
</div>

This evaluation was performed on 23m existing records in the database, as well as
being implemented as a new step in the evaluation of incoming geocoding results.
