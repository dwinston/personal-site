---
title: "Indexing Validators"
date: 2022-09-07T10:26:18+02:00
draft: false
tags:
- FAIR-enabling-services
---

Why would one consider indexing validators? Reuse.

The value of reuse seems obvious for structural and semantic _specification_, i.e. schemas and
controlled vocabularies -- there is opportunity to perceive two datasets as aligned. But, this
alignment is only _indicated_, not necessarily _validated_.

Two datasets, A and B, are stated to both conform to schema S. If you wish to verify this, what do
you do? You apply a validator V to both. Therefore, it seems that if the same validator V is already
stated to have been successfully applied to both datasets A and B in order to verify conformance to
S, you will have higher confidence in proceeding to analysis without applying validation yourself,
or at least without insisting on comprehensive, compute-intensive validation by default.

A given schema-specification validator may also be relatively sophisticated and transform an input
dataset to conform more tightly to the specification, as per [Postel's
Law](https://en.wikipedia.org/wiki/Robustness_principle), making it even more valuable to reuse
unambiguously identified validators as part of data-integration workflows.

Validators may be composed, e.g. conjunctively as [attribute/predicate specs are in
Datomic](https://docs.datomic.com/on-prem/schema/schema.html#entity-predicates), encouraging
granular reuse. However, one could not naively employ conformers-as-validators in such a scheme
unless they formed a commutative semigroup (mutually rectifying robustness -- Postel would
approve!).