---
title: "Identifying Validation"
date: 2022-08-29T21:59:10+02:00
draft: false
tags:
- FAIR-enabling-services
---

What conveys that data has been validated or is yet to be validated?

How do you identify the nature and process of validation for a given digital object?

Who is involved? What auxiiary resources are involved? Is the process:

1. Do-it-yourself, with (implicit or explicit) references to validation assets?

2. Do-it-with-you, with references to validation services?

3. Do-it-for-you, with references to validation results and/or signoffs?


An example of explicit reference amenable to do-it-yourself validation is the `schemaURL` field in an OpenLineage RunEvent JSON document, which links to its JSON Schema definition:

```json
{
  "eventType": "START",
  "eventTime": "2020-12-09T23:37:31.081Z",
  "run": {
    "runId": "3b452093-782c-4ef2-9c0c-aafe2aa6f34d",
  },
  "job": {
    "namespace": "my-scheduler-namespace",
    "name": "myjob.mytask",
  },
  "inputs": [
    {
      "namespace": "my-datasource-namespace",
      "name": "instance.schema.table",
    }
  ],
  "outputs": [
    {
      "namespace": "my-datasource-namespace",
      "name": "instance.schema.output_table",
    }
  ],
  "producer": "https://github.com/OpenLineage/OpenLineage/blob/v1-0-0/client",
  "schemaURL": "https://openlineage.io/spec/1-0-0/OpenLineage.json#/definitions/RunEvent"
}
```

Flavors of do-it-with-you validation include checksums and content hashing. You give a service some
input with a checksum so that the service can verify that your input is plausible. A service gives
you a content hash so that you can verify that its output is plausible. But how do you identify what
is being done, and to which field ([perhaps it's done to the object identifier
itself](https://github.com/multiformats/cid))? One useful standard is the HTTP
[`Digest`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Digest) header.

Do-it-for-you signoffs may involve digital signatures (and there is a standards-track HTTP
[`Signature`](https://wicg.github.io/webpackage/draft-yasskin-http-origin-signed-responses.html#name-the-signature-header)
Header).

It's clear that cryptography must play a big role here:

> We should accept the premise that people will not run their own servers by designing systems that
can distribute trust without having to distribute infrastructure. This means architecture that
anticipates and accepts the inevitable outcome of relatively centralized client/server
relationships, but uses cryptography (rather than infrastructure) to distribute trust.[^moxie]

[^moxie]: M. Marlinspike, "My first impressions of web3," Moxie Marlinspike, Jan. 07, 2022. https://moxie.org/2022/01/07/web3-first-impressions.html (accessed Aug. 29, 2022).

