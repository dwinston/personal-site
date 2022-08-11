---
title: "Schema Translation Infrastructure"
date: 2022-08-11T11:13:35-04:00
draft: false
---

Repurposing data is hard sometimes. Given a current application's data-worldview -- i.e., its schema
-- one cannot in general pull in historical data collected for different applications because those
applications had different worldviews -- i.e., they used different data schemas.

One may perform one-off or ongoing transformations -- e.g. ETL jobs -- as part of a hub-and-spoke
strategy to bring data from past worlds into the "present" world so that all the data can be queried
in a uniform way, in the language of the present-application schema.

Unfortunately, the "present" world is a moving target. And "past" worlds may be merely dormant --
they may become "present" again if a given application is revisited.

Rather than hub-and-spoke schema convergence and single-timeline data migration, what if schema
translation infrastructure sought to reconcile queries across multiple worlds? That is, what if
application-X-centric questions could travel to and collect partial information from
other-application-centric worlds using the languages (schema) of those worlds?

Building off Ink & Switch's ideas on edit lenses for schema evolution[^cambria] and off Radul and
Sussman's ideas on propagation networks for computation[^radul], as well as off the observed
salubrious hourglassing of the Internet's layered-architecture design[^beck2019], I'm thinking about
how to facilitate effective "schema networking" that acknowledges and embraces the never-ending
schema evolution characteristic of data collection efforts by research-producing organizations.

## Initial Scribbles

First, I offer a simplified recapitulation of the layered architecture of the Internet:

{{< figure src="/img/internet-layers-written.png"
    title="Layered Architecture for the Internet"
    width="80%" >}}

Next, I offer a mapping of the above to an analogous six-layered architecture for schema
translation:

{{< figure src="/img/schema-translation-infra-layers-written.png"
    title="Layered Architecture for Schema Translation"
    width="80%" >}}

The *physical protocol* layer is concerned with data (de)serialization/marshalling and storage. The
*data-link protocol* layer is where ETL happens -- how bytes are de-isolated and made accessible to
the network. The *network protocol* layer is where propagation among worldviews/schemas "runs", with
each "cell" (in the parlance of the propagation network literature) a join-semilattice (or is it a
meet-semilattice?) world that accumulates partial information via edit-lens functional propagators.
The *transport protocol* layer is RDF over HTTP ([FAIR Digital
Objects](/posts/a-fair-digital-object/)?), the *application protocol* layer is RDF query (SPARQL, a
Datalog, etc.), and the *application* layer is where specific-worldview-conforming data  (i.e.,
things you plot, perform exploratory data analysis (EDA) on, select/engineer features from to feed
to ML-model training, etc.) materialize.

Finally, I offer a rough diagram of how various layer activities and dataflow within/between them
may be visualized:

{{< figure src="/img/schema-translation-infra-layers-diagram.png"
    title="Schema Translation Infrastructure in Action"
    width="80%" >}}

I want to close by noting that the problem of schema reconnection comes up not only with research
laboratory datasets that were collected independently by different teams, but also with datasets
collected over a long period of time by a single team as project/application requirements evolve and
place adaptation pressure on the "working" schema to undergo several revisions, thus necessitating
reconnection among schema versions (i.e. migrations, but not necessarily unidirectional if, say, a
sub-team is still using an "old" schema and wants to contribute "new" data).

[^cambria]: "Project Cambria: Translate your data with lenses," Oct. 06 , 2020.
https://www.inkandswitch.com/cambria/ (accessed Aug. 01, 2022).

[^radul]: A. Radul, "Propagation networks: a flexible and expressive substrate for computation,"
Thesis, Massachusetts Institute of Technology, 2009. Accessed: Aug. 11, 2022. [Online]. Available:
https://dspace.mit.edu/handle/1721.1/54635

[^beck2019]: Beck, M. (2019). On the hourglass model. Communications of the ACM, 62(7), 48–57.
https://doi.org/10/gj3fnj

