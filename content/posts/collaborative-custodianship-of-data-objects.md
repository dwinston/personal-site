---
title: "Collaborative Custodianship of Data Objects"
date: 2021-05-07T14:26:44-04:00
draft: false
---

In a collaboration, data objects are produced at many sites. To make the data objects findable, you
may steward a central, searchable index for their metadata. How then do you make the data objects
accessible for download?

One common solution is to centralize the custodianship -- have all sites upload copies of their data
objects to a central store. The central store may partition storage across several physical servers
behind the scenes (e.g. an Amazon S3 bucket), but it is still logically a single store, managed by a
single custodian.

What about collaborative custodianship? This seems apt when the total volume of data is very large,
especially compared to the "active" volume in use at any given time. In this scenario, it seems
important to allow custodian sites to (1) only serve data to members of the collaborative, and (2)
use tiered storage.

One solution that could work here is to have a central registrar where sites register their data
objects as URIs, along with any required request headers and/or a required POST body. A site can
later update any data object's registration.

When a user in the collaborative wants a data object, they can be given the necessary request info,
along with a one-time bearer token if authorization is required. When a site receives a request, it
can confirm the token validity with the registrar before servicing the request. As a side effect of
token confirmation, the registrar can also compile usage statistics on behalf of each site.

As for accommodating tiered storage, it seems that having sites implement a variant of Amazon S3's
[RestoreObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_RestoreObject.html) API would
work well. For example, if a data object is available but not immediately accessible, the site gives
a 202 Accepted response, with an operation ID in a header for checking status via follow-up HEAD
requests. If a restore is already in progress, the response to a duplicate request is a 409
Conflict. And if retrieval is unavailable, a 503 Service Unavailable response with a Retry-After
header can allow a user agent to try again. In any case, once an object is available, a 303 See
Other response can direct a client to GET it from where it has been restored.

Are you part of a data collaborative with distributed custodianship? If so, how does that work, and
what about the system works well versus not as well?

{{< subscribe >}}

