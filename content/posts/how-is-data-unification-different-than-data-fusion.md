---
title: "How Is Data Unification Different Than Data Fusion?"
date: 2021-04-12T12:38:43-04:00
draft: false
---

In response to [this note](https://donnywinston.com/posts/tenets-of-scalable-data-unification/), a
reader asked

> How is data unification different than data fusion?

I re-read the Stonebraker whitepaper I had linked to in that note, and what it describes does *not*
seem meaningfully different than [data fusion](https://en.wikipedia.org/wiki/Data_fusion).

I propose that data unification is more conservative than data fusion -- it stops short of the lossy
reduction often required for decision-support systems.

From the Wikidpedia article on data fusion linked above:

> ... data integration is used to describe the combining of data, whereas data fusion is integration
followed by reduction or replacement.

In particular, Stonebraker's 6th Tenet expresses the need for irreversible reduction (fusion) with
acceptable confidence via machine learning:

> A rule system implementation will not scale. Only machine learning systems can scale to the level
required by large enterprises.

Decisions are often made using methods other than logical reasoning, i.e. "going with your gut".
Machine learning allows decision-makers to model gut-like reasoning quantitatively over large data
sets when expert-supplied domain logic is insufficient to reduce the data without loss.

The example given in the whitepaper is that 500 rules were able to classify only 2M records out of
20M, so machine learning was used to make educated guesses about the remaining records.

In unification, no guessing is permissible. Rather, additional user input is solicited. For example,
with type inference, a compiler does not "train" on the types you explicitly annotate, plus the ones
it can infer with 100% confidence, in order to assign guesses to what remains. Rather, though it may
guess, it requires user input to confirm guessed types. Until the type checker is 100% confident,
the unification process is unsuccessful.

Thus, I view Stonebraker's contention that a rule system implementation will not scale as saying
that, if a data application requires classification of all records, even in the absence of logical
certainty based on supplied domain rules, then data unification is insufficient, and data fusion is
required -- 100% logical certainty is sacrificed, but decisions must be made today, and the best one
can do is track provenance and report some quantification of the confidence.

In sharing scientific research data, the goal is often to provide data reductions to the extent
possible without loss -- the output is, in a strong sense, equivalent to the input. Any further
reduction that may be necessary to support decisions and policy can be done as fusion beyond
unification.

{{< subscribe >}}