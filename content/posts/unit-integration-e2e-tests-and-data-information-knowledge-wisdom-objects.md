---
title: "{Unit,Integration,End-to-End} Tests and {Data,Information,Knowledge,Wisdom} Objects"
date: 2025-07-02T12:55:42+02:00
draft: false
---

Data are elements. A datum is a unit, subject to unit tests. Data may be combined in formations, i.e. as information.

Information objects, i.e. data composites, can be treated as elemental units as well, subject to unit tests. Information objects are also readily subject to integration tests; they are integrations of data units.

Knowledge objects are sets of relations among addressable data/information objects, i.e. among fact-(package-)units. Consider these units as nodes of a graph. Consider the relations among these units, i.e. the (also addressable) finite set of conceptual relations in use by a knowledge object, as edges connecting nodes. And there you have it: a knowledge graph.

Knowledge objects can be treated as composite units as well, subject to integration tests. Treated as knowledge graphs, they are also readily subject to end-to-end (e2e) tests in which use cases are expressed as (a sequence of) graph journeys/queries/traversals.

Some end-to-end scenarios are not well-represented as a user presenting a structured query over known situational elements (data/information objects) and their known conceptual relations. Rather, the user presumes and seeks operation over informal associations among informally defined composites/situations and their informally defined (and informally salient) elements/aspects. Digital objects can represent this sought-after wisdom, often as learned vector embeddings trained over temporally-qualified data/information objects, i.e. events. Such wisdom objects are subject only to end-to-end tests, not to integration or unit tests.
