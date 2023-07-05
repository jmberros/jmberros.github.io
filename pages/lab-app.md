---
title: Interactive App for Genetic Reporting
layout: post
---

I developed from scratch and maintained during +6 years an internal web
application based on **Ruby on Rails** for Biocodices, a medical genomics laboratory.

The app serves as an **online inventory** of patients, clinics, doctors and DNA
testing results, implements the
[CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete)
operations through a user-friendly interface, **automates the data entry** of
forms and **bulk-editions** of different types of data, as well as the generation
and **interactive edition of PDF reports** to communicate the results.

This _in house_ software has saved the laboratory thousands of dollars in
proprietary LIMS (Laboratory Information Management Software).

IMPORTANT NOTE: All the patient, doctor and clinic names in the screenshots
have been <span class="warning-text">anonymised with fake names</span> from the Ruby gem
[Faker](https://github.com/faker-ruby/faker) for the purposes of this showcase.
<span class="warning-text">Sensitive data has also been blurred</span> in the screenshots.

### Interactive customization of PDF reports

Interactive edition and generation of PDF reports based on database data with
user customizations thorough an easily editable YAML (black textarea on the
right).

<div class="showcase-img">
  <a href="/images/lab-app/edit-PNC.png">
    <img class="with-border" src="/images/lab-app/edit-PNC.png" width="100%">
  </a>
  <a href="/images/lab-app/edit-NGA.png">
    <img class="with-border" src="/images/lab-app/edit-NGA.png" width="100%">
  </a>
</div>

### Interactive generation of stats for different subsets of data

jQuery-powered highly interactive generation of stats for internal reporting
of the lab performance on different clinics, methods, periods, etc.

<div class="showcase-img">
  <a href="/images/lab-app/stats.png">
    <img class="with-border" src="/images/lab-app/stats.png" width="100%">
  </a>
</div>

### Inventory of cases, samples, patients, DNA test results, etc.

Easy creation, edition, deletion of several types of entities related to the
lab daily work.

<div class="showcase-img">
  <a href="/images/lab-app/lab-cases-index.png">
    <img class="with-border" src="/images/lab-app/lab-cases-index.png" width="100%">
  </a>
</div>

Inline edition of DNA library details, based on jQuery.

<div class="showcase-img">
  <a href="/images/lab-app/edit-library.png">
    <img class="with-border" src="/images/lab-app/edit-library.png" width="100%">
  </a>
</div>

Billling index for sales people.

<div class="showcase-img">
  <a href="/images/lab-app/billing-index.png">
    <img class="with-border" src="/images/lab-app/billing-index.png" width="100%">
  </a>
</div>

Bulk-edition of cases.

<div class="showcase-img">
  <a href="/images/lab-app/bulk-edit-cases.png">
    <img class="with-border" src="/images/lab-app/bulk-edit-cases.png" width="100%">
  </a>
</div>

### Workflows for the creation of cases, patients and samples

Beginning of a workflow with the creation of a new Case.

<div class="showcase-img">
  <a href="/images/lab-app/workflow-1-new-case.png">
    <img class="with-border" src="/images/lab-app/workflow-1-new-case.png" width="80%">
  </a>
</div>

Creation of a new patient as continuation of the workflow.

<div class="showcase-img">
  <a href="/images/lab-app/workflow-2-new-patient.png">
    <img class="with-border" src="/images/lab-app/workflow-2-new-patient.png" width="80%">
  </a>
</div>

### User edition for admins

Edition of diferential access for types of users.

<div class="showcase-img">
  <a href="/images/lab-app/users-edit.png">
    <img class="with-border" src="/images/lab-app/users-edit.png" width="80%">
  </a>
</div>

### Complex design of a MySQL database

A quite complex design of a MySQL database was needed for this app. Centered around
the entity of "Cases" (typically, a case is one order of genetic testing from one patient),
it grew to have multiple samples per case/patient, patients, medical doctors, and
clinics associated to each case, laboratory equipment used for each case (the reactives
of the DNA sequencing), and different types of reports.

The UML diagram of the database is included as an illustration of this challenge:

<div class="showcase-img">
  <a href="/images/lab-app/database-UML.png">
    <img class="with-border" src="/images/lab-app/database-UML.png" width="80%">
  </a>
</div>
