---
title: "When ETL Is a Symptom"
date: 2021-04-22T16:57:55-04:00
draft: false
---

When you have several different applications (e.g. to perform simulations and analyses) that each
have their own data model, it's typical for each to also maintain its own siloed data store. Then,
in order to use all the applications in concert to complete a research project, or to support an
ongoing research program, you need to run extract-transform-load (ETL) pipelines to sync the data.

In the best case for such an application-centric architecture, you may have a central data store
with which each application-specific store performs ETL. In the worst case, you have quadratic
growth of point-to-point ETL.

Even if every application's data is technically in the same store (e.g. a "data lake"), each
application's data model can be arbitrarily different from the others', necessitating custom
transformations to be implemented and maintained over time.

In this scenario, ETL is a symptom of data diseconomy. You may recognize and budget for "technical
debt" when optimizing for expediency in developing a given application, perhaps to hit a conference
deadline. This debt is at the code level. However, beware also of "integration debt" at the data
level if adding a new software tool with an arbitrarily different data model.

What is an alternative to ballooning ETL efforts? Though it takes discipline, a data-centric,
(data-)model-driven architecture is a way out of the quagmire.[^1]

I don't have a catchy-acronym substitute for ETL -- perhaps cache, map, cache (CMC), where bookend
caching is optional, an incidental performance optimization. That is, one can federate virtualized
queries that map at query time, e.g. via the [R2RML](https://www.w3.org/TR/r2rml/) standard if a
given application needs to work with data in a tabular form rather than the document/graph form of a
central data store. The "mapping" is just one of form -- the underlying data model is shared across
all applications.

[^1]: McComb, Dave. *The Data-Centric Revolution: Restoring Sanity to Enterprise Information
Systems*. Technics, 2019.

{{< subscribe >}}