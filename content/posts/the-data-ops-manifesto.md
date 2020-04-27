---
title: "The Data Ops Manifesto"
date: 2020-04-22T08:41:54-04:00
draft: false
---

I came across
[The DataOps Manifesto](https://www.dataopsmanifesto.org/),[^1]
which states five values with regard to developing and delivering analytics. I was surprised that I disagreed with
 all five.
 
## "Individuals and interactions over processes and tools"

Processes and tools are the foundation of effective analytics, and I don't think that's what the authors
 meant by their use of the word "over". Yes, of course, individuals and interactions inform the design of such
  processes and tools, but the former are transient. People come and go. Interactions wax and wane.

This value hints at a certain charm around informality, but often an apparent lack of structure means only that the
structure is unknown [or perhaps denied](https://en.wikipedia.org/wiki/The_Tyranny_of_Structurelessness). Analytics
 need structure if they are to track how structure (schema) evolves.

## "Working analytics over comprehensive documentation"

Analytics need to work. However, ancillary support like documentation is the foundation for answering new questions
, questions not addressed
 by what's merely at work *right now*.
 
 Consider the division of database systems into online transaction processing (OLTP) and
  online analytical processing (OLAP). OLTP systems are the *working* systems, made to handle specific
  questions (requests, transactions) quickly. OLAP systems, though also tuned to handle specific
   aggregation-hungry questions, are there to answer new questions.
   
To emphasize a "working" system over support for infrequently-asked questions is to devalue the OLTP/OLAP
 distinction.

## "Customer collaboration over contract negotiation"

My disagreement with this relates to my take on the importance of processes and tools above. Collaboration how?
What does it look like?
Contracts materialize collaboration. In software development, they
 often take names like
 *interfaces*, *types*, *unit tests*, etc.

## "Experimentation, iteration, and feedback over extensive upfront design"

What is the thing with which you can experiment, iterate, and obtain feedback? An upfront design. At first I thought I
 would need to call out "extensive" as a strawman, but I realize it's actually great for me here.
 
 *Extent* is the area
 covered by something. An extensive design covers what you know there is to cover. What if you know very little about
  the problem area upfront? Well then, your extensive design shouldn't take very long, and it will grow in extent as
   you experiment, iterate, and get feedback. But materialize what you (claim to) know up front. 

## "Cross-functional ownership of operations over siloed responsibilities" 

Cross-functional use of resources is great, but I turn to the
[single-responsibility principle](https://en.wikipedia.org/wiki/Single-responsibility_principle)
when it comes to ownership, to responsibility. This dichotomy is analogous
 to the second part of the [SOLID](https://en.wikipedia.org/wiki/SOLID) acronym for software design
  principles, namely the [open-closed principle](https://en.wikipedia.org/wiki/Open%E2%80%93closed_principle), where
  an entity allows its behavior to be extended without allowing its modification.

[^1]: Since I discuss specific content,
[this snapshot](https://web.archive.org/web/20200415223843/https://www.dataopsmanifesto.org/) captures what I saw.