---
title: "Cleanup of a database of 10M company names"
layout: post
---

During six months at **Grata Inc.**, I had the chance to devote myself to a gargantuan challenge: **cleaning up a database of roughly 10M company names**, mainly in English, but with other languages present as well. The company names table had multiple issues to be addressed:

- Names that were **too short**: 1 and 2-letter names, a complex mixture of wrong names and correct acronyms.
- Names that were **too long**: a mixture of valid long names and names with a tagline or description to be removed.
- Names with **decorative characters** of all sorts: emoji, unwanted "fancy" letters using math symbols, non-English characters and punctuation characters used decoratively.
- Names with **extraneous phrases** of various flavors: "we are hiring", "Foo Inc., formerly Bar LLC", "acquired by X", "powered by Y", "a division of Z group", taglines, marketing phrases, etc.
- Wrongly scraped names that did not match the company at all.
- **Mojibake**, aka the weird characters that appear after decoding text with the wrong character encoding.

With this purpose, a **cohesive OOP solution** was crafted from scratch and developed over the course of months: a **Name Refiner class with a complementary name-utils module**. The class and the utils module grew progressively as new fixes were addressed. Unit and integration **testing** for all features were *religiously* provided.

The core of the Refiner was a **novel scoring method proposed for the company names**. The score leveraged as much as possible on the available company data, e.g. the domain, the social media handles, and multiple (and sometimes different) names for the same company from different sources. The idea was to **quantify an intuitive notion of what a "correct" company name was** in this context, as a name that matched the domain and/or handles at least approximately. For this, string similarity measures had to be combined with loads of domain-specific logic so that the results matched what was oftentimes obvious to the human eye, but also full of hardly automatable subtleties.

Moreover, every fix was accompanied by a non-empty set of incorrectly "fixed" marginal cases, where the automation did not apply. Huge efforts were geared towards avoiding these negative side effects as much as possible. The hard-earned lesson was that in a set of millions of datapoints, every proposed solution has tradeoffs.

**Performance needs** were also addressed, since a massive backfill was run in production each time a fix was merged to main.

Last but not least, the Name Refiner was carefully written and rewritten with code readability and maintainability in mind.

