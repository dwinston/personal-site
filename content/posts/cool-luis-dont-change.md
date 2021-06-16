---
title: "Cool LUIs Dont Change"
date: 2021-06-16T11:53:06-04:00
draft: false
---

After my last note on identifiers, Leo Talirz pointed me to a great riff[^cool-dois] on Tim
Berners-Lee's classic note[^cool-uris] on "cool URIs".

In the "Cool DOIs" article, Fenner breaks down a DOI into three parts: proxy, prefix, and suffix. A
proxy is a server that maintains a map from prefixes to registrants. Example proxies are
[https://doi.org/](https://www.doi.org/) and [https://hdl.handle.net/](https://hdl.handle.net). An
example prefix is `10.5281`. [https://doi.org/10.5281](https://doi.org/10.5281) and
[https://hdl.handle.net/10.5281](https://hdl.handle.net/10.5281) thus should return the same
information: that given a DOI with prefix `10.5281`, e.g. `10.5281/ZENODO.31780`,
[datacite.org](https://datacite.org/) is the registrant from which you can resolve the full DOI.
Thus, when you ask for [https://doi.org/10.5281/ZENODO.31780](https://doi.org/10.5281/ZENODO.31780),
the [https://doi.org/](https://www.doi.org/) proxy looks up `10.5281` and tells your web client to
ask datacite.org for a URL corresponding to `10.5281/ZENODO.31780`. The URL is at zenodo.org,
meaning folks at zenodo.org registered the DOI with datacite.org.

McMurry et al.[^mcmurry] characterize a URI-as-identifier in a similar manner: as resolver, prefix,
and local ID. A resolver can be a "primary" resolver, e.g. doi.org, but it can also be a so-called
"meta-resolver"[^compact], e.g. [identifiers.org](https://identifiers.org/) or
[n2t.net](https://n2t.net/). You register a prefix with a meta-resolver,  and you also register
resolution providers for your prefix. For example, someone registered the [doi
prefix](https://registry.identifiers.org/registry/doi) with identifiers.org, along with a resolution
provider with URL pattern `https://doi.org/{$id}`. Because identifiers.org and n2t.net share
registrations, you can ask for
[https://n2t.net/doi:10.5281/zenodo.18003](https://n2t.net/doi:10.5281/zenodo.18003), which
meta-resolves to [https://doi.org/10.5281/zenodo.18003](https://doi.org/10.5281/zenodo.18003) via
URL pattern filling, and doi.org takes it from there. Another registered prefix is
[uniprot](https://registry.identifiers.org/registry/uniprot), with provider patterns
`http://purl.uniprot.org/uniprot/{$id}` and `https://www.ncbi.nlm.nih.gov/protein/{$id}` (so a
meta-resolver can try an alternative if the primary provider is down).
[https://identifiers.org/uniprot:A0A022YWF9](https://identifiers.org/uniprot:A0A022YWF9) or
[https://n2t.net/uniprot:A0A022YWF9](https://n2t.net/uniprot:A0A022YWF9) yield the same result.
`uniprot:A0A022YWF9` is an example of a so-called compact URI (CURIE).

With meta-resolvers, you have semantic flexibility in your choice of prefix. Fenner emphasizes that
DOI prefixes should be random and opaque because registrant/organization names can change. With
meta-resolution, if UniProt changes their name, they can register a new prefix and encourage its use
while still supporting the `uniprot` prefix. However, local IDs should be unique. My title for this
note reflects this revision: cool local unique identifiers ("LUIs"[^compact]) don't change.

Berners-Lee's note gives sage advice related to rolling your own resolver for LUIs via a server
hosted at a domain name you control. For semantically flexible prefixing, qualify everything with
creation date. The precision of this date can reflect an acceptable cadence for updates: for
research data projects, I think month-level precision, e.g. `/YYYY/MM/`, is acceptable. Thus,
`https://<domain>/2021/06/<org>/<LUI>` reads as "ask `<domain>` for the record for `<LUI>` under the
namepace `/2021/06/<org>`, i.e. from the data repository that, in June 2021, `<domain>` knew by the
name `<org>`.

You can register these `https://<domain>/YYYY/MM/<org>/` namespaces as prefixes with meta-resolvers
and/or within your data products (e.g. as prefixes in RDF serializations). For a given `/YYYY/MM/`
qualification, your organization `<org>` can reflect the semantic partitioning strategy du jour (or
rather, du mois), e.g. {`/YYYY/MM/mp/calculations/`, `/YYYY/MM/mp/materials/`,
`/YYYY/MM/mp/structures/`,...}. The important thing here is that each such prefix is merely an alias
for a permanent and semantically opaque repository ID within `<domain>`, akin to the `10.5281`
example for DOIs.

This leaves us, at last, to LUIs. For these, I agree with Fenner's note and with Geewax[^geewax]:
use random integers encoded with [Crockford's Base32](https://www.crockford.com/base32.html) and a
checksum. For example, using the [base32-lib](https://pypi.org/project/base32-lib/) Python packaged
by [Invenio](https://inveniosoftware.org/) (spun out of CERN) folks:

```python
import base32_lib as base32

id_encoded = base32.generate(
    length=10,
    split_every=4,
    checksum=True
)
print(id_encoded)  # tw0t-ywdj-94
id_decoded = base32.decode(
    encoded=id_encoded,
    checksum=True
)
print(id_decoded)  # 923446243762
id_encoded2 = base32.encode(
    id_decoded,
    split_every=4,
    checksum=True
)
print(id_encoded2)  # tw0t-ywdj-94 
```

In the example, I specify the total length of encoded strings to be 10 characters, including 2
characters for the (ISO 7064, MOD 97-10) checksum. Thus, strings decode to 40-bit integers -- 8
characters * (log2(32) = 5) bits/character. There are 2**40 ~ 1 trillion possible LUIs.

What's nice about base32 encoding is that you can insert optional dashes anywhere for readability.
Here I insert one every 4 characters, yielding LUIs like `tw0t-ywdj-94`. The encoding is also
case-insensitive, and excludes the letters `I`, `L`, and `O`, because they can be visibly confused
with the numbers `1` and `0` -- when decoding, a supplied letter `O` will be replaced with the
number `0`. The letter `U` is also excluded to avoid accidental obscenity.

You can use up to 12 characters (14 with checksum) for encoding up to ~ 1.1 quintillion (10**18)
LUIs and still store them internally as 64-bit integers. I think that my 8-character (12 with
checksum and dashes) example above is a good tradeoff for compactness and cardinality -- you can
always create another repository under your domain, e.g. for transient/internal LUIs.

Finally, I do recommend recording your LUIs in an index so that collisions during generation, while
unlikely, are thwarted. Being able to encode LUIs as integers can help ensure fast index lookups.

[^cool-dois]: M. Fenner, “Cool DOI’s,” DataCite Blog, 2016.
[https://doi.org/10.5438/55e5-t5c0](https://doi.org/10.5438/55e5-t5c0) (accessed Jun. 15, 2021).

[^cool-uris]: T. Berners-Lee, “Cool URIs don’t change.,” 1998.
[https://www.w3.org/Provider/Style/URI](https://www.w3.org/Provider/Style/URI) (accessed Jun. 15,
2021).

[^mcmurry]: J. A. McMurry _et al._, “Identifiers for the 21st century: How to design, provision, and
reuse persistent identifiers to maximize utility and impact of life science data,” _PLoS Biol_, vol.
15, no. 6, p. e2001414, Jun. 2017, doi: [10/b88j](https://doi.org/10/b88j).

[^compact]: S. M. Wimalaratne et al., “Uniform resolution of compact identifiers for biomedical
data,” Sci Data, vol. 5, no. 1, Art. no. 1, May 2018, doi: [10/gdh496](https://doi.org/10/gdh496).

[^geewax]: J. J. Geewax, [*API Design Patterns*](https://www.manning.com/books/api-design-patterns).
O’Reilly Media, 2021.

{{< subscribe >}}