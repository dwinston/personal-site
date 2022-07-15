---
title: "High-Precision Content Classification Using Hierarchy"
date: 2022-07-15T08:58:09-04:00
draft: false
---

Content classification is the most fundamental form of holistic content understanding. It helps make
your resources findable ([F2](https://w3id.org/fair/principles/terms/F2)) and connects them to other
resources ([I3](https://w3id.org/fair/principles/terms/I3)).

Content understanding represents each piece of content in the index. Relevance of content is a
function of query and content understanding. Query understanding represents each search query as a
search intent.

Classification maps a document to one or more predefined categories. We can do so using hand-tuned
rules or machine learning.[^1] The categories can be a flat list, or they can be arranged in a
hierarchical (single-hierarchy or faceted) taxonomy[^2].

If the categories are hierarchical and broadly applicable
([I1](https://w3id.org/fair/principles/terms/I1)), then a classifier might take advantage of the
hierarchy and more confidently map content to a non-leaf category (e.g., mapping a material to
“Semiconductor” rather than “High-Gap Semiconductor” or “III-V Semiconductor”). In general, it’s
best to map value objects and entities to leaf categories.

Reducing the number of labels substantially improves the precision of a classifier. But filtering
out infrequent labels decreases coverage, and it’s not clear that out-of-scope examples will be
recognized in production.([F4](https://w3id.org/fair/principles/terms/F4)) A more robust approach is
to leverage the hierarchical nature of a taxonomy and roll up infrequently used labels to their
parent or other ancestor categories.

[^1]: G. Ingersoll and D. Tunkelang, “Course Notes for ‘Search with Machine Learning.’” Corise
Education, Jun. 20, 2022. [Online]. Available:
https://corise.com/course/search-with-machine-learning/

[^2]: D. Tunkelang, “Taxonomies and Ontologies,” Medium, Aug. 30, 2017.
https://queryunderstanding.com/taxonomies-and-ontologies-8e4812a79cb2 (accessed Jul. 15, 2022).

{{< subscribe >}}