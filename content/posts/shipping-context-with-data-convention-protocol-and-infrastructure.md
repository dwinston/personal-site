---
title: "Shipping Context With Data -- Convention, Protocol, and Infrastructure"
date: 2021-03-05T14:27:46-04:00
draft: false
---

How do you effectively share a computational process?

You could simply share a directory of source code and rely on shared conventions -- shared programming language, shared
tooling for build and runtime environments, a README.txt convention for communicating setup instructions, etc.

You could go further and use e.g. a container runtime+image protocol such as that published by the Linux Foundation's
Open Container Initiative (used by Docker et al.). Necessary context is less likely to be missing.

Finally, you could share infrastructure such as a platform to run containers. Necessary context is even less likely to
be missing.

What about sharing data?

You could share a directory of files and rely on shared conventions -- field names, file types, a README. You might
provide a modicum of helpful context via the HTTP protocol and shared infrastructure (the Web) by hyperlinking to
remotely hosted resources in your README.

You could use a container protocol like the Data Package of the [Frictionless Data
toolkit](https://frictionlessdata.io/). With an ecosystem of tooling, necessary context is more likely to be "obviously
not missing" rather than merely "not obviously missing". If you can't "contain" all your data+context, Linked Data
protocols such as JSON-LD and CSV for the Web (CSVW) build off the HTTP protocol and shared Web infrastructure.

For further assurance that a data consumer isn't missing context, you can use infrastructure such as the
https://goodtables.io/ service for continuous validation of GitHub-or-S3-hosted spreadsheets (compatible with
Frictionless-Data-protocol formats), or use the so called ["Baked Data"
pattern](https://simonwillison.net/2020/Dec/13/datasette-io/) exemplified by the [Datasette
project](https://datasette.io/) and [Mozilla.org](https://mozilla.github.io/meao/2018/03/28/bedrock-the-sqlitening/)
(another "contain it all" approach based on continuous re-deployment of of a read-only database, e.g. a single-file
SQLite database).

If you can't contain all the data+context you need to share in one place -- i.e. when data sharing means data
collaboration, then I suggest infrastructure based on Linked Data -- https://data.world/ and https://terminusdb.com/ are
two examples -- that embraces your data being part of a Web -- not necessarily part of "the" Open Web, but a Web
nonetheless, with a basis on protocols like HTTP and DNS and on existing network infrastructure supporting those
protocols.

{{< subscribe >}}

