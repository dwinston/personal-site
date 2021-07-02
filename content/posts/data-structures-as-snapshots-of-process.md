---
title: "Data Structures as Snapshots of Process"
date: 2021-06-24T15:01:53-04:00
draft: false
---

Imagine a data system modeled as three parts: an interface, a processor, and a repository. The
repository "contains" information. The processor receives symbol streams to alter or retrieve
information from the repository, and the processor outputs symbol streams. The interface is the
medium, the opaque surface, of symbol-stream exchange between you and the processor.[^kent]

What information is "in" the repository? If data depends on a continuous variable, like time, the
actual things stored may be "breakpoints", so that extracting data is a combination of
lookup-plus-compute. You may get a value for temperature at the precise time of an observation, but
the value is not stored – it is interpolated.

What is the difference between fetching a stored data structure and dynamically generating a record
with the same characteristics? The distinction between repository and processor is not so clear.
Data structures are snapshots of process; a repository is, in a way, a cache.

Just like it is more expensive to rework a product on an assembly line at the end as opposed to at
the beginning, it is more expensive to adapt a data product for a second application the more it has
been structured for a first application.

In scientific research, published data products are often structured for "manuscript applications,"
so repurposing the data requires reverse engineering PDF-embedded figures/tables or
spreadsheet/notebook-embedded formulae, annotations, and charts.

Data structures that embody snapshots of processing are valuable – they reduce latency for
predictable data requests for known applications. To maximize FAIR[^fair] characteristics of your
data, though, look upstream.

[^kent]: W. Kent, _Data and reality_, 2nd ed. Bloomington, Ind: 1stBooks Library, 2000.

[^fair]: M. D. Wilkinson _et al._, “The FAIR Guiding Principles for scientific data management and
stewardship,” _Sci Data_, vol. 3, no. 1, p. 160018, Mar. 2016, doi:
[10/bdd4](https://doi.org/10/bdd4).

{{< subscribe >}}