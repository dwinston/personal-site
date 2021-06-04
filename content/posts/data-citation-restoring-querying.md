---
title: "Data Citation: Restoring ↔ Querying"
date: 2021-05-21T10:46:51-04:00
draft: false
---

Approaches to data citation may span classes of big-O complexity, for both space (memory/storage)
and time (compute/transfer).

Dataset revisions may be minted and persisted without any delta encoding / structural sharing. The
main mechanism of reproduction for citations in this case is restoration. Space complexity is high,
as storage needs are high. Cost of storage can be reduced via tiered storage / compression, yielding
increases in time complexity for restoration.

Opposite to restore-centered revision control is query-centered revision control for which space
complexity is not proportional to the number of minted revisions, but rather is proportional to the
total amount of information recorded across time. Rather than via copy-on-write, [persistent data
structures](https://en.wikipedia.org/wiki/Persistent_data_structure) are achieved via delta encoding
/ structural sharing, akin to git's approach to revision control for codebases.

With query-centered revision control, the main mechanism of reproduction for citations is querying.
Space and time complexities can be balanced here in different ways. For example, one can maintain
multiple covering indexes that result in lower time complexity -- faster queries -- at the cost of
higher space complexity for the functional degeneracy.

There can also be interplay between restoring and querying. There may be structural sharing among
dataset revisions, but a particular revision may need to be "restored" for it to then be queried.
Alternatively, a "change log" may be queried directly, with an overlay filter that restricts results
to be consistent with a target version of the dataset.

{{< subscribe >}}