---
title: "W3C data recommendations -- there are many!"
date: 2022-06-01T09:17:13-04:00
draft: false
---

The World Wide Web Consortium (W3C) publishes a range of specifications and guidelines which help move web standards forward.

However, even when restricting scope to the Latest version of specifications with the status Recommendation and with the tag Data, there are currently 77 of them: <https://www.w3.org/TR/?tag=data&status=REC&version=latest>!

I read through the listing, and here I try to categorize and present a subset of the specifications that I think are most relevant to scientific data management:

- description representations, i.e. formal ways to define and communicate data, metadata, and queries:

    - Resource Description Framework (RDF)
    - SPARQL Protocol and RDF Query Language (SPARQL)

- description metamodels, i.e. formal ways to define and communicate models:

    - Shapes Constraint Language (SHACL)
    - Relational Database to RDF Mapping Language (R2RML)
    - RDF Schema
    - Web Ontology Language (OWL)
    - Rule Interchange Format (RIF)

- description models, i.e. models that may be applied directly or may serve as umbrellas for more specialized models:

    - Data Catalog Vocabulary (DCAT)
    - Provenance Data Model (PROV)
    - Simple Knowledge Organization System (SKOS)
    - CSV for the Web (CSVW)
    - RDF Data Cube Vocabulary
    - Organization Ontology
    - Open Digital Rights Language (ODRL)

I have left out specifications for serialization, i.e. the text-based appearance of things when viewing/editing them and their formats as files as disk.

Still, 14 specifications is a lot! I've tried to list them out in each category in order of roughly decreasing "bang for your learning buck" for typical use cases I've encountered.

I'd love to hear from you which, if any, of the specifications above you've found useful and/or which you would like to know better (or at all!).

{{< subscribe >}}