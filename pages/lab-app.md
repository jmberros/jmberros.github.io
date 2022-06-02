---
title: Web App for Medical Genomics Laboratory
layout: post
---

I developed from scratch and maintained during +6 years an internal web
application based on **Ruby on Rails** for a medical genomics laboratory, while
I completed my thesis on site.

The app serves as an **online inventory** of patients, clinics, doctors and DNA
testing results, implements the
[CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete)
operations through a user-friendly interface, **automates the data entry** of
forms and **bulk-editions** of different types of data, as well as the generation
and **interactive edition of PDF reports** to communicate the results.

This _in house_ software has saved the laboratory thousands of dollars in
LIMS (Laboratory Information Management Software).

IMPORTANT NOTE: All the patient, doctor and clinic names in the screenshots
have been replaced with **fake names** from the Ruby gem
[Faker](https://github.com/faker-ruby/faker) for the purposes of this showcase.
Sensitive data has also been blurred in the screenshots.

### Interactive customization of PDF reports

Interactive edition and generation of PDF reports based on database data with
user customizations thorough an easily editable YAML (black textarea on the
right).

<div class="showcase-img">
  <img class="with-border" src="/images/lab-app/edit-PNC.png" width="100%">
  <img class="with-border" src="/images/lab-app/edit-NGA.png" width="100%">
</div>

### Interactive generation of stats for different subsets of data

jQuery-powered highly interactive generation of stats for internal reporting
of the lab performance on different clinics, methods, periods, etc.

<div class="showcase-img">
  <img class="with-border" src="/images/lab-app/stats.png" width="100%">
</div>

### Inventory of cases, samples, patients, DNA test results, etc.

Easy creation, edition, deletion of several types of entities related to the
lab daily work.

<div class="showcase-img">
  <img class="with-border" src="/images/lab-app/lab-cases-index.png" width="100%">
</div>

Inline edition of DNA library details, based on jQuery.

<div class="showcase-img">
  <img class="with-border" src="/images/lab-app/edit-library.png" width="100%">
</div>

Billling index for sales people.

<div class="showcase-img">
  <img class="with-border" src="/images/lab-app/billing-index.png" width="100%">
</div>

Bulk-edition of cases.

<div class="showcase-img">
  <img class="with-border" src="/images/lab-app/bulk-edit-cases.png" width="100%">
</div>

### Workflows for the creation of cases, patients and samples

Beginning of a workflow with the creation of a new Case.

<div class="showcase-img">
  <img class="with-border" src="/images/lab-app/workflow-1-new-case.png" width="80%">
</div>

Creation of a new patient as continuation of the workflow.

<div class="showcase-img">
  <img class="with-border" src="/images/lab-app/workflow-2-new-patient.png" width="80%">
</div>

### User edition for admins

Edition of diferential access for types of users.

<div class="showcase-img">
  <img class="with-border" src="/images/lab-app/users-edit.png" width="80%">
</div>
