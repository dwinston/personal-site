---
title: "Conceptual Provenance"
date: 2021-03-08T14:31:25-04:00
draft: false
---

We often think of provenance as a physical thing, tracking the history of a sample and of what we measured. But the
provenance of a result started when someone had the idea or the request to measure it. The metadata for a result is not
just the parameters on the instrument, or how much sample, or which sample -- it's all those other steps upstream.

Conceptual metadata are like tags, meaningful handles. In a research environment, they allow you to find things based on
a concept as opposed to e.g. having to know that it was Jim that ran this on Thursday and Jim always puts his results in
this folder. In the absence of conceptual metadata, the best search algorithm you have is often your personal network --
having to know who typically runs this kind of thing and then asking them where it's stored. In a research environment
where (a) there's a fair bit of turnover (students graduating, postdocs moving on), and (b) we have a lot of stuff done
outside our team, e.g. through transient collaborations, that personal-network algorithm gets harder and harder to rely
on. So it results in the repetition of experiments.

When conceptual context -- describing planned experiments, methodologies, sample prep, execution of measurement,
calculated/reduced results -- lives in separate systems, you have orphaned context and meaning separate from the
ultimate results. So, in order to bring information together in a report/presentation, or to fully describe and record
the findings for something like a publication or filing, somebody has to read from one system and type or copy/paste
stuff into another. There are compounding opportunities for human error, dropping units, putting things in the wrong
blank, typing strings that are non-standard, etc. This makes for a very fragile and tenuous handle on the conceptual
provenance of a measurement/result.

At any given point in a research workflow, we know a lot about our stuff. Somebody in our electronic universe knows what
we need to know -- perhaps we just haven't enabled an electronic flow of that context to capture with the data. This is
useful not just for integration for indexes and search downstream, but it also ensures that context, no matter who comes
and goes from the team, is more or less permanently embedded with the data.

(I borrowed *heavily* from [this fantastic podcast episode](https://www.bioradiations.com/data-standardization/) --
check it out.)

{{< subscribe >}}