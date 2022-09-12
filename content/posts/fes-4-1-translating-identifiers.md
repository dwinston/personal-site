---
title: "Translating Identifiers"
date: 2022-09-12T15:59:25+02:00
draft: true
---

Don't. Identifiers should be opaque.

If you're given an <a title="http://www.w3.org/2002/07/owl#sameAs" href="https://prefix.zazuko.com/owl:sameAs">owl:sameAs</a> assertion from a party you trust, use that.

If you need to mint surrogates because what you're given aren't Globally Unique, Persistent and
Resolvable Identifiers (GUPRIs)[^gupri], either house your
inheritance as local parts/suffixes in your global namespace, assert datatype properties to record
the historical correspondence, or both.

[^gupri]: E. Schultes et al., "FAIR Digital Twins for Data-Intensive Research," Front. Big Data,
vol. 5, p. 883341, May 2022, doi: 10.3389/fdata.2022.883341.