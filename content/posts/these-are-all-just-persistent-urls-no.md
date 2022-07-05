---
title: "These Are All Just Persistent URLs, No?"
date: 2022-07-05T09:06:03-04:00
draft: false
---

<!-- KaTeX block: \\[ x \rightarrow y \\] -->
<!-- KaTeX inline: \\( x \rightarrow y \\) -->

I am beginning to walk through each [question](https://w3id.org/fair/fip/terms/FIP-Question) of the
[FAIR Implementation Profile (FIP) Ontology](https://w3id.org/fair/fip/terms/FIP-Ontology). My goal
is to construct and share a populated model of people's articulations -- aka
[declarations](https://w3id.org/fair/fip/terms/FIP-Declaration) -- of choices they've made or with
[challenges](https://w3id.org/fair/fip/terms/FIP-No-Choice-Declaration) they face with regard to
addressing each question, as well as the
[considerations](https://w3id.org/fair/fip/terms/considerations) they associate with any such choice
or challenge.

The first question for which [I'm seeking
declarations](https://donnywinston.com/posts/fip-question-f1/) is
[F1-D](https://w3id.org/fair/fip/terms/FIP-Question-F1-D):
> What globally unique, persistent, resolvable identifiers do you use for datasets?
 
I've gotten some great responses so far, mostly
about people choosing to use the [Handle (incl.
DOI)](https://donnywinston.com/posts/the-handle-system-of-persistent-identifiers/) or
[ARK](https://donnywinston.com/posts/the-ark-system-of-pids/) systems.

I got a great question from my former group-mate [Shyam
Dwaraknath](https://www.linkedin.com/in/shyam-dwaraknath/):
> In the end these are all just persistent URLs no?

For all intents and purposes, *yes*. Practically, if you don't give someone a resolving[^1] HTTP(S)
URL, such that they can Locate and retrieve the Resource given a Uniform Identifier (i.e.,
URI\\(\implies\\)URL), they should be able to straightforwardly construct one.

Handles and ARKs use their compact forms to communicate

1. an intention of persistence, and (related to this)

2. a URL-construction protocol in case they are

    (a) not communicated as URLs, or

    (b) they are, but the URLs don't resolve.

If you see e.g. `10.1038/sdata.2016.18` somewhere, the hope is you will grok that
the `\d+[\.\d+]+/.+` pattern (period-delimited numbers, then a `/`, then stuff) is likely a Handle,
so you will try putting https://doi.org/ or https://hdl.handle.net/ before it. There either need to
be well-known public Handle HTTP Proxy servers, or you search around for "Handle proxy server".
You'll also see `doi:10.1038/sdata.2016.18` sometimes. Same principle. The hope is you know how to
URLify it trivially.

The form of an ARK is similar in intent. The hope is that if you see e.g. `ark:57802/dw0/agu/6045`
somewhere (for ARKs, the `ark:` prefix is part of the ID form, even in URL paths), you'll think
"this ID is intended to be persistent -- an archival resource key" and "I hope some name mapping
authority (NMA) is publicly resolving `ark:57802` IDs". The well-known public ARK HTTP Proxy is
<https://n2t.net>, and e.g. <https://n2t.net/ark:57802/dw0/agu/6045> passes through to
<https://ns.polyneme.xyz/ark:57802/dw0/agu/6045> because `https://ns.polyneme.xyz` is registered
there as the NMA for the name assigning authority (NAA) `ark:57802`.

Other persistent ID systems that imply/offer HTTP URLs have tighter coupling to the DNS domain
responsible for resolving the IDs. Some of these systems are intended for general use, such as
<https://purl.org/> and <https://w3id.org/>.

In these systems, prefixes are not *allocated* like with Handles or ARKs, and there is no emphasis
on prefixes being semantically opaque so as to increase the likelihood of continued commitment to
persistence if/when stewarding organizations change names. Rather, prefixes are *claimed*, like
<http://purl.org/dc> (serving e.g. <http://purl.org/dc/terms>) and <https://purl.org/dw> (serving
e.g. <https://purl.org/dw/squirrel>), or <https://w3id.org/nmdc> (where currently, all path
extensions, e.g. <https://w3id.org/nmdc/nmdc-schema>, resolve to the same page).

Other DNS-coupled systems are socially positioned as providing specific types of persistent
identifiers. Such systems include the World Wide Web Consortium (W3C) <https://w3.org/> namespace
for standards (e.g. <https://w3.org/ns/dcat>), the Open Researcher and Contributor ID (ORCID)
<https://orcid.org/> (e.g. <https://orcid.org/0000-0002-8424-0604>), the International Generic
Sample Number (IGSN) <https://igsn.org> (e.g. <https://igsn.org/IEWFS0001>), and the Research
Organization Registry (ROR) <https://ror.org/> (e.g. <https://ror.org/02jbv0t02>).

If/when any such special-purpose, domain-name-tied system cannot fulfill persistence, it is hoped
that there will be (a) an adopter organization and (b) sufficient signage (e.g. minimal maintenance
of the old domain as a static notice) to enable programmatic workarounds, like the case of the
Global Researcher Identifier Database (GRID) <https://grid.ac/> being passed to ROR for stewardship.

[^1]: Any HTTP URL is technically resolv*able*. Whether it _actually_ resolves in response to an
HTTP request is a matter of service.