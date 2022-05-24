---
title: "The Persistence of Identity"
date: 2022-05-24T14:07:33-04:00
draft: false
tags:
- society-of-FAIR
---

What is that strange possession that stays the same throughout its life?[^som]

Can we recollect how things appeared to us before we learned to link new meanings to those things?

What is this body of changelessness in spite of change?

Perhaps the purview of a thing's persistence is its predictable pathways of provenance:[^prov-o]

* the typical effects of its typical activities,[^prov-act]
* its body of influenc(ed/ing) entities[^prov-ent] whose meanings change only slowly, and
* whichever of its agents[^prov-age] change the least as its life proceeds.

Data does not have intrinsic meaning:

> The semantics of our data are defined by the effects it produces when passed into our functions. These effects should be predictable whenever possible, but data cannot prevent itself from being interpreted in surprising ways.[^eoc]

An identifier is an association between a string of data and an object.[^ark]. The semantics of our identifiers are then defined by the effects produced by interpreters that believe records bearing witness to these associations.

A layer of indirection separates *what* something does from *how* it does it. Similarly, an identifier separates *what* something *is* from *how* it is.

What are some tools for predictability in indirection?

* *referential transparency*: The semantics of purely functional code will remain the same if we replace every expression with its result, e.g. "1 + 1" with "2" (for typical senses of "1", "+", and "2"!).
* *invariant relations*: The semantics of a data structure's interface -- its abstract representation, its exposed behavior -- will remain the same if we decide to change its concrete representation -- its internal model -- as long as we enforce appropriate invariant relations on that concrete representation.[^hoare]

Effects are the currency of meaning, yet their causes and conditions are ever fleeting:

> ...everything in the world is the result of a vast concurrence of causes and conditions, and everything disappears as these causes and conditions change and pass away.
> 
> -- Buddha[^buddha]

"All models are wrong, but some are useful." An identity is ultimately a model, an abstract description that hides certain details while illuminating others, that can yield useful predictions when it provides adequate explanations relating primitive phenomena to one another and to more complex phenomena. Go forth and identify.

[^som]: M. Minsky, *The Society of Mind*. New York: Simon and Schuster, 1986, p. 54.
[^prov-o]: https://www.w3.org/TR/prov-o/
[^prov-act]: https://www.w3.org/TR/prov-o/#Activity
[^prov-ent]: https://www.w3.org/TR/prov-o/#Entity
[^prov-age]: https://www.w3.org/TR/prov-o/#Agent
[^eoc]: Z. Tellman, Elements of Clojure. Monee, IL: Lulu.com, 2019.
[^ark]: J. A. Kunze, “The ARK Identifier Scheme (v.34).” Internet Engineering Task Force (IETF), Jan. 2022. [Online]. Available: https://datatracker.ietf.org/doc/draft-kunze-ark/
[^hoare]: C. A. R. Hoare, “Proof of correctness of data representations,” Acta Informatica, vol. 1, no. 4, pp. 271–281, 1972, doi: 10.1007/BF00289507.
[^buddha]: B. D. Kyōkai, The teachings of Buddha, 1. ed. New Delhi: Sterling Publishers, 2004.

{{< subscribe >}}