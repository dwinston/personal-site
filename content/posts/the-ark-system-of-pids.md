---
title: "The ARK System of Persistent Identifiers (PIDs)"
date: 2022-07-01T16:00:01-04:00
draft: false
---

The [Archival Resource Key (ARK) system](https://arks.org/) is an alternative to the [Handle
system](https://donnywinston.com/posts/the-handle-system-of-persistent-identifiers/) to satisfy
[FAIR's F1 Principle](https://w3id.org/fair/principles/terms/F1).

Similar to the Handle system, naming authority for ARKs is distributed by allotting prefixes.
However, there is no "pre-prefix" administration via a small number of credentialed multi-primary
administrators, and there is currently no fee per allotted prefix, called a Name Assigning Authority
Number (NAAN).

Another difference between the Handle and ARK system is in distinguishing between a name assigning
authority (NAA), i.e. identifier minting, and a name mapping authority (NMA), i.e. identifier
resolution. With the Handle system, NAA and NMA functions are administered by the same organization.
With the ARK system, an NAA may be its own NMA, may migrate from one NMA to another, or may have
multiple NMA service providers.

For more on ARKs, see my post on [Object Persistence: A Matter of
Service](https://donnywinston.com/posts/object-persistence-a-matter-of-service/), the most recent
[specification](https://datatracker.ietf.org/doc/draft-kunze-ark/34/), and the [ARK
Alliance](https://arks.org/) website.
