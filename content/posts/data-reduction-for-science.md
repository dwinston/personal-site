---
title: "Data Reduction for Science"
date: 2021-04-16T09:36:47-04:00
draft: false
---

[Earlier this
week](https://donnywinston.com/posts/how-is-data-unification-different-than-data-fusion/), I wrote
that

> In sharing scientific research data, the goal is often to provide data reductions to the extent
possible without loss – the output is, in a strong sense, equivalent to the input. Any further
reduction that may be necessary to support decisions and policy can be done as fusion beyond
unification.

As luck would have it, the U.S. Department of Energy (DOE) posted a funding opportunity announcement
(FOA) yesterday on [Data Reduction for
Science](https://science.osti.gov/-/media/grants/pdf/foas/2021/SC_FOA_0002501.pdf):

> Scientific observations, experiments, and simulations are producing data at a rate beyond our
capacity to store, analyze, stream, and archive. This data almost always contains redundancies and
trivialities that hide the important information of interest to scientists. Of necessity, many
research groups have already begun reducing the size of their data sets...These efforts should be
expanded to include mathematical rigor to ensure that scientifically-relevant constraints on
quantities of interest are satisfied, to be integrated into scientific workflows, and to be
implemented in a manner that inspires trust that the desired information is preserved.

There have been efforts for decades to identify and deal with this issue, with cute acronyms for
relevant data like ROT (Redundant Obsolete and Trivial), WORN (Write Once Read Never), and WORSE
(Write Once Read Seldom if Ever). However, the DOE FOA highlights that it is not enough to
*separate* storage ("hot", "cold", etc. tiers) for research data -- we must seek to *avoid* storage
of ROT data.

{{< subscribe >}}