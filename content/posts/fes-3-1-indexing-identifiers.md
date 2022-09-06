---
title: "Indexing Identifiers"
date: 2022-09-06T14:09:02+02:00
draft: false
---

Indexing identifiers is key to disambiguating entities.

Wikipedia has [disambiguation pages](https://en.wikipedia.org/wiki/Category:Disambiguation_pages).
For example, there are various concepts in mathematics and computing, various computing products,
and various companies that identify with the term
"[Precision](https://en.wikipedia.org/wiki/Precision)". I made [disambiguation pages for
same-chemical-formula inorganic crystal
structures](https://web.archive.org/web/20220906121536/https://legacy.materialsproject.org/Fe2O3/)
for the Materials Project.

Indexing identifiers is also key to unifying entities. It's an [open
world](http://dbpedia.org/resource/Open-world_assumption) after all,[^1] with a comcomitant
[non-unique naming assumption](https://chempedia.info/info/nonunique_naming_assumption/). OpenAlex
[indexes various ID types for a work](https://docs.openalex.org/about-the-data/work#ids). For
example,
[http://api.openalex.org/works/https://doi.org/10.7717/peerj.4375](http://api.openalex.org/works/https://doi.org/10.7717/peerj.4375)
will funnel you to the payload for `https://openalex.org/W2741809807`, which has an `ids` field with
`openalex`, `doi`, `mag` (Microsoft Academic Graph), `pmid` (Pubmed), and `pmcid` (Pubmed Central)
IDs.

Finally, indexing identifiers is key to registering and resolving metadata, i.e. relationships
between identifiers. Registries include [Linked Open Vocabularies
(LOV)](https://lov.linkeddata.es/dataset/lov), the [Ontology Lookup Service
(OLS)](https://www.ebi.ac.uk/ols/index), the [Zazuko Prefix Server](https://prefix.zazuko.com/), and
the [OBO Foundry](https://obofoundry.org/). Resolvers include
[Identifiers.org](https://identifiers.org/) and [Name-To-Thing (n2t)](https://n2t.net/). There is
even at least one *meta*registry, [Bioregistry.io](https://bioregistry.io/).

Any time you encounter a web service using a "remote data access" style, i.e. exposing a query
language via a single access point -- SQL, SPARQL, GraphQL, MongoDB, etc. -- its highly likely that
all entity identifiers are indexed to support efficient retrieval and combination/joining.



[^1]: Unless you can bask in glorious isolation  in a siloed domain/organization.