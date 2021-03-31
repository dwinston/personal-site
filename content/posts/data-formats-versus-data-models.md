---
title: "Data Formats Versus Data Models"
date: 2021-02-17T13:51:08-04:00
draft: false
---

A format describes what your content "is"; a model describes what your content is "about". Is-ness issues will affect
people’s ability to use your data (it's not informative if it's not "in formation"), but about-ness is at the core of
analysis.

CSV and JSON are formats. SQL and RDF describe models.

What is your data "about"?

Is it about rectangular entities, each with a fixed number of attributes/columns, with cell references pointing to rows
of other rectangles? SQL models rectangular data.

Is your data about documents, each a tree structure that contains sub-document data? The document object model (DOM)
that your browser applies to every webpage is a fine example.

Is your data about named entities, each with a variable number of attributes and relations to other entities? Perhaps
sub-graphs of your data can be presented in rectangle/table- or document-friendly formats, but your data is more "about"
a graph of entities, their attributes, and their relations. RDF models graph/relational data.

And how do you communicate the about-ness (model) of your data when you share it (in a format)? Does the model travel
with the data, or is it lost / nontrivial to look up (what does that column/field mean)?

I'd love to know how you are achieving (or struggling to achieve) the format/model distinction, and the sharing of both
for any given dataset.

{{< subscribe >}}
