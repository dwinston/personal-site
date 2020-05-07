---
title: "Data-Driven Decoding"
date: 2020-05-07T14:57:31-04:00
draft: false
---

There's a Python library called `monty` that supports a convention
for moving between JSON objects and Python class instances.
The major components are a mix-in class, `MSONable`, along with subclasses of
`json.encoder.JSONEncoder` and `json.decoder.JSONDecoder`.

An appropriate JSON object will have two special keys: `@module` and `@class`.
The string values of these are used in Python to essentially run
```python
from @module import @class
```
This isn't how it's actually done -- the syntax alone is wrong -- but the idea is that
the `@module` and `@class` fields in the JSON object
are used to import the Python class needed
to instantiate an appropriate object. The rest of the key-value pairs in the source
JSON object are passed as keyword arguments to the class constructor, thus creating a
Python object corresponding to the source JSON.

This instantiation is done recursively for all field
values in the source JSON,
so the procedure can work even for Python classes that take parameters with
non-built-in types.

In this convention, hints for how to interpret the data are passed as data.
There is no separate "metadata" file that an application needs to
know about and process. An application can be passed an anonynous JSON object and
infer what it means. The decoding is driven by the data. 

## RDF and data-driven decoding

RDF-based applications use special keys analogous to the
MSON format's `@module` and `@class`. With RDF, though, the keys are
unambiguous identifiers (URIs) and typically build on vocabulary standards
such as RDFS Schema and OWL ontonologies.

In RDF, one could use the key [`rdf:type`](http://www.w3.org/1999/02/22-rdf-syntax-ns#type)[^rdfns]
-- or another key that is a [`rdfs:subPropertyOf`](http://www.w3.org/2000/01/rdf-schema#subPropertyOf) `rdf:type` -- to
 supply a URI
 value that
 represents a Python class.
 Because the identity of the class is unambiguous,
 an application might offer to `pip install` it if applicable.
 
 Finally, because RDF is a set of statements --
 3-tuple (aka
  *triple*) forms of (subject, predicate, object), an RDF subject[^bnodes] can have multiple objects given for the
  same predicate. Thus, one can associate a subject with multiple classes, each a
  valid alternative in the right context. The same set of statements could drive a `matplotlib` plot in a Jupyter
   notebook or a React component in a browser dashboard, without needing to
   [hard-code](https://plotly.com/dash/) such interoperability for defined use cases.

[^rdfns]: `rdf:` is a common prefix for `<http://www.w3.org/1999/02/22-rdf-syntax-ns#>`, and tooling for prefixed
 terms and registering namespaces is common in the RDF ecosystem: no one typically types out or even needs to look at
  long URIs.
 [^bnodes]: The subject of a set of triples can be anonymous,
 analogous to a JSON object without a name bound to it.
 Such a node in an RDF graph is called a *blank node*.