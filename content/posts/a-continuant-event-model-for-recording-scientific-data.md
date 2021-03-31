---
title: "A Continuant-Event Model for Recording Scientific Data"
date: 2021-03-26T14:56:43-04:00
draft: false
---

The RDF data model is quite flexible: Anybody can say Anything about Any topic (aka the "AAA slogan"). However, I
recommend -- and describe here -- a particular modeling strategy when it comes to entering new facts about research
activities into a data management system. Once entered this way, workflows may add additional derived facts to suit the
needs of downstream applications. This strategy has been called *entity-event modeling* [in the context of RDF
graphs](https://www.youtube.com/watch?v=2PbuPyeR5Aw), and is a specialization of the broader [event
sourcing](https://martinfowler.com/eaaDev/EventSourcing.html) pattern.

First, identify one or two "core continuants" for your domain, where a continuant is something that continues to exist
throughout some period of time, as distinguished from an "occurrent," which is anything that may be said to occur and
that is associated with one or more continuants. These core continuants should be suitable as principal subjects across
applications -- they are domain-specific, not application-specific.

For example, a microbiome data collaborative may posit a "study" activity as a core continuant, which is influenced by
events relating to generation of environmental bio-sample entities, communication with sequencing- and
annotation-workflow activities, and association with various human or software agents.

The W3C provenance ([PROV](https://www.w3.org/TR/2013/REC-prov-dm-20130430/)) data model, a vocabulary with a [mapping
to RDF](https://www.w3.org/TR/2013/REC-prov-o-20130430/), is a great fit for continuant-event modeling. At its core,
PROV describes the use and production of *entities* by *activities*, which may be influenced in various ways by *agents*
(such as people). Crucially, the distinction between activity and entity in PROV is similar to that between
['continuant' and 'occurrent', respectively, in logic](http://www.ditext.com/johnson/intro-3.html). A so-called
"prov:Activity" may be a subject of ongoing concern, i.e. a continuant: generating, using, and invalidating entities;
being triggered to start or end by entities; associating with agents (that in turn may have roles or plans, or may
delegate to other agents); and communicating with other activities via shared entities.

Depending on your domain, your "core continuant" may be any of prov:Activity, prov:Agent or even prov:Entity. Think
about the most important set of "continuing" subjects across many instantaneous occurrences, i.e. across many
observations of state. For a [multi-omics data collaborative](https://microbiomedata.org/), the core subject may be a
study (a prov:Activity). For a [collection of data on all known inorganic materials](https://materialsproject.org/), the
core subject may be a "material" (a prov:Entity with many specializations, i.e. alternate structures). For many service
businesses, the core subject may be a customer or patient (a prov:Agent).

{{< subscribe >}}
