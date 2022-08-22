---
title: "Identifying Identifying"
date: 2022-08-22T19:27:28-04:00
draft: false
---

Day 1 of my [five-week experiment to elaborate on FAIR-enabling
services](https://donnywinston.com/posts/a-five-week-experiment-to-elaborate-on-fair-enabling-services/),
and I already find myself fallen flat on my face.

I had wanted to go through motions of brainstorming concepts related to the service of identifying,
partition them into concepts, attributes, and relationships in the sense of Sequeda and
Lassila's[^1] "Knowledge Report" intermediate representation -- for each, draft a table to name it,
provide an alternative name or two, a definition, an identifier for the thing, an identifier
template for instances of the things culled from sources, and a query to get instance from sources
-- or at least a nod to how one might proceed with these, particularly for the last two items.

I instead found myself in Philadelphia for longer than anticipated, for reasons I may or may not
divulge over a beer, and so here's what I came up with in the limited timebox I gave myself to push
*something* out today:

{{< figure src="/img/fes-identifying-concepts.png"
    title="Identifying some concepts (attributes? relationships?) about identifying"
    width="100%" >}}

An identifying service provided guarantees wrt protocol, policy, and algorthims to make good on the
guarantees. These guarantees revolve around the nature of requests and responses. Requests wrt
identifying are about minting new IDs, binding information to minted IDs, or resolving supplied IDs
to bound information. Responses are either the thing identified, information about the thing, or
where to get the thing.

Okay, timebox is over. Yes, leaves in the diagram above have gone unexplained. Thankfully, there are
more days for thinking, i.e. writing.

{{< subscribe >}}

[^1]: J. Sequeda and O. Lassila, Designing and building enterprise knowledge graphs. San Rafael:
Morgan & Claypool Publishers, 2021.
