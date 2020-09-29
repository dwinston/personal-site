---
title: "Headless Materials Research Management Systems"
date: 2020-09-29T16:26:43-04:00
draft: false
---

A headless content management system (CMS) is one that is API-first, decoupled from any particular
presentation layer on the front-end. Such a service can support multiple channels for
working with and presenting content, given the type of user and their context.
[Strapi](https://strapi.io) is one example of an open-source headless CMS.

Consider a so-called materials research management system (MRMS).
I am specializing this to materials science, rather than say a generalized "scientific research"
management system. Furthermore, I am specializing this to research: not procurement, not product
development, not manufacturing, not distribution, not sales.

However, I am also not drilling further
in to, say, "research data". I am including all activities that pertain to research, which may include
reference to, for example, procurement activity. Other concerns of research activity
include domain knowledge/ontologies, hypotheses, experiments, analyses, reports, and presentations.
Finally, I reuse the "management system" part from prior art like content management systems (CMSes) and
relational database management systems (RDBMSes) that provide useful interfaces for governance.

So, what are some examples of such systems? Citrine Informatics advertises an online
[platform](https://citrine.io/product/what-is-the-citrine-platform/) that uses an open-source [data
model](https://citrineinformatics.github.io/gemd-docs/)
they developed called Graphical Expression of Materials Data (GEMD). The GEMD model distinguishes materials,
processes, and measurements, and distinguishes between intent (specification) and realization
(e.g. actual conditions observed for a run of an experiment). For example, a process of procurement can
be said to produce a material, another process can prepare a sample of a material as an ingredient for
a measurement run, etc. It is clear that the Citrine platform is intended as a system for
materials research management.

Another example of a MRMS is the Materials Project's contributions framework,
[MPContribs](https://mpcontribs.org/). At this time, MPContribs does not provide many
affordances for explicit modeling of research assets and activities -- unlike GEMD, the semantics
of submissions are mostly implicit and open-ended. The emphasis of MPContribs is empowering users to
submit generic reports and custom presentations of processed research results in a way that links
them to existing Materials Project materials. MPContribs is a great example of a headless MRMS, as it
serves both customized landing pages for each submitted project as well as inset "cards" on pre-existing
material detail pages.

Finally, I'd like to point out Toyota Research Institute's
computational autonomy for materials discovery (CAMD) system, an [open-source](https://github.com/tri-amdd/camd)
framework that explicitly models and manages research concerns like hypotheses, experiments, and analyses.
One designs sequential learning campaigns to deploy software agents that evaluate
candidate materials in some search space, given relevant seed data, and that iteratively dispatch hypotheses to an
experimental facility (whether a physical laboratory or e.g. a density functional theory (DFT) program). CAMD
is also a type of headless MRMS that tracks hypotheses and experiments as well as provenance regarding
decision processes.

One reason I'm particularly interested in *headless* materials research management systems is that research activities
are distributed, not centralized. Systems that accommodate a variety of contributions from a variety
of stakeholders, particularly across not only space but time (employees move on, graduate students graduate, ...),
can flourish. The World Wide Web (WWW) does this for documents -- HTTP is headless, and web browsers render a variety
of markup for a variety of folks. I'm excited about what we can do for data and metadata with HTTP, i.e. the
Semantic Web.