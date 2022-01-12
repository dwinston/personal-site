---
title: "Metadata as Relations Between Identifiers"
date: 2022-01-12T18:03:35-05:00
draft: false
---

> An item of metadata is a relationship that someone claims to exist between two entities.[^indecs]

With [linked data](https://www.w3.org/DesignIssues/LinkedData.html), then,

> all metadata can be expressed in terms of relationships between identifiers.[^bide]

Consider that in RDF, even literals are objects. A triple with a "literal value" V as its object is
a relationship with an implicit identifier associated with the value V and also associated with a
type and a language:

```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
<#it> rdfs:label "book" .
<#it> rdfs:label "book"^^xsd:string . # type explicit
<#it> rdfs:label "book"^^xsd:string@en . # language explicit
```

This may be more clear in a JSON-LD representation, where a literal may be represented as a JSON
object with a `@value` field and with optional fields `@type` (which defaults to `xsd:string`) and
`@language` (which defaults to `en`), i.e.

```json lines
"book"
{"@value": "book"}
{"@value": "book", "@type": "xsd:string"}
{"@value":  "book", "@type": "xsd:string", "@language": "en"}
```

are equivalent. It seems helpful to explicitly associate an identifier with all literal values in an
information system, i.e. an `@id` field for a JSON-LD representation, even if the `@id` URL is not
externally resolvable and the entity's value is inlined as `@value` rather than fetched separately.

[^indecs]: G. Rust and M. Bide, "The <indecs> metadata framework: Principles, model and data
dictionary," Jun. 2000. [Online]. Available:
https://www.doi.org/topics/indecs/indecs_framework_2000.pdf

[^bide]: M. Bide, "Standard Identifiers: an overview of the current landscape," presented at the
USPTO Open Meeting: Facilitating the Development of the Online Licensing Environment for Copyrighted
Works, Apr. 01, 2015. [Online]. Available:
[pdf](http://www.linkedcontentcoalition.org/phocadownload/150401%20BIDE%20Standard%20Identifiers%20Overview%20with%20embedded%20slides.pdf)


