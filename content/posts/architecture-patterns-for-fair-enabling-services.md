---
title: "Architecture Patterns for FAIR-Enabling Services"
date: 2022-10-17T10:26:37-04:00
draft: false
---

I've been trying to grok architecture patterns as presented by Percival and Gregory[^patterns] to
support domain-driven design and event-driven microservices with Python. I hope you find the diagram below useful.

{{< figure src="/img/architecture-patterns-with-python-for-fair-enabling-services.png" width="100%"
title="Relating domain-driven design, event-driven microservices, command-query responsibility segregation (CQRS) + views, and validation (of syntax, semantics, and pragmatics)" >}}

A microservices approach seems apt for FAIR-enabling services that need to be composed, flexibly,
for any given research artifact's digital lifecycle. Consider these services:

- minter[^arklet] (F)[^FAIR]
- binder[^arklet] (F)[^FAIR]
- resolver[^arklet] (F)[^FAIR]
- index[^index] (F)[^FAIR]
- object store[^objectstore] (A)[^FAIR]
- transactor[^transactor] (I)[^FAIR]
- harmonizer[^harmonizer] (I)[^FAIR]
- tracker[^tracker] (R)[^FAIR]

Consider how you may want to swap one technology choice for a given FAIR-enabling service with
another choice, at any time, as part of evolving FAIR infrastructure to which you connect in order
to collaborate on and publish / share research artifacts.

[^FAIR]: principle addressed: *F* &mdash; Findable, *A* &mdash; Accessible, *I* &mdash; interoperable, *R* &mdash; reusable.

[^arklet]: Example: "Arklet - A basic ARK resolver." Internet Archive, Oct. 14, 2022. Accessed: Oct. 17, 2022. [Online]. Available: https://github.com/internetarchive/arklet

[^index]: Example: "Elasticsearch". https://www.elastic.co/elasticsearch/

[^objectstore]: Example: "Amazon Simple Storage Service (Amazon S3)". https://aws.amazon.com/s3/

[^transactor]: Example: "Transactor | Datomic." https://docs.datomic.com/on-prem/overview/transactor.html (accessed Oct. 17, 2022). https://docs.datomic.com/on-prem/overview/transactor.html

[^harmonizer]: Example: "DataHarmonizer." Centre for Infectious Disease and One Health, Aug. 08, 2022. Accessed: Oct. 17, 2022. [Online]. Available: https://github.com/cidgoh/DataHarmonizer

[^tracker]: Example: "git - the stupid content tracker." https://git-scm.com/docs/git (accessed Oct. 17, 2022).

[^patterns]: H. J. W. Percival and R. G. Gregory, _Architecture patterns with Python: enabling test-driven
development, domain-driven design, and event-driven microservices_, First edition. O’Reilly, 2020.
([available online](https://www.cosmicpython.com/book/preface.html)).