---
title: "Validation: Syntax, Semantics, and Pragmatics"
date: 2022-07-18T10:24:18-04:00
draft: false
---

Validation is about preconditions for operation. It may be useful to separate preconditions into
three subtypes: syntax, semantics, and pragmatics.[^1]

*Syntax*: Rules about what's grammatically well-formed. Example: A `CalculateAqueousStability`
command may have a set of atomic-composition pairs and a set of ion-concentration pairs. An
atomic-composition pair is a string paired with a number between 0 and 1. An ion-concentration pair
is a string paired with a number.

*Semantics*: Rules about what may be syntactically valid but is nonetheless nonsense. Example: A
`CalculateAqueousStability` command may be syntactically valid, but it's compositions don't add up
to 1, the ion concentrations are physically implausible, etc.

*Pragmatics*: Rules about contextual appropriateness for processing a syntactically and semantically
valid message. Example: an online system can't efficiently calculate stability for a system of more
than 4 atomic elements on-the-fly, so this kind of command is rejected.

<figure> <img src="/img/pourbaix-app-command-example.png" width="100%" alt="Calculate Aqueous Stability" title="Calculate Aqueous Stability"/>
<figcaption>Calculate Aqueous Stability <a href="https://materialsproject.org/pourbaix">on materialsproject.org</a>.</figcaption>
</figure>

[^1]: H. J. W. Percival and R. G. Gregory, *Architecture patterns with Python: enabling test-driven
development, domain-driven design, and event-driven microservices*, First edition, pp 255-264.
O’Reilly, 2020.

{{< subscribe >}}