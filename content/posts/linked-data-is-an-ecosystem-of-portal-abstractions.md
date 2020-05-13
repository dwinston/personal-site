---
title: "Linked Data is an Ecosystem of Portal Abstractions"
date: 2020-05-13T15:41:38-04:00
draft: false
---

In an episode of the CoRecursive podcast[^corecep50], Sam Ritchie uses the phrase
"portal abstraction" to describe how the use of a particular term can open
a portal -- a gateway -- to a world of relevant prior art.

He discusses issues in analytics. One issue is distributing
summative calculations over data both as batches and in real-time, specialized
for "big" and "fast" data, respectively. A second, compounding issue is dealing
with data that may be missing.
The term that helped Sam deal with the first issue is the *semigroup*
from abstract algebra.
The term that helped him deal with the second issue is the *monoid*.

Suppose Sam had stuck with a bespoke term like "Addable" to define a code interface
to objects that could be added together associatively by calling a required "add"
method of the objects, and that perhaps knew about a special "identity" value 0
that could represent missing data without affecting the outcome of a sum.
The term "Addable" isn't specialized enough to yield a treasure trove of related
terms and relevant prior art that would unambiguously apply to the use and
extension of Sam's bespoke interface.

Transitioning to less ambiguous terms like *semigroup* and *monoid* led Sam to
read research papers of certain relevance and to discovering useful ideas for his
work, ideas like probabilistic data structures and the hyperloglog algorithm.

In natural language, terms are often overloaded -- words have many meanings. The 
vocabulary of abstract algebra has many terms that have no significant competing
meanings among English speakers, and so they indeed are fertile candidates for
portal abstraction. More generally, though, disambiguation among word and phrase
meanings would be needed for similar power.

Linked data use unambiguous URIs to denote terms. Collections of such terms
and their relations, also constructed and machine-readable as linked data,
constitute the variety of ontologies offered by domain specialists. Linked data
is an ecosystem of portal abstractions.

[^corecep50]: <https://corecursive.com/050-sam-ritchie-portal-abstractions/>