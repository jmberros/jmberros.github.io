---
title: Some repositories & Code showcase
layout: post
---

## paip (DNA data analysis pipelines)

<a href="https://github.com/biocodices/paip" target="_blank">
  https://github.com/biocodices/paip
</a>

<strong>paip</strong> is a Luigi-based Python pipeline for the analysis of DNA
sequencing NGS data. It has routines for quality control, variant calling and
report generation, with a comprehensive unit test suite for pytest. I coded
this in the span of 2 years as new needs arised in a medical genomics
laboratory.

## anotala (annotation of mutations)

<a href="https://github.com/biocodices/anotala" target="_blank">
  https://github.com/biocodices/anotala
</a>

<strong>anotala</strong> is an Python bioinformatics utilty that lets you
annotate DNA mutations, i.e. add extra information to mutations found in a
sample like aminoacid/protein affected, coding vs. non-coding and other region
types, predicted strength of effect with different softwares, diseases
known to be associated with the mutation.

It implements a cache that can be based on MySQL, PostgreSQL or Redis.

<div style="display: flex;">
  <div class="showcase-img">
    <a href="/images/repos/qc-pipe.png">
      <img src="/images/repos/qc-pipe.png">
    </a>
  </div>

  <div class="showcase-img">
    <a href="/images/repos/vc-pipe.png">
      <img src="/images/repos/vc-pipe.png">
    </a>
  </div>

  <div class="showcase-img">
    <a href="/images/repos/ann-pipe.png">
      <img src="/images/repos/ann-pipe.png">
    </a>
  </div>
</div>

## vcf to dataframe (DNA data format conversion)

<a href="https://github.com/biocodices/vcf_to_dataframe" target="_blank">
  https://github.com/biocodices/vcf_to_dataframe
</a>

<strong>vcf_to_dataframe</strong> is a Python utilty to import a VCF file
(a standard format to store DNA variants) as a pandas DataFrame. It allows
to import any subset of samples in the file and it converts all INFO and GT
fields to Python lists or dicts to ease the downstream parsing.


## bed to tabix (1KGP genotypes downloader)

<a href="https://github.com/biocodices/bed_to_tabix">
  https://github.com/biocodices/bed_to_tabix
</a>

<strong>bed_to-tabix</strong> is a friendly Python CLI utility that will
download the genotypes of 2,504 individuals of the 1,000 Genomes Project (1KGP)
for the genome regions define in an input BED file. The script deals with
chromosome separate downloading and merging, and with temporary files clenaup.

<div class="showcase-img">
  <a href="/images/repos/bed_to_tabix.png">
    <img src="/images/repos/bed_to_tabix.png">
  </a>
</div>
