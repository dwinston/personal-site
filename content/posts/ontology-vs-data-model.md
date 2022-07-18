---
title: "Is an Ontology 'better' than a Relational Data Model?"
date: 2022-06-27T10:40:08-04:00
draft: false
---

Is an ontology "better" than a relational data model?
"More expressive power" doesn't always mean "better".
However, ontologies allow you to ratchet up power while [keeping logic in data structures](https://en.wikipedia.org/wiki/Rule_of_least_power).

By "relational data model", folks typically mean "SQL model".
In the RDF world, this is roughly on par with a SHACL model, i.e. a model that expresses constraints on the shapes of entities and on the so-called "primitive" types of their properties/attributes/columns/fields (string, boolean, integer, etc.).
Both SHACL and SQL can set the ranges of properties to be "reference" types, which is indirect in SQL through primitive-typed (usually an integer or string) foreign keys.

An ontology language allows for more expressive data modeling than shape and attribute validation, while staying at the level of declarative data description.
In the RDF world, OWL lets you express notions of commonality and variability familiar from object-oriented programming such as classes, subclasses, and properties -- you don't need a software-defined object-relational mapping (ORM) layer.
You can also express certain constraints for and between classes, entities (individuals), and properties.

There's nothing you can express using ontologies that you cannot also express using a SQL data model plus a general programming language, or just a programming language.
So why declaratively model data at all? Why SQL then and not just CSV files if you're going to load the data into Python et al. anyway?
The rule of least power (<https://en.wikipedia.org/wiki/Rule_of_least_power>).
Ontology languages give you more expressive power than shape-constraint languages while reducing the risk of non-reusability of your modeling logic for unforeseen applications.

{{< subscribe >}}