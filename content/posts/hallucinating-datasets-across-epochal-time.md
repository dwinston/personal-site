---
title: "Hallucinating Datasets Across Epochal Time"
date: 2022-06-09T10:46:13-04:00
draft: false
---

"Dataset" is a derived notion, a psychological construct, where "versions" of the dataset are a succession of values that we perceive to be causally related. "Dataset" is a side effect.

Consider Rich Hickey's epochal time model, which I have [written about previously](https://donnywinston.com/posts/the-materials-paradigm-and-epochal-time/):

<img
src="https://donnywinston.com/img/hickey_are-we-there-yet_epochal-time-model.jpg"
alt="Epochal time model, from Rich Hickey's 'Are We There Yet' talk"
title="Epochal time model, from Rich Hickey's 'Are We There Yet' talk"
width="70%">

Identity is a derived notion, a collecting of values and calling each value a “state”. A state is just a labeling of a value for an identity at a point in "time". The succession of states is the identity. Identity is a side effect of choosing a timeline of value succession.

Consider drawing a dotted line on the figure above that encompasses all of the immutable values (boxes) and all of the ovals (pure functions). This may be considered the [functional](https://donnywinston.com/elements_of_clojure/#functional) [phase](https://donnywinston.com/elements_of_clojure/#phase) of a [process](https://donnywinston.com/elements_of_clojure/#process), where data is [transformed](https://donnywinston.com/elements_of_clojure/#transform) ([accreted](https://donnywinston.com/elements_of_clojure/#accrete), [reduced](https://donnywinston.com/elements_of_clojure/#reduce), or [reshaped](https://donnywinston.com/elements_of_clojure/#reshape)), separate from the [operational](https://donnywinston.com/elements_of_clojure/#operational) (i.e., [pull](https://donnywinston.com/elements_of_clojure/#pull) or [push](https://donnywinston.com/elements_of_clojure/#push)) phases of that process.

With this perspective, a process's functional phase also suggests labeling its succession of values. Each value may be called “data”. That is, a value becomes data when it is an input or output for a process. Depending on where the value is in the topology of the process, it may be considered “raw data” or “derived data” with respect to that process.

What, then, may we call the succession of data values for the timeline of a process -- what is the "identity" here, where successive values are "states"? In the [OpenLineage specification](https://github.com/OpenLineage/OpenLineage/blob/3808d4ab7dc0229c0f7997eda49fc00ab3947f26/spec/OpenLineage.md#openlineage-spec), the name for this identity is "dataset". In the [Marquez reference implementation](https://github.com/MarquezProject/marquez/blob/c53f66c0a3f748742eea69db5f3c287c63c929a9/docs/index.md#data-model) of OpenLineage, a "dataset version" is a read-only, immutable version of a dataset, i.e. an immutable value in the sense of the epochal time model.

Thus, "dataset versions" are the states, and "datasets" the identities, for the succession of values associated with the functional phase of a process.  To the extent that an immutable digital object -- a value -- is useful in the functional phase of one or more processes, it is useful to identify it as a "dataset version". To the extent that a succession of such values, which we perceive to be causally related via a process, is useful in whole or in part to various timelines of various processes, it is useful to identify this succession as a "dataset".

{{< subscribe >}}