---
title: "Data Dictionaries for Humans and Machines"
date: 2021-04-23T13:14:49-04:00
draft: false
---

Shared datasets often have column/field names that are ambiguous in their meaning, or contain
identical/related concepts with different names, hindering reuse. This ambiguity happens regardless
of the method of sharing -- via files, web pages, or APIs. The traditional solution for this is to
provide documentation.

However, documentation is typically delivered “out-of-band”, i.e., not directly linked within the
same artifact (file/object) as the data. Furthermore, any linking among terms by different data
providers, whether to assert equivalence or to clarify differences, is typically done in an ad hoc
manner, hindering interoperability and thus reuse.

I am getting started with a [working group of materials
scientists](https://github.com/marda-dd/docs) to develop data dictionaries using Linked Data
principles. I'd like to highlight one feature of the HTTP standards that is helpful in serving both
human-readable and machine-readable documentation for data:

> In HTTP, ***content negotiation*** is the mechanism that is used for serving different
representations of a resource at the same URI, so that the user agent can specify which is best
suited for the user (for example, which language of a document, which image format, or which content
encoding).
> <br/>— [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Content_negotiation)

For example, let's say we have a data dictionary identified as
<https://ns.polyneme.xyz/2021/04/marda-dd/test#> with a contained term
<https://ns.polyneme.xyz/2021/04/marda-dd/test#helloWorld>. When you click on the link in a web
browser, your user agent (e.g. Firefox, Chrome, Safari, etc.) assumes you want a response in the
"text/html" format. However, if you are accessing the resource programmatically, you may want a
different format:

```shell
# A readable, hand-editable RDF format ("turse [sic] triples")
curl -H "Accept: text/turtle" \
    https://ns.polyneme.xyz/2021/04/marda-dd/test#helloWorld
# JSON-LD
curl -H "Accept: application/ld+json" \
    https://ns.polyneme.xyz/2021/04/marda-dd/test#helloWorld
# XML
curl -H "Accept: application/rdf+xml" \
    https://ns.polyneme.xyz/2021/04/marda-dd/test#helloWorld
# Or explicitly request HTML
curl -H "Accept: text/html" \
    https://ns.polyneme.xyz/2021/04/marda-dd/test#helloWorld
```

Not all web servers implement content negotiation. However, it is a nice alternative to making data
consumers scrape web pages, find links by eye to obtain different formats, or remember your
convention for how to alter a URL to obtain the desired resource -- it's the same resource, just a
different representation.

You can have a look at the implementation of the above "hello world" example
[here](https://github.com/marda-dd/hello-world/tree/main/dwinston). Thank you [Matthew
Evans](https://ml-evs.science/) for contributing to the code.

{{< subscribe >}}