---
title: "K-Lines via RDF and PROV"
date: 2021-02-09T08:17:25-05:00
draft: false
---

A "knowledge line", aka "K-line", is a representation of knowledge that connects what we know with how it's used -- we
keep each thing we learn close to the agents that learn it in the first place.[^minsky] When a K-line is re-activated,
the agents attached to it are re-activated, putting a system in a "mental state" similar to when this thing we know was
last generated, used, and/or persisted.

A K-line "memorizes" the entities we're working with in part by making a list of the agents involved in our activities.
"Re-membering" is in part a recollection of agents -- getting the band back together -- to restore a working context.

K-lines may be facilitated by Linked Data standards. The PROV ontology focuses on `prov:Entity`, `prov:Agent`, and
`prov:Activity` classes and how these first-class concepts relate to one another. The RDF data model facilitates the
wire-like structure of K-lines as a graph, and PROV provides the controlled vocabulary and schema.

[^minsky]: Minsky, Marvin. *The Society of Mind*. Simon and Shuster, 1986.
