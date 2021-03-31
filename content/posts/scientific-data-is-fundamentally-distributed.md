---
title: "Scientific Data Is Fundamentally Distributed"
date: 2021-02-24T14:00:30-04:00
draft: false
---

Scientific data is fundamentally distributed: physically, conceptually, and temporally.

You can't situate all the data you'll ever need, once and for all, in one place. There will always be another source of
data. And another. Centralization doesn't work for large, global enterprises like modern science. Even
command-and-control corporate enterprises have gone from data warehouses to data lakes (still centralized, but less
stringently organized) to data meshes (decentralized!). Connection and flow among data nodes is key.

It's not just the data that's distributed -- the concepts are, too. People use different names for the same thing, the
same name for different things, "kinda-the-same" names for "kinda-different" things...oy. From the Zen of Python
(`import this`): "Namespaces are one honking great idea -- let's do more of those!" In Python code, I can have something
like "from pymatgen import Structure" at the top of a file and know that when this module talks about Structure, it's
talking about it in the sense specified by the python materials genomics (pymatgen) package.

Data needs similar means for disambiguation. In the RDF data model, each concept is a URI, like
[https://schema.org/unitCode](https://schema.org/unitCode) (which one might "import" by registering
"[https://schema.org/](https://schema.org/)" as a default namespace, or as the prefix "scm:" and then using
"scm:unitCode", etc.). Furthermore, RDF graphs (cf. knowledge graphs) provide additional disambiguation power in placing
concepts within a directed graph in which relations (edges) among concepts (nodes) are also unambiguously named URIs.

This note is getting a bit long, so I will defer treatment of the nature and implications of the temporal distribution
of scientific data to a separate note.

Are you sufficiently convinced that centralization, both for physical data instances and conceptual data-attribute
definitions, is untenable for modern collaborative research? Let me know.


{{< subscribe >}}

