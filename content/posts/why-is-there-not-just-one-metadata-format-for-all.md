---
title: "Why Is There Not Just One Metadata Format for All Kinds of Research Data?"
date: 2022-05-13T09:21:10-07:00
draft: false
---

> Why is there not just one metadata format for all kinds of research / data?
>
> -- asked on [fairdataforum.org](https://fairdataforum.org/t/fair-aware-tool-faq/479/3)


Metadata modeling and formatting are separate concerns. It is reasonable that different scientific domains and studies within domains may have widely varying modeling concerns. Controlled vocabulary terms, validity constraints, and other metadata elements will surely vary and evolve over time.

What’s not as obvious is why different scientific domains and studies within domains would have different formatting concerns. Different software applications and tools may have their preferred metadata formats for operational convenience. Thus, as some software gains prominence in a specific domain, its preferred format may be adopted by other tools in the ecosystem for ease of exchange and integration.

For there to be a single metadata format that is universally adopted for metadata exchange — that is, a format that a given software tool may convert to a preferred internal format for convenience of use by the tool — that format would need to be able to communicate the model being used as well. Thus, the format would need to host a language for defining models.

There have been some efforts at this. One effort that has gained some recognition in the FAIR data community is that of the Semantic Web set of standards. Specifically, the Resource Description Framework (RDF) base model, exchanged using a handful of standardized plain-text formats such as JSON-LD, and using RDF-expressed modeling languages such as RDFS (RDF Schema), OWL (Web Ontology Language), and SHACL (Shapes Constraint Language), is one effort towards a universal “meta-model” for defining and exchanging metadata models along with the metadata itself, in plain-text formats that both humans and machines can interpret unambiguously, if only to convert metadata to preferred internal modeling languages and formats.

{{< subscribe >}}