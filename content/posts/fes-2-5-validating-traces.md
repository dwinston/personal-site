---
title: "Validating Traces — Syntactically, Semantically, and Situationally"
date: 2022-09-04T13:28:00+02:00
draft: false
---

How do you validate a reified trace of digital-object provenance?

Is it even possible? This is syntactic validation. Values that should be strings are strings, dates
are dates, lists are lists, you know the drill...

Is it plausible? This is semantic validation. This date should be earlier (i.e., "less than" in
ISO8601 format) than that date, this number should be an integer multiple of that number, this
field's values are unique across the collection, this field is a reference to an object of that
type, etc. Also known as structural validation.

Is it probable? This is situational valuation, i.e. a matter of
[pragmatics](https://donnywinston.com/posts/validation-syntax-semantics-pragmatics/). This mode of
"validation" logs not _errors_ per se, but rather _warnings_. This is the world of statistical
process control, of setting thresholds for anomaly detection and tuning your go-ahead logic to align
with risk tolerance and chosen strategies for mitigation of failures.
