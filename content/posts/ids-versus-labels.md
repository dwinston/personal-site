---
title: "Identifiers Versus Labels"
date: 2021-06-04T10:52:48-04:00
draft: false
---

Data protocols vary over project lifetimes, and many projects involve parameter sweeps. You might
see filesystem directory structures evolve naming schemes like the following[^signac]:

```
# let's not overthink this at first.
concentration_A_0.25/
# hierarchy is good, right?
concentration_A/0.25/
# paths are getting too long.
conc_A/0.25/
# change to percentages. clever!
conc_A/25/
 # add a parameter
conc_A/25/temp_08/
# switch order, add another parameter
temp_08/conc_A/25/conc_B/05/
# ...
```

Or perhaps such decisions about hierarchy are reflected in a "flat" filesystem, e.g. you see one or
more of {`_`, `-`, `.`} as parameter delimiters in longer filenames, rather than `/`.

You certainly need to track where data came from and how to reproduce it. And it's convenient to be
able to visually compare two points in a state space without a lot of eye movement. Rather than
compare e.g. JSON documents that each take a large on-screen area to display, you want to compare
compact labels that each express a [composite key](https://en.wikipedia.org/wiki/Composite_key) in
the state space.

However, this composite key can change over the lifetime of a project as new parameters/dimensions
are added to the state space of measurements. You need flexible, adaptable labeling of data objects.

Labeling, however, is different than identification. What makes a good identifier? It should be easy
to use (i.e., to read/share/verify), unique, permanent, fast and easy to generate, and
informationally dense (i.e. compact). In addition, if security is a concern, it should be
opaque/unpredictable (so people can't guess IDs they aren't given).[^geewax]

Salient attributes here are *permanent* and *fast and easy to generate*. If you need to *think*
about what your identifiers should look like, there's a good chance you will find yourself
*re-thinking* your decision. This means not only that your identifiers will not be permanent, and
thus you need to deal with migrations, but they may be *not* fast and easy to generate because (a)
not all components of your composite key may be recorded yet for a given data object, or (b) minting
new identifiers is awaiting a new decision about your naming scheme.

Labels, on the other hand, can change over time. They can accumulate, each preferred by a given
audience due to spoken language and/or domain expertise. One label can be marked as preferred for
display by default in a given user interface.

Such labels can certainly be information-dense composite keys, facilitating rapid and text-based
recognition by eye of an object record without needing to look at *all* the metadata associated with
an object ID. Flexible labeling supports good identifiers.

[^signac]: Examples are taken from [this talk](https://www.youtube.com/watch?v=CCKQH1M2uR4) about
the [signac](https://signac.io/) data management framework, motivating its use of opaque IDs for
state-space points.

[^geewax]: Geewax, J. J. (2021). Resource Identification. In [*API Design
Patterns*](https://www.manning.com/books/api-design-patterns). O’Reilly Media.

{{< subscribe >}}