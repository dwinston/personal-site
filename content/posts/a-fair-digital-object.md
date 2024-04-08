---
title: "A FAIR Digital Object - Inching up the Hourglass"
date: 2022-07-19T11:15:09-04:00
draft: false
tags:
  - scholarly
---

Whether deliberate[^1] or inevitable[^2], the hourglass architecture of the Internet supports a
great diversity of applications implemented using a great diversity of supporting services:

<figure>
<img src="/img/internet-hourglass.png" width="100%"
     alt="An (incomplete) illustration of the hourglass Internet architecture showing the six layers, from top to bottom: specific applications, application protocols, transport protocols, network protocols, data-link protocols, and physical-layer protocols. A FAIR Digital Object (FDO) protocol could extend the HTTP application protocol."
     title="An (incomplete) illustration of the hourglass Internet architecture showing the six layers, from top to bottom: specific applications, application protocols, transport protocols, network protocols, data-link protocols, and physical-layer protocols. A FAIR Digital Object (FDO) protocol could extend the HTTP application protocol."/>
<figcaption>An (incomplete) illustration of the hourglass Internet architecture showing the six layers, from top to bottom: specific applications, application protocols, transport protocols, network protocols, data-link protocols, and physical-layer protocols. A FAIR Digital Object (FDO) protocol could extend the HTTP application protocol.</figcaption>
</figure>

Could there be a minimal "spanning layer" protocol for FAIR-principled[^fair] applications and
services? The [FAIR Digital Object (FDO)](https://fairdo.org/) has emerged as a conceptual nexus for
consideration of such a protocol.

There is a working draft online for an FDO framework.[^fdof] In it, an identifier resolves to a
digital object (byte sequence) by default, but one may also request a so-called identifier record.
This record would certainly support -- via a simple qualified reference -- the operation of
accessing the identified object's value-obvious situational information, i.e. the raw byte sequence.
Crucially, the identifier record would also support -- again, via simple qualified references --
operations to access methodological (still value-obvious to certain consumers) and more
philosophical (epistemic, ontological, axiological -- value typically not obvious) information:

<figure>
<img src="/img/FDOF-IR_resolution.png" width="100%"
     alt="A FAIR Digital Object (FDO) framework - the identifier record, identifier resolution behavior, typing, and metadata schemas and records."
     title="A FAIR Digital Object (FDO) framework - the identifier record, identifier resolution behavior, typing, and metadata schemas and records."/>
<figcaption>A FAIR Digital Object (FDO) framework - the identifier record, identifier resolution behavior, typing, and metadata schemas and records (<a href="https://fairdigitalobjectframework.org/">source</a>). </figcaption>
</figure>

{{< subscribe >}}

[^1]: M. Beck, "On the hourglass model," Commun. ACM, vol. 62, no. 7, pp. 48–57, Jun. 2019, doi:
10/gj3fnj.

[^2]: S. Akhshabi and C. Dovrolis, "The evolution of layered protocol stacks leads to an
hourglass-shaped architecture," SIGCOMM Comput. Commun. Rev., vol. 41, no. 4, pp. 206–217, Oct.
2011, doi: 10.1145/2043164.2018460.

[^fair]: M. D. Wilkinson et al., "The FAIR Guiding Principles for scientific data management and
stewardship," Sci Data, vol. 3, no. 1, p. 160018, Mar. 2016, doi: 10/bdd4.

[^fdof]: L. O. Bonino da Silva Santos, "FAIR Digital Object Framework Documentation," Nov. 03, 2021.
https://fairdigitalobjectframework.org/ (accessed Jul. 19, 2022).
