---
title: "A Perlisism for Identifiers: Delay Binding"
date: 2022-08-08T22:42:20-04:00
draft: false
---

Inference based on semantic retrieval is more robust than inference based on syntactic parsing.

> identifiers should be as dumb as possible -- in other words, should include as little metadata as
possible about the thing being identified, leaving all information to be retrieved from metadata
repositories rather than inferred from the identifier itself. People always want to infer meaning,
and will often try to teach machines to do the same. The problem is that apparent meaning in the
structure of an identifier is all too often misleading...[^bide]

In order to be authoritative, identifiers should be assigned as early as practicable in the creation
process, but minting is not binding.

> Functions delay binding; data structures induce binding. Moral: Structure data late in the
programming process.[^perlis]

Identifier resolution delays binding; identifier structures induce binding. Moral: Structure
identifiers late (or never) in the minting process.

Also, structure identifier resolution (i.e. retrieved-metadata structure) late. Metadata is about claims;
there may be many and different claims about the same thing. "Multiple resolution", i.e. making
different metadata sources/profiles/formats accessible depending on what a client is trying to
retrieve, is akin to functional polymorphism and hence even later binding.

[^perlis]: A. J. Perlis, "Special Feature: Epigrams on programming," SIGPLAN Not., vol. 17, no. 9,
pp. 7–13, Sep. 1982, doi: 10.1145/947955.1083808. Online at
<http://www.cs.yale.edu/homes/perlis-alan/quotes.html>.

[^bide]: M. Bide, "Standard Identifiers: an overview of the current landscape," presented at the
USPTO Open Meeting: Facilitating the Development of the Online Licensing Environment for Copyrighted
Works, Apr. 01, 2015. [Online]. Available:
[pdf](http://www.linkedcontentcoalition.org/phocadownload/150401%20BIDE%20Standard%20Identifiers%20Overview%20with%20embedded%20slides.pdf)

