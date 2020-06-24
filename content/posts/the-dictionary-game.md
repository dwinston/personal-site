---
title: "The Dictionary Game"
date: 2020-06-24T09:57:12-04:00
draft: false
---

Word games are a technique for troubleshooting problem statements. They are usually cheaper than unwanted solutions.
They expose ways that well-intentioned problem solvers trip over a misunderstood word, a misplaced comma, or
ambiguous syntax.[^lights]

In the dictionary game, you make a list of a dictionary's meanings for each word in the original sentence. Then, you
try to apply each of those meanings in turn. Consider a little word like *had*. It's defined as the past tense and past
participle of *have*, which in turn has tens of definitions. Consider the phrase, "Mary had a little lamb." The
dictionary game asks you to consider options for *had* (via *have*) such as:
- To be in possession of, as one's property; own.
- To be related or in a particular relationship to: ***have three children***.
- To hold in one's mind; entertain: ***have doubts***.
- To bribe or buy off.
- To win a victory over; to down.
- To cheat, deceive, or trick.
- To accept or take: ***I'll have the gray jacket***.
- To partake of; consume, as by eating or drinking.

Consider playing the dictionary game with problem statements involving your data: statements and queries
involving names of tables/collections, columns/fields, etc.

The Resource Description Framework (RDF) approach to data modeling leans into the dictionary game. A resource never
has a string literal like "title" as a property. Rather, it has a
[v:title](https://www.w3.org/Submission/vcard-rdf/#vcard:title) (job title of an employee), a
[dc:title](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#http://purl.org/dc/terms/title
) (title of a creative work)
, or some
other resource with an unambiguous URI that happens to have a [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label)
of "title".

[^lights]: Gause and Weinberg, *Are Your Lights On?*, pp73-80. Dorset House, 1990.  