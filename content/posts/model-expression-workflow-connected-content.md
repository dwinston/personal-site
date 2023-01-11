---
title: "A Model-Expression Workflow for Connected Content"
date: 2023-01-11T05:54:28-05:00
draft: false
tags:
- raw
---

For each layer in the structured-content stack,[^Atherton2018] from least to most volatile (i.e. domain modeling
⟶ content design ⟶ interface design), draft successive model expressions,[^Żytkow1990] from most to least
ambiguous (as many expressions as needed to move confidently to the next stack layer).

Structured-content-stack breakdown:

1. Domain model (object types and relationships)
2.  Content
    - content model (content types and attributes)
    - content spec (labels and data types)
    - content population
3. Representation
    - content-type resource templates (incl. resource transclusions)
    - index templates
    - collection resource templates
4. Navigation
    - global navigation
    - contextual navigation


Model expressions:

1. model-memo (functional and non-functional requirements [^NFR])
2. model-diagram
3. model-formalism
4. model-implementation

[^Atherton2018]: M. Atherton and C. Hane, Designing connected content: plan and model digital products for today and tomorrow. San Francisco, CA: New Riders, 2018.
[^Żytkow1990]: J. M. Żytkow and A. Lewenstam, "Analytical chemistry; the science of many models," Fresenius J Anal Chem, vol. 338, no. 3, pp. 225–233, Jan. 1990, doi: 10.1007/BF00323013.
[^NFR]: https://en.m.wikipedia.org/wiki/Non-functional_requirement
