---
title: "FAIR-Enabling Services Redux"
date: 2022-10-03T11:18:58-04:00
draft: false
level: Intermediate
keywords:
- FAIR-Enabling Services
- FAIR
---

I have sought to identify and enumerate core [FAIR-enabling
services](https://donnywinston.com/posts/fair-enabling-services/). I attempted a [five-week
experiment](https://donnywinston.com/posts/a-five-week-experiment-to-elaborate-on-fair-enabling-services/)
to expand on my tentative list, but I did not complete it. The list wasn't compelling for me.

I have been brewing an updated list of core FAIR-enabling services, which I hope to be less
bombastic about. Nevertheless, I want to share with you this list and my thoughts about concretizing
them through pedagogically minded demo implementations tied together by a running example that I
intend to refine and deploy for a real project.

FAIR-Enabling services:

1. an identifier _minter_ (e.g. [arknoid](https://github.com/jkunze/docker-arknoid))
2. a metadata _tracker_ (e.g. [terminusdb](https://github.com/terminusdb/terminusdb))
3. a metadata _transactor_ ([terminusdb](https://github.com/terminusdb/terminusdb) schema)
4. a metadata _indexer_, to feed a search engine (e.g. [elasticsearch](https://github.com/elastic/elasticsearch))
5. an identifier metadata _resolver_ (e.g. [fastapi](https://github.com/tiangolo/fastapi) with conneg)
6. a data object _retriever_ (e.g. [minio](https://github.com/minio/minio) s3 presigned urls)
7. a metadata _harmonizer_ (e.g. [cambria](https://www.inkandswitch.com/cambria/)-esque json patch graph)

I'd like to demo a service stack via `docker-compose`. Some resources I am thinking to consult or
leverage directly here are [arknoid](https://github.com/jkunze/docker-arknoid),
[TerminusDB](https://github.com/terminusdb/terminusdb),
[Elasticsearch](https://github.com/elastic/elasticsearch),
[FastAPI](https://github.com/tiangolo/fastapi), [MinIO](https://github.com/minio/minio), and
[Project Cambria](https://www.inkandswitch.com/cambria/).

My intended running example is the incorporation of heliophysics concepts into the [Unified
Astronomy Thesaurus (UAT)](https://astrothesaurus.org/) and harmonizing that with the
[OpenAlex](https://openalex.org/) concept scheme so that one may evaluate semantics-fueled
improvements to query understanding and thus search-result relevance via the OpenAlex dataset. The
OpenAlex dataset has value as a testbed for improvements to in-production search engines such as the
[SAO/NASA Astriphysics Data System](https://ui.adsabs.harvard.edu/).