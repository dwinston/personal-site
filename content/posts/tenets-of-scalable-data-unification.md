---
title: "Tenets of (Scalable) Data Unification"
date: 2021-04-09T11:18:45-04:00
draft: false
---

*Unification* is a process of combining partial-information structures. First used in computing for
theorem proving,[^1] it is used widely for *type inference* in programming-language compilers and
for logic-programming systems.

*Data unification* is described well in [this
whitepaper](https://www.dropbox.com/s/s75l3y17df1scja/Seven-Tenets-of-Scalable-Data-Unification-2019-01.pdf?dl=0)
by Stonebraker. It is concerned not just with ingest, cleaning, and transformation generally, but
also specifically with schema integration, deduplication (entity consolidation), and
classification.

One of the examples problems he gives is of unifying data from 10,000 electronic lab notebooks for
Novartis, a large drug company. This is an "enterprise company" problem, and he outlines seven
tenets of data unification for situations at this scale.

I think the tenets also apply to dealing with the scale of scientific research data. Because it's
often a tiny research group attempting unification rather than a large business unit, attention to
such tenets may be even more critical.

If you get a chance to read the whitepaper, let me know what you think.

[^1]: J.A. Robinson; "A Machine-Oriented Logic Based on the Resolution Principle," in Journal of the
ACM, 12(1) (January 1965): 23–41.

{{< subscribe >}}