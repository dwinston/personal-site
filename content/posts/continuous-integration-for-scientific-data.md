---
title: "Continuous Integration for Scientific Data"
date: 2021-03-12T14:39:37-04:00
draft: false
---

How do you check potential changes to your published data?

You might set a rhythm for releases, say monthly or quarterly. You generate a new release candidate, run a set of
checks, and then release. You reproduce the whole thing rather than add to it, and you do your checks at the end.

You might do incremental rather than batch processing. You apply changes to your last release, run checks, and then
release. You either (a) apply changes to a full copy of the last release, or (b) you have version control and can apply
changes to a new branch of the data without maintaining a separate copy and without disrupting references to the
release.

When applying potential changes, you might also apply them in sequence as a pipeline with checks at each stage, rather
than / in addition to checks at the very end.

Your pipelining may use entirely bespoke software, or it may use software with maintenance shared across a community,
such as [FireWorks](https://materialsproject.github.io/fireworks/), [Airflow](https://airflow.apache.org/), or
[Dagster](https://dagster.io/). Similarly, your data checking may use entirely bespoke software, or it may use shared
software such as [Great Expectations](https://greatexpectations.io/) or built-in facilities of pipelining software (e.g.
enforced typing on step inputs and outputs in Dagster).

How do you stage and check potential changes to your published data? I'm curious about what you've done / seen done /
are doing in practice, and if your current practice feels sufficient.

{{< subscribe >}}