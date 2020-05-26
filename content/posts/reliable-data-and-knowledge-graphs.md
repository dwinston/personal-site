---
title: "Reliable Data and Knowledge Graphs"
date: 2020-05-22T17:46:37-04:00
draft: false
---

What makes data reliable? A recent article[^knsci] outlines five properties. It's
1. "clean" -- formatted uniformly, conforming to certain rules/schema, etc.
2. grounded in shared meaning spaces -- names are unambiguous
3. supplied with context -- where it comes from, how it was sourced
4. accessible in a standardized format -- easily imported
5. maintained -- kept up-to-date

In
["What is a Knowledge Graph?"](http://www.semantic-web-journal.net/content/what-knowledge-graph),
a vocabulary is presented that maps to the first four properties of reliable data above:
1. A *graph* is a set of assertions expressed between entities. Meaning is encoded via
 graph structure. Cleanliness comes in part from limiting the set of relations (edges)
 under consideration for an analysis.
2. An *unambiguous graph* has these relations and entities unambiguously identified --
grounded in ontologies as shared meaning spaces.
3. A *bare statement* graph is one that does not also encode provenance,
especially justification and attribution, in the graph.
4. Use of Semantic Web standards like RDF ensure open serialization formats and query tooling.

A *knowledge graph* is then presented as an unambiguous graph, with a limited set of relations,
that encodes provenance -- and is thus not simply a "bare statement" graph.

The way that a knowledge graph encodes provenance is important for the fifth property of reliable
data above -- maintainability. One part of maintenance is about adding new facts, and another
part is about managing changes to models to keep analyses reproducible.

Knowledge graphs are self-describing, *self-revealing* (aka "intuitive").
They represent facts (data) and models (metadata) in the same, machine-readable way. An ontology is
a blueprint for your actuals in the graph, that you ship with the graph.
Add a schema graph (ontology) to an instance graph (data), and you get a
knowledge graph.[^topquadrant]

If you ensure that even tiny graphs[^nanopubs] include not only their instance data but also 
(linked identifiers for) their associated provenance, then maintenance becomes a simple
additive process, perhaps with a process akin to periodic log-structured merges for compaction.

Assertions become not-current quickly. By shipping provenance *with* the data and
not merely *alongside* it, you can ensure data reliability in-process at the query level.

[^knsci]: Fletcher et al., "Knowledge Scientists: Unlocking the data-driven organization".
[arXiv:2004.07917](https://arxiv.org/abs/2004.07917)

[^topquadrant]: I got the ships-with-the-blueprint idea, and the crisp algebra of
graph-plus-graph-equals-graph, from [these](https://www.youtube.com/watch?v=mjNaL9FJDiA)
[presentations](https://www.youtube.com/watch?v=3KA__Dcb8Ns) by TopQuadrant.

[^nanopubs]: [*Nanopublication Guidelines*](http://nanopub.org/guidelines/working_draft/).
Concept Web Alliance Working Draft, Sep 2018.

