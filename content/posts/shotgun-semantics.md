---
title: "Shotgun Semantics"
date: 2022-08-01T16:28:46-04:00
draft: false
---

Developers often resort to *shotgun parsing*: scattering data checks and fallback values in various
places throughout the system’s main logic.[^cambria]

The habit of scattering parser-like behaviour throughout an application’s code and the resulting
inconsistencies in data handling can often lead not just to annoying complications and bugs, but
also security vulnerabilities.[^shotgun]

This is about reading data. What about when writing data, when setting the foundations for how it
will ultimately "behave" and be interpreted? Are you firing shotshells, or are you [slinging
webs](https://www.wikidata.org/wiki/Q79037)?

[^cambria]: "Project Cambria: Translate your data with lenses," Oct. 06 , 2020.
https://www.inkandswitch.com/cambria/ (accessed Aug. 01, 2022).

[^shotgun]: S. Bratus and M. L. Patterson, "Shotgun parsers in the cross-hairs," presented at BruCON 2012. Slides: http://langsec.org/brucon/ShotgunParsersBruCON.pdf (accessed Aug. 01, 2022).


