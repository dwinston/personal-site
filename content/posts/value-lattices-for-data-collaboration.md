---
title: "Value Lattices for Data Collaboration"
date: 2021-04-07T11:17:16-04:00
draft: false
---

Values like "3" are typically considered separately from *constraints* like "< 10" or *types* like
"number".

What if these were all on equal footing as values in a hierarchy? "3" is an instance of "< 10" is an
instance of "number".

A lattice is a partially ordered set, in which every two elements have a unique least upper bound
(join) and greatest lower bound (meet). In a value lattice, "constraints" and "types" *are* values,
with "is a" as the partial order.

What this means, for example, is that if you use a value lattice to represent schemas, you can
always unambiguously merge multiple schemas independently of order -- the most general mutually
compatible schema is the unique greatest lower bound. You can also infer a schema/template for data
entry from concrete instances -- that would be the least upper bound. Finally, validating new data
against the current schema and verifying that a new schema is backwards compatible with the current
schema is the same operation -- is the former an "instance of" the latter?

Using a value lattice, there is no need for configuration/schema files to mutually import each other
within a package or project. Files can be split across organizational lines, each with a different
set of policies. There may also be an opportunity here for collaborative data querying. Whereas
validating data is the problem of finding data that is inconsistent with some constraints, querying
is the problem of finding data that matches some given constraints. Clearly these two concepts are
related.

For a deeper dive into value lattices and tooling to incorporate them into your work, check out the
[CUE project](https://cuelang.org/docs/concepts/logic/). Portions of my note here were lifted
directly from the linked page, as I did not feel they could be improved upon!

{{< subscribe >}}