---
title: "Relational Homology"
date: 2020-06-02T09:55:31-04:00
draft: false
---

Homology deals with substructure similarity. For example, the structures of concern may be gene sequences -- structures
with clear reification as physical arrangements of atoms. An example technique for evaluating such structural homology
among genes is k-mer search.

Let *structural homology* refer here to homology over concrete structures, and let *relational homology* refer to
homology over abstract relationships that connect concrete structures. This distinction is akin to that between the
analysis of specialized data structures versus graph data.

Data structures and algorithms are intimately linked. Specialized data structures afford associated algorithms for
specialized analysis. Graphs, as data structures that may encode abstract relations and thus must be traversed,
will be slower to analyze than more concrete data structures designed to perform particular operations efficiently.

Consider program interpretation versus compilation. The code-as-data is operated upon similarly in both cases. With
code execution via an interpreter, a rich dynamism is possible for parsing code and data structure on the fly. With
a compiler, guarantees on program and data structure allow the interpretation to be done just once,
and with greater scrutiny for optimization opportunities.

People routinely conceptualize using graphs. Drawing nodes and edges on a whiteboard is a common technique for
thinking about processes, and the resources upon which processes act. Great swaths of mathematics have been
unified under category theory's objects (nodes) and arrows (edges).

Of course, people also routinely need to concretize their abstract conceptualizations. Better
user experiences can follow from translation of graphs into more specialized data structures and associated
algorithms, for efficiency both of machine execution and of human mental modeling (and thus of formulation of
interface-affordant queries).

When designing interfaces to aid a user in identifying similarities among data in a large collection, it is tempting
 to focus only on structural homology, in guiding users to probe known unknowns. Apart from searching for homologous
 data structures, users may also benefit from searching for homologous metadata structures -- a search for relational
 homology, a probing of unknown unknowns. Specialized lexical search, like k-mer search, certainly has its place in a
  multiscale model of search across domain-specific data -- but so does semantic search.