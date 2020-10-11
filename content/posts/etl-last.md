---
title: "ETL Last"
date: 2020-10-11T10:13:21-04:00
draft: false
---

What matters for application of knowledge -- what substantiates it? I think two things do:
shared conceptualizations, and use cases.

Shared conceptualizations, or ontologies, materialize entities and their relations with each other
(i.e. object properties) and with data literals / annotations (i.e. data properties).
Applying such a conceptualization to given instances
(and bundling this application with the conceptualization) results in a
graph -- not a system of interlocking tables (i.e. a relational database).

Use cases materialize access patterns. Use cases manifest as user interfaces with affordances for
interpretation of and interaction with the knowledge graph - with the shared conceptualization along
with the known concrete entities and literals to which that ontology is asserted to apply.

Once use cases as prototyped are validated, then the observed shapings of data in service of the access
patterns may themselves be materialized with some confidence. These shapings are your system of interlocking
tables (e.g. SQL), your collections of JSON documents (e.g. MongoDB), etc.

ETL takes you from one shaping of data to another. A knowledge graph has the most
general structure -- the least possible shaping. To develop use cases is to discover shapings. Once you
identify shapings, you can ensure adequate ongoing performance of use cases (i.e. in "production")
by implementing ETL from your source graph to appropriate shapings that in turn are exposed by APIs.