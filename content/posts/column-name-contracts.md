---
title: "Column-Name Contracts"
date: 2022-01-24T14:18:07-05:00
draft: false
---

URIs are great for namespacing terms. However, the local names — after the last `/` — could be a
free-for-all. One common convention — but not typically a *contract* — is to use upper camel case
for [rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class) instances and lower camel case for
[rdf:Property](http://www.w3.org/1999/02/22-rdf-syntax-ns#Property) instances. Is it useful to
systematize the construction of local names? [Emily Riederer argues
yes](https://emilyriederer.netlify.app/post/column-name-contracts/).

I like her general approach, and I think her eight "level 1" measure types are nice examples that
could be accepted without discussion by many teams. I often start "count of quanity or event
occurrence" terms with `n_` and "unique identifer for an entity" terms with `id_` in my code.


A pleasant surprise was seeing a concept map at the end of the post, a boxes-and-arrows diagram to
help illustrate the concepts from the post, which I have reproduced here:

<figure> <img src="/img/column-name-contracts.png" width="100%" alt="concept map for column name
contracts" title="concept map for column name contracts"/>
<figcaption>Concept map for column name contracts.</figcaption>
</figure>

I would like to more formally represent the knowledge expressed in my writing. Step one seems to be
to draw out a concept map. After this, I can translate such a diagram to RDF. In this way, I might
build up a queryable knowledge base. Perhaps more importantly, I will encounter and hopefully
overcome many obstacles to doing this effectively, including weaknesses in tooling.

To start, here is a tiny RDF dataset of the above concept map, serialized as turtle:

```ttl
@prefix : <https://ns.polyneme.xyz/ark:57802/2022/01/dwi/cnc/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

:Dataframe a owl:Class .
:Column a owl:Class .
:DataType a owl:Class .
:Unit a owl:Class .
:Meaning a owl:Class .
:Name a owl:Class .
:Validation a owl:Class .
:Documentation a owl:Class .
:DataDictionary rdfs:subClassOf :Documentation .
:ERDiagram rdfs:subClassOf :Documentation .

:has a owl:ObjectProperty ; owl:inverseOf rdfs:member .
:shouldEncode a owl:ObjectProperty .
:canSupport a owl:ObjectProperty .
:shouldCheckConsistencyOf a owl:ObjectProperty .
:explainedIn a owl:ObjectProperty .
```

The most important aspect of this is that the URLs for the new vocabulary resolve. 😊