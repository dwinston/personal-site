---
title: "On the Hourglass Model, for FAIR"
date: 2021-05-17T14:43:22-04:00
draft: false
---

The hourglass model is an approach to layered system architecture where a middle layer is
intentionally constricted in order to support flexibility in the implementation of layers above and
below. Above the *spanning layer* are *applications*, and below the spanning layer are *supports*.

Beck (2019) provides a formal analysis of the hourglass model.[^beck2019] His Hourglass Theorem
conveys that
> a weaker layer specification has fewer possible applications but more possible supporting layers
than a stronger layer specification.

The [GO FAIR initiative](https://www.go-fair.org/today/fair-digital-framework/) is trying to
identify a plausible hourglass approach to infrastructure for FAIR data and services:

<img src="/img/go-fair-hourglass.png" width="100%"
     alt="GO FAIR hourglass" />

Their labeled [hourglass
icon](https://www.go-fair.org/resources/internet-fair-data-services/hourglass/) (reproduced above)
gives a good sense of the tradeoff. The spanning (exchange) layer needs to be strong enough to
facilitate a minimal variety of useful services, but must also be weak enough to facilitate the
greatest possible variety of supporting data that services can suck up through the straw.

[^beck2019]: Beck, M. (2019). On the hourglass model. Communications of the ACM, 62(7), 48–57.
https://doi.org/10/gj3fnj

{{< subscribe >}}