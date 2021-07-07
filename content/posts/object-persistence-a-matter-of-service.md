---
title: "Object Persistence: a Matter of Service"
date: 2021-07-05T14:08:02-04:00
draft: false
---

I recently encountered the Archival Resource Key ([ARK](https://arks.org/)) identifier scheme and
read its latest draft specification.[^1] Its thesis is that the persistence -- i.e., long-term
identification and access -- of any information resource -- i.e., an "object" -- is a matter of
service.

A stewardship promise must come from a current provider, which may not be the original assigner,
because an assigner simply cannot ensure persistence -- either via object structure or via a naming
scheme. The ARK spec makes a distinction between the so-called "memory institution" that acts as a
name assigning authority (NAA) and thus associates an identifier with an object, and a service
provider -- a name mapping authority (NMA) -- that actually stewards that information.

Without a description -- "a record bearing witness to the identifier's association with the object,
as recorded by a set of object characteristics"[^1] -- real identification is incomplete. A naked
identifier isn't enough -- you need the record, the "receipt." The name mapping authority -- which
may be the same as the name assigning authority for as long as funding/politics allows -- acts as
host, as steward.

Persistent identification (naked identifier plus description record) is separable from persistent
access. Description-only NMAs can redirect object-access requests to other NMAs, e.g. publishers
that restrict access to object content.

A key function of ARK's abstract model is for a service to deliver not only a descriptive metadata
record, but to deliver also a policy declaration: a declaration of permanence for each serviced
object -- its availability, identifier validity, content invariance, and change history. [NLM
"permanence levels"](https://www.nlm.nih.gov/pubs/techbull/ma05/ma05_archive.html) are an example of
such declarations.

On a practical level, ARK facilitates the distinction between name mapping and name assigning via
the anatomy of a typical ARK:

```bash
https://<nma>/ark:<naan>/<assigned_name>
```

The above is highly simplified. `<naan>` is the name assigning authority (NAA) number, i.e. the the
opaque number assigned to the NAA. `<nma>` is the name mapping authority -- `n2t.net` is commonly
used, just like `doi.org` is commonly used for resolving DOIs. `https://` is common, though ARK is
an abstract model with no concretions around use of e.g. JSON or even HTTP.[^2] Finally,
`<assigned_name>` can reflect object hierarchies and qualifiers for variants (versions, formats,
etc.), all in ways formally given in the ARK spec.

A memory institution names objects with identifiers like `ark:12345/x2fr5`, and any number of NMAs
may serve access to the named objects and/or to their descriptions. Just like your web browser
discovers an IP address for a given domain name, your browser can discover one or more NMAs
servicing a NAAN namespace and thus an ARK. This can work even if a preferred NMA is given but is
not available, e.g. the ARK is presented as `https://example.org/ark:12345/x2fr5`.

ARKs are kind of like DOIs, but you can assign names freely under your assigned NAAN, you can
migrate your object repository to any NMA at any time, and NMAs can be explicit to users about
multi-faceted persistence policies on a per-object basis, all while guaranteeing permanence of the
"naked" (string) identifier.

[^1]: J. A. Kunze, ["The ARK Identifier Scheme
(v.27)."](https://www.ietf.org/archive/id/draft-kunze-ark-27.txt) Internet Engineering Task Force
(IETF), Feb. 2021.

[^2]: However, a functional profile[^3] is introduced and outlined that uses HTTP URL query string
arguments (QSAs), e.g. `?info`. QSAs / URL parameters are referred to as "inflections" in the ARK
spec, which I find adorable.

[^3]: A citation within a citation? You read right. For more on "functional profile" as a term of
art for implementing an abstract model's functions, specifically via both HTTP URL QSAs and via HTTP
headers, see L. G. Svensson, R. Atkinson, and N. J. Car, “Content Negotiation by Profile: W3C
Working Draft,” Nov. 26, 2019.
[https://www.w3.org/TR/2019/WD-dx-prof-conneg-20191126/](https://www.w3.org/TR/2019/WD-dx-prof-conneg-20191126/).

{{< subscribe >}}