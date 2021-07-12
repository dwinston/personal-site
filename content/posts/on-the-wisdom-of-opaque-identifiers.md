---
title: "On the Wisdom of Opaque Identifiers"
date: 2021-07-12T11:11:23-04:00
draft: false
---

[Wikidata](https://www.wikidata.org) uses opaque identifiers for its catalogued information
resources. For example, the statement "[wd:Q42](https://www.wikidata.org/wiki/Q42)
[wdt:P69](https://www.wikidata.org/wiki/Property:P69)
[wd:Q691283](https://www.wikidata.org/wiki/Q691283)" may map to the label sequence "'Douglas Adams'
'educated at' 'St John's College'" with a language-locale preference of English-US.

Opaque naming is wise for internationalization. However, in local, specialized contexts, e.g. the
JSON-LD context for a particular dataset, there is value in human-readable suffixes so that e.g.

```json
{
 "@context": {
   "d": "http://example.org/data/",
   "p": "http://examples.org/properties/"
 },
 "@id": "d:DouglasAdams",
 "p:educatedAt": "d:StJohnsCollege"
}
```

would be a valid JSON API response that is both human- and machine-actionable.

So, let's continue to pursue "global" semantic names, right? This should be fine for scientific
research, where we've more or less settled on use of the English language, no?

After reading Levary et al. (2012),[^levary] I think that the pursuit of "global" semantic names for
things is futile, *particularly* in the context of scientific research.

Words/phrases (aka "signs") are often polysemous – they accumulate senses. For example, I inherited
the infuration of my PhD advisor over use of the the term "resolution" in lithography/metrology to
mean "minimum discernable feature dimension", e.g. linewidth, versus what I consider to be the
preferred sense of the term: "minimum discernable inter-feature separation", e.g. line spacing.

When encountering terms of art in scientific and technical literature, an author can mean several
things by it, even within a specialized discipline or sub-discipline. In fact, I think that use of
polysemous terminology is to be expected in the research literature, as pursuit of new knowledge is
a primary goal. For new knowledge to be accepted among practitioners, it must be ac*knowledge*d, and
this may take the form of attempting a change or narrowing of the typical sense of of a term within
the practitioners' context. This attempt may be acknowledged by the community, and thus *become*
(part of the pool of) knowledge it stewards, or it may be rejected.

Senses also accumulate signs. A concept (sense) may be expressed via a set of synonym words/phrases,
aka a *synset*. Above, I tried to express a concept with the synset "{resolution, minimum
discernable inter-feature separation, line spacing, ...}". The longstanding practice of [authority
control](https://en.wikipedia.org/wiki/Authority_control) in library science, e.g. authority files
and subject headings, acknowledges this accumulation, but nevertheless often persues a single,
canonical display of each name, a canonical sign for each sense.

My takeaway from Levary et al. (2012)[^levary] is that the appearance of a new concept in a
dictionary often corresponds to the appearance of a word A "that was not definable at earlier
times", i.e. a word that required another new word B to define it, which in turn – being a new word
itself – requires another new word C to define it, perhaps simply the former new word A, i.e. C is
A.

In other words, new concepts are loops. It is not reasonable to assume that a concept corresponds to
a single "node" in a word graph, a synset, and to choose a canonical sign from among candidate
synonyms. Rather, a concept often comprises two or more (but not many more; loops with length > 5
tend to represent semantic misinterpretations) nodes.

This makes it even more difficult to stick a canonical semantic sign on a concept. Thus, I
appreciate the wisdom of opaque identifiers, which can be mapped for particular (json-ld) contexts
to identifiers with human-readable suffixes, with e.g.
`owl:equivalentProperty`/`owl:equivalentClass`/`owl:sameAs` assertions, so that local
human-actionable vocabularies can nonetheless be unambiguously unified.

[^levary]: D. Levary, J.-P. Eckmann, E. Moses, and T. Tlusty, “Loops and Self-Reference in the
Construction of Dictionaries,” _Phys. Rev. X_, vol. 2, no. 3, p. 031018, Sep. 2012, doi:
[10/gffcxd](https://doi.org/10/gffcxd).

{{< subscribe >}}