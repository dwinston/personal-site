---
title: "The Handle System of Persistent Identifiers"
date: 2022-06-30T08:52:40-04:00
draft: false
---

The Handle system is a popular choice for the assignment and resolution of globally unique,
persistent identifiers. Governance is centralized with the [DONA Foundation](https://www.dona.net/),
and administration is distributed among so-called [Credentialed Multi-Primary Administrators
(MPAs)](https://www.dona.net/mpas), of which there are currently nine. You've likely heard of at
least one MPA: the [International DOI Foundation](https://www.doi.org/).

Each MPA is assigned a number. The DOI Foundation has `10`. This is why all DOIs begin with `10.`.
Each MPA can in turn give a "complete" prefix (everything before the `/`) to a so-called "naming
authority". The DOI Foundation[^doi-ras] gave the [Nature Publishing Group](https://www.nature.com/) (now
[Springer Nature](https://www.springernature.com/)) `10.1038`, for example, who in turn can create
as many local names as they'd like, such as `10.1038/sdata.2016.18`.

How do handles get resolved? Each handle prefix may have its own administrator, and administration
of handles is distributed, similar to the Domain Name System (DNS). The Handle system is compatible
with DNS, but does not require it. In practice, there are known public HTTP proxy servers such as
https://hdl.handle.net/ and https://doi.org/ that allow resolution of handles as URLs. Hence,
https://doi.org/10.1038/sdata.2016.18 is resolvable.

Another big MPA is the [Corporation for National Research Initiatives (CNRI)](https://cnri.net/).
CNRI governed the Handle system before passing it off to the formed-for-this-purpose DONA Foundation
in 2015. Before this, CNRI assigned MPA-esque numbers to a bunch of organizations, and these
continue to be administered by the CNRI-as-MPA, even though it's assigned number is `20` now. For
example, CNRI assigned `1721.1` to [MIT](https://web.mit.edu/), which is used for it's
[DSpace](https://dspace.mit.edu/) repository. My PhD thesis was assigned `1721.1/71495`. So,
<https://hdl.handle.net/1721.1/71495> and  <https://doi.org/1721.1/71495>[^1] (and
<https://dspace.mit.edu/handle/1721.1/71495>) all get you to it.

You can inspect Handle prefix records, which are analogous to DNS records, via
<https://hdl.handle.net/>. For example, <https://hdl.handle.net/1721.1> lets you know that this
prefix is administered by MIT DSpace via the CNRI MPA (see the `/20.ADMIN`-containing `HS_ADMIN`
entry).

So how do you start minting and resolving Handles?

Become a credentialed MPA? I don't know, that seems hard for an individual researcher. There are
only nine [credentialed by DONA](https://www.dona.net/mpas).

Request a completed prefix from an existing MPA, e.g. something that matches `10.\d+` from the DOI
foundation? Yes, you can do that. MPAs typically charge registration and annual service fees per
allotted prefix (i.e., the whole `.`-delimited number before the `/` in a handle). In the case of
the DOI Foundation, they delegate to e.g. [Crossref](https://www.crossref.org/) to assign `10.`
prefixes. In this case, for additional [fees](https://www.crossref.org/fees/), Crossref will resolve
identifiers for you (beyond assigning you a prefix to mint as many as you'd like).

A final method is to find a service provider that has a complete prefix and will let you mint
handles under their prefix, or will mint them for you. This is the most typical route for
researchers. For example, [Zenodo](https://zenodo.org) got `10.5281` from
[DataCite](https://datacite.org/) (another `10.\d+` service provider the DOI Foundation delegates
to), and they'll give you a full handle when you upload stuff to <https://zenodo.org>.
[ResearchEquals](https://www.researchequals.com) got `10.53962` from CrossRef, and they'll give you
one for anything you put on <https://www.researchequals.com/>. And of course, journal publishers
typically give you one when you publish an article with them.

[^doi-ras]: Actually, one of its [registration agencies
(RAs)](https://www.doi.org/registration_agencies.html), [Crossref](https://www.crossref.org/). The
DOI Foundation doesn't give out prefixes directly. Individuals request prefixes from RAs, not from
the DOI Foundation. Thank you [Ed Pentz](https://twitter.com/epentz) for clarifying this. \[footnote
added 2022-07-01\]

[^1]: Wait, what? It's a DOI? Nope. DOIs are Handles that start with `10.`. https://doi.org/ is
(currently) a public HTTP proxy server that resolves all Handles, regardless of prefix.