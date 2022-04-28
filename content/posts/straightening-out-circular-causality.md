---
title: "\"Straightening Out\" Circular Causality"
date: 2022-04-27T11:31:34-04:00
draft: false
tags:
- society-of-FAIR
---

We often seek to "straighten out" a maze-like, loop-containing situation. We try to find a "path" through "causal" explanations that go in only one direction. Why?

> There are countless different types of networks that contain loops. But all networks that contain no loops are basically the same: each has the form of a simple chain.

Any directed acyclic graph (DAG) can be linearized, i.e. topologically sorted. And we can apply the same types of reasoning to *everything* we can represent in terms of chains of causes and effects. We can proceed from start to end without any need for a novel thought.

But frequently, to construct such a path, we have to ignore important interactions and dependencies that run in other directions.

In loopy situations, one may find success in shifting from "causal" learning to "clausal" learning. If data values are annotated with dependencies, e.g. labeled with external provenance, with justifications for data-processing decisions, etc., then dependency-directed backtracking may help to path-find by avoiding sets of premises that support previously discovered contradictions.[^1]

In this way, annotating data with provenance metadata can formally help to "straighten things out".

[^1]: C. Hanson and G. J. Sussman, Software design for flexibility: how to avoid programming yourself into a corner. Cambridge: The MIT Press, 2021.

{{< subscribe >}}