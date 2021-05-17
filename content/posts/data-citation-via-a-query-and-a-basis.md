---
title: "Data Citation via a Query and a Basis"
date: 2021-05-12T14:41:38-04:00
draft: false
---

Against what bases are queries against your data evaluated? If you only expose a single "data base"
that changes over time, then data citations cannot be a combination of query and basis.

When citing a passage in a book, the edition/variation of its publication, i.e. the thing that is
assigned an ISBN, is the basis. Optionally, a citation may include a "query" against this basis -- a
page number, page range, chapter number/title, etc. Yes, part of the passage may be copied inline as
a quotation, but a reader can use the provided query and basis to evaluate a cited passage in
context.

One way to support granular data citations is to allow people to share both their queries against
your data and the bases against which those queries were evaluated. These (query, basis) pairs can
be assigned IDs so that citations can be shared compactly. This allows people citing your data to
avoid the equivalent of quoting tens of pages of a book inline to ensure their readers can examine
that text.

But how are multiple bases maintained, single bases restored for queries, and queries executed, all
with reasonable space and time complexity? There are a variety of approaches, each with their
tradeoffs.

Have you undertaken such an endeavor, dear reader? Let me know about your experience.
In a follow-up note, I'll go over some approaches I've encountered.

{{< subscribe >}}