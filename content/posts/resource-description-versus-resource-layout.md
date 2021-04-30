---
title: "Resource Description (Ontology/Schema) Versus Resource Layout (API)"
date: 2021-04-30T09:59:35-04:00
draft: false
---

Resource description refers to defining concepts and relationships that represent the content and
structure of some subject matter (ontology) or a database (schema) in a formal language. The
relationship between ontology and database schema is nuanced -- Uschold provides a nice
comparison.[^uschold] You can formally describe resources using the resource description framework
(RDF), SQL's data definition language (DDL), etc.

Resource layout refers to the arrangement of resources and their relationships for a particular
resource-oriented API.[^geewax] The layout isn't *intrinsic* -- it refers to choices regarding what
to "lay out".

Not every conceptual resource needs to "graduate" to be an API resource -- some may end their
journey at the point of becoming only in-lined data types of other resources (Do you need to
atomically interact with a concept?). Hierarchical relationships (i.e. containment/ownership) may
make sense when there are cascading actions or inherited access policy / properties.

Resource layout, as a layer on top of resource description, is an opportunity to make the common
case awesome -- without compromising the feasibility of advanced cases -- for a particular
application.

{{< subscribe >}}

[^uschold]: Uschold, M. ["Ontology and database schema: What’s the
difference?"](https://doi.org/10.3233/AO-150158). *Applied Ontology*, 10(3-4) pp. 243–258, 2015.
Based on a talk given in 2011
([slides](https://www.slideshare.net/UscholdM/ontologies-and-db-schema-whats-the-difference)).

[^geewax]: Geewax, JJ. [*API Design Patterns*](https://www.manning.com/books/api-design-patterns).
Manning, 2021.