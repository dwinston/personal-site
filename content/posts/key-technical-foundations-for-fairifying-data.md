---
title: "Key Technical Foundations for FAIRifying Data"
date: 2022-12-22T09:25:52-05:00
draft: false
---

The key technical foundations for FAIRifying data are (1) ubiquitous persistent identifiers; (2) rich controlled metadata; and (3) granular programmatic access. These foundations provide a basis for FAIR data infrastructure.

This note is inspired by Rory Macneil’s recent interview with Sharif Islam on the FAIR Data Podcast, published on 2022-12-21. In particular, I expand on the Q&A segment starting at PT14M10S.

# ubiquitous persistent identifiers (PIDs)

Identifiers must be persistent. Persistence is a matter of service, which needs organizational support. Furthermore, you are playing on hard mode here if you don’t ensure global uniqueness via HTTPS URIs. Crucially, PIDs must be ubiquitous across data holdings. A single PID that addresses all study-publication data elements as an aggregate, e.g. “one DOI for the primary article’s supplemental dataset”, is insufficient.

# rich controlled metadata

Metadata makes PIDs findable. Catalogs and search portals use metadata to help you find PID-associated content. Metadata elements must be controlled; that is, so-called controlled vocabularies must be used to boost (a) leverage in tagging and (b) precision and recall in retrieval, which is critical with “big” data-item collections. Furthermore, the controlled metadata needs  to be rich — tracking only “minimal” required metadata elements is insufficient. Finally, you are playing on hard mode if your control mechanism does not use PIDs for knowledge organization. A system of least power here is the W3C Simple Knowledge Organization System (SKOS).

# granular programmatic access

Programmatic access must be supported. A well-documented, open-standards-based protocol
facilitates machine-to-machine interactions to glue things together
in a way that is distinct from affordances possible with human-centered interfaces (including bespoke APIs) and portals. This programmatic access must be granular — egress costs scale with data volume delivered, so let users sub-select slices of data. You are again playing on hard mode if programmatic access, and communicating granularity of such access, does not use PIDs. The HTTP protocol and URI scheme were designed for this, as were the W3C RDF (Resource Description Framework) Recommendations.

