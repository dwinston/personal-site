---
title: "Validating Translation"
date: 2022-09-01T10:20:34+02:00
draft: false
tags:
- FAIR-enabling-services
---


Given a [representation](https://www.w3.org/TR/dx-prof-conneg/#dfn-representation) of (meta)data
that [dcterms:conformsTo](http://purl.org/dc/terms/conformsTo) some [data
profile](https://www.w3.org/TR/dx-prof-conneg/#dfn-data-profile), you may wish to translate it to
another data profile.

If a resource is accesible from an HTTP server, then as a client you may [negotiate the content
representation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Content_negotiation) in a standard
way. Traditional content negotiation (aka "conneg") is limited to file formats, aka syntax rather
than semantics, but [content negotiation by profile](https://www.w3.org/TR/dx-prof-conneg/) (aka "connegp")
can facililate translation.

There may be many ways to [functionally
specify](https://www.w3.org/TR/dx-prof-conneg/#dfn-functional-specification) data profile
negotiation, i.e. translation. Ultimately, one [functional
profile](https://www.w3.org/TR/dx-prof-conneg/#dfn-functional-profile) is employed for a given
instance of translation.

Thus, it seems that one way to "validate translation" would be to identify the functional profile
employed and trace process outputs for conformance.

I'm really getting into weeds here, aren't I? My insistence on exploring the cross product of
{identifying,validating,indexing,translating,tracing} \\(\times\\)
{identifiers,validators,indexers,translators,tracers}  to elucidate FAIR-enabling services is a bit
dizzying. I shall cautiously continue.