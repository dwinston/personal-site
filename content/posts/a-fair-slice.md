---
title: "A FAIR Slice"
date: 2020-08-20T11:50:42-04:00
draft: false
---

I like Cynthia Arnold's approach to the problem of data discovery for a materials R&D organization.
In a podcast episode for Citrine, she says[^arnold]:
> companies don’t really need to boil the proverbial ocean to make progress in better using the historical data
> and the existing data. Doing a data inventory I think is a very good starting point, understanding what you have.

An inventory, understanding what you have, is all about *finding*. Nothing is accessible yet, just identifiable.

She goes on:
> Then identify which data will provide the most value, and how it will be used once you can organize it and make it
> accessible. And this becomes the basis of a data strategy and a data roadmap within the organization.

This is backtracking a FAIR[^fair] pipeline. Envision some data's end value,
which depends on its successful use (reusable), which depends on its organization for purpose (interoperable),
which depends on it being accessed (accessible).

The focus here is on pursuing a vertical slice of "AIR". The "F" in this FAIR strategy, a data inventory, is wide.
You can think of the outcome of data inventory
as a store of metadata, a virtual data lake, that points to data in existing stores but does not move the data. As
Mark Watson says[^hylangkg]:
> It is common to build a large data lake and then have staff not be able to find data.
> Don’t try to do everything at once.

Back to Arnold:
> Start with where you have problems and opportunities, and ask what data can support being better to deliver
> on these solutions and these opportunities. When the rubber hits the road, you can put together a focused team
> of a few content experts and some systems people. They can work together to help clean up and organize and put
> the identified datasets to use on real opportunities rather quickly.

The work of a few -- not many -- content experts and systems people will result in accessed data being made
interoperable with the requirements of the present opportunity. Avoid having too many stakeholders on early prototypes.
Conceptual integrity is key.

Arnold finishes up:
> And then, I think if you’re systematic about this and proceed down the line with fulfilling your data strategy
> really directed at real opportunities and problem solutions, I think you’re going to find you’re going to build
> your way into a good data taxonomy and framework that will be highly reusable and valuable.

In other words, as vertical slices of "AIR" accumulate around the nexus of your wide-"F" data inventory, latent
opportunities for connectivity will surface, unifying your graph of accessible, interoperable, and reusable data.
Embrace eventual connectivity. 

[^arnold]: ["The Business Case for Materials Informatics"](https://citrine.io/episode-010-dr-cynthia-arnold-the-business-case-for-materials-informatics/), DataLab # 10 (2019).
[^fair]: Wilkinson, M., Dumontier, M., Aalbersberg, I. et al. *The FAIR Guiding Principles for scientific data management and stewardship*. Sci Data 3, 160018 (2016). https://doi.org/10.1038/sdata.2016.18
[^hylangkg]: Mark Watson, ["Recommended Industrial Use of Knowledge Graphs"](https://leanpub.com/hy-lisp-python/read#leanpub-auto-recommended-industrial-use-of-knowledge-graphs),
in *A Lisp Programmer Living in Python-Land: The Hy Programming Language* (2020).