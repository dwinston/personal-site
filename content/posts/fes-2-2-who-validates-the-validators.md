---
title: "Who Validates the Validators?"
date: 2022-08-30T15:49:05+02:00
draft: false
tags:
- FAIR-enabling-services
level: Advanced
reqs:
- https://w3id.org/fair/fip/terms/Metadata-schema
- http://www.w3.org/ns/shacl#Validator
- https://json-schema.org/
- https://w3id.org/fair/fip/terms/Knowledge-representation-language
- https://w3id.org/fair/fip/terms/Structured-vocabulary
- https://w3id.org/fair/fip/terms/Semantic-model
- http://usefulinc.com/ns/doap#Specification
teaches:
- https://en.wikipedia.org/wiki/Robustness_principle
---

Given a <a href="https://w3id.org/fair/fip/terms/Metadata-schema">fip:Metadata-schema</a> and a validator for it,
such as a <a title="http://www.w3.org/ns/shacl#Validator" href="https://prefix.zazuko.com/sh:Validator">sh:Validator</a> or a [JSON Schema](https://json-schema.org/), how do you determine that the
validator is...valid? That it speaks the desired <a href="https://w3id.org/fair/fip/terms/Knowledge-representation-language">fip:Knowledge-representation-language</a>,
that it knows all the terms in a desired <a href="https://w3id.org/fair/fip/terms/Structured-vocabulary">fip:Structured-vocabulary</a> and checks their usage against a desired <a href="https://w3id.org/fair/fip/terms/Semantic-model">fip:Semantic-model</a>?
In other words, that it adheres to a <a title="http://usefulinc.com/ns/doap#Specification" href="https://prefix.zazuko.com/doap:Specification">doap:Specification</a>?

I do not know. However, I suspect that it is more important [to check output rather than input](https://en.wikipedia.org/wiki/Robustness_principle).

{{< subscribe >}}

{{< fairpoint >}}
