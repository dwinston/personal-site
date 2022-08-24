---
title: "Validating an Identifier Service"
date: 2022-08-23T16:23:41-04:00
draft: false
tags:
- FAIR-enabling-services
---

How do you validate that an [identifier service](https://w3id.org/fair/fip/terms/Identifier-service)
provides global uniqueness of minted keys, persistence of bindings, and resolution of keys to
descriptive metadata?

> The key problem with testing is that a test (of any kind) that uses one particular set of inputs
tells you _nothing at all_ about the behaviour of the system or component when it is given a
different set of inputs.[^1]

If you know that a given ID provided by a service is unique, that tells you *nothing at all* about
the uniqueness of another ID provided by that service. You need to understand -- be able to reason
about -- whatever algorithm the service uses to guarantee uniqueness, and trust that the service
implements that algorithm.

> The key problem is that a test (of any kind) on a system or component that is in one particular
_state_ tells you _nothing at all_ about the behaviour of that system or component when it happens
to be in another state.[^1]

If you know that an ID provided by a service is bound to a particular digital object and/or to
particular descriptive metadata, that tells you *nothing at all* about what the service will bind
that ID to tomorrow. You need to understand and trust any policy provided by that service regarding
persistence of bindings.[^2][^3]

> Running a test in the presence of concurrency with a known initial state and set of inputs tells
you nothing at all about what will happen the next time you run that very same test with the very
same inputs and the very same starting state...and things can’t really get any worse than that.[^1]

If you know that a service resolves an ID request to metadata describing a digital object and its
location, that tells you *nothing at all* about how the server will respond to an identical
follow-up request. You need to understand and trust the access protocols provided by the service.

{{< subscribe >}}

[^1]: B. Moseley and P. Marks, "Out of the Tar Pit." Feb. 06, 2006.
[[online](https://github.com/papers-we-love/papers-we-love/blob/master/design/out-of-the-tar-pit.pdf)]

[^2]: J. Kunze, S. Calvert, J. DeBarry, M. Hanlon, G. Janée, and S. Sweat, "Persistence statements: describing digital stickiness," Nov. 2016, Accessed: Aug. 23, 2022. [Online]. Available: https://escholarship.org/uc/item/2zm9x47c

[^3]: "Permanence Levels and the Archives for NLM’s Permanent Web Documents. NLM Technical Bulletin. 2005 Mar-Apr." https://www.nlm.nih.gov/pubs/techbull/ma05/ma05_archive.html (accessed Aug. 23, 2022).








