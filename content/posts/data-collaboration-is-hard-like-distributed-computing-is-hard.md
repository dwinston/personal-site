---
title: "Data Collaboration Is Hard Like Distributed Computing Is Hard"
date: 2021-03-24T14:52:54-04:00
draft: false
---

It is hard to mediate among concrete representations, among data structures with differing schema. There are certainly
valiant efforts to [replicate shared data structures without conflict](https://www.inkandswitch.com/local-first.html)
and to facilitate [distributed schema evolution](https://www.inkandswitch.com/cambria.html), i.e. to sync "under the
hood" concerns.

Alan Kay's original vision of "object-oriented" design is analogous to the "cell-oriented" operation of a human being,
in that questions of concrete representation are postponed.

> "Every cell in our bodies is a descendant of a single zygote. All the cells have exactly the same genetic endowment
(about 1GByte of ROM!). However there are skin cells, neurons, muscle cells, etc. The cells organize themselves to be
discrete tissues, organs, and organ systems. This is possible because the way a cell differentiates and specializes
depends on its environment...context that selects particular behaviors from the possible behaviors that are available in
its genetic program."[^1]

In distributed computing systems with a [log-centric
architecture](https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying),
each individual service ("cell") has the same genetic endowment -- the shared log of events. Each service is a state
machine that can respond to the event log differently, and thus exhibit different behavior. At any time, a service can
be "re-built", perhaps using different logic, that re-plays the same event log to do its thing.

In a scientific data collaboration, each actor specializes in acting on and producing data in a particular way. If all
input and output is cast as a log of simply-structured events, as a shared and growing sequence of nucleotides (and with
a growing number of distinct "types" -- not just A, T, G, and C "events"!), then each actor can draw upon a shared
genetic endowment for its activities, even as those activities may change over time -- as actors differentiate.


[^1]: Sussman, "[Building Robust
Systems](http://groups.csail.mit.edu/mac/classes/symbolic/spring07/readings/robust-systems.pdf)" (2007). See also:
Hanson and Sussman, Software Design for Flexibility: How to Avoid Programming Yourself into a Corner. MIT Press, 2021.

{{< subscribe >}}