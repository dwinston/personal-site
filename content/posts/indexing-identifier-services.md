---
title: "Indexing Identifier Services"
date: 2022-08-24T22:55:26-04:00
draft: false
tags:
- FAIR-enabling-services
---

Where do you look for identifiers?

If you're looking for a URI, the IANA has a [registry of
schemes](https://www.iana.org/assignments/uri-schemes/uri-schemes.xhtml), like `https`, `mailto`,
and `tel`.

These days, to resolve an identifier, you generally use the `https` scheme, which has an `authority`
component in its URI format. You can go with content addressing like [IPLD
CIDs](https://ipld.io/glossary/#cid), but that doesn't solve where to look -- it solves knowing that
you found the thing (or that you already have the thing).

Authority is hard to persist. So people and organizations pool efforts towards generic authority
under the `https` URI scheme, like `hdl.handle.net`, `doi.org`, `n2t.net`, `identifiers.org`,
`purl.org`, `w3id.org`, `wikidata.org`, etc. Or they pool towards authority with narrower scope,
like `orcid.org`, `ror.org`, `igsn.org`, etc. Or they just pursue lasting authority with a new
`.org` or through a trusted `.gov`, etc.

How do you index identifiers from various sources? There are efforts like
[LOV](https://lov.linkeddata.es/dataset/lov/) for vocabularies, and
[Crossref](https://www.crossref.org/) and [DataCite](https://datacite.org/) for DOIs.

I think [OpenAlex](http://openalex.org/) is setting a nice example of collecting identifiers from
various systems and connecting them, along with descriptive metadata.

What about collecting identifier services? Is this of interest? Is it a fool's errand due to the
rise and fall of authority? Or is tracking and using the rising and falling of reputation and
reliability, Google-PageRank-style, a way to shepherd researchers to robust persistence of
identifiers?

{{< subscribe >}}
