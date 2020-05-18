---
title: "Data Discovery and Join-Path Discovery"
date: 2020-05-18T11:00:43-04:00
draft: false
---

How do you source data relevant for some analysis? Once you "have" the data, how do you feed it to the analytic task?

Traditional *enterprise data integration* joins paths across a handful of silos
for a handful of specific analytic tasks.
In data science, however, neither the set of relevant silos nor the set of relevant analytic tasks are both small and
well-defined.

Just as business enterprises sanction siloing for business units, academic research groups sanction siloing
for their members. Lab members can certainly collaborate, but each graduate student and postdoc typically is
granted operational agility sufficient to distinguish themselves as a research unit with their own output, such as 
first-author publications.

A business enterprise, to facilitate
 operational agility, will allow individual business units to "do their own thing." This leads to data silos, 
 one for each unit. Common analytic tasks that motivate joins across silos include:
 negotiating with suppliers, where data sourced from each unit's procurement systems can help suggest
 terms and conditions for new vendor contracts; and classifying spending, where taxonomies for parts and
 transactions can help reconcile overall strategy with resource allocation.

In "Data Integration: The Current Status and the Way Forward,"[^stonebraker]
Stonebraker and Ilyas discuss how to support the work of data scientists within enterprises.
Given the rise of data-intensive science[^dataintensive],
their discussion pertains to many research groups as well.

Data discovery is the use of relationships across silo metadata to source data relevant for some set
of analytics tasks. These relationships can be in some cases automatically discovered,
which is valuable when silos don't explicitly include such relationship metadata.

Join-paths, across relationships, are how data are feed to specific analytic tasks. Join-paths can also in
some cases be automatically discovered,
which is valuable when potential analytics tasks are numerous or not pre-defined.

You have local access to structured databases, to directories of individual files, and you'd like to access
 public data sources as well. You also have a battery of analytic tasks, many of which might have known schemas
 for inputting data. The nature and number of these data sources and analytic tasks change over time.
 Data discovery and join-path discovery are key ideas to achieve high-quality results
in this kind of environment within hours or days rather than weeks or months.

Stonebraker and Ilyas mention use of "semantic features of the various tables and columns" and of 
"semantically coherent join paths," with references to recent academic projects.
Semantic Web technologies such as RDF graphs and ontology-aware SPARQL engines are well-suited to help tackle
these discovery problems.
 

[^stonebraker]: Stonebraker and Ilyas, "Data Integration: The Current Status and the Way Forward,"
IEEE Bulletin of the Technical Committee on Data Engineering, 41 (2), June 2018.
[[pdf](http://sites.computer.org/debull/A18june/p3.pdf)]

[^dataintensive]: *The Fourth Paradigm: Data-Intensive Scientific Discovery*. Microsoft Research, 2009.
