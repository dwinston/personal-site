---
title: "Event Sourcing With Eliot"
date: 2020-10-19T09:49:35-04:00
draft: false
---

[Eliot](https://eliot.readthedocs.io/en/stable/index.html) is a Python logging system that outputs a
stream of JSON objects detailing causal chains of actions. Scientific computing is identified
in [its documentation](https://eliot.readthedocs.io/en/stable/scientific-computing.html) as an ideal use case for
this style of logging, in part because feedback cycles can be slow for such long-running processes
where interactive step-debugging is inconvenient.

It seems that such logs would also be appropriate for event sourcing. Data derived from the logs could power
dashboards for scheduling and monitoring workflow pipelines, as well as viewing processed workflow outputs,
with eventual consistency that is good enough given the timescales involved in these long-running processes.