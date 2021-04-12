---
title: "Reusable Data Attributes"
date: 2021-04-05T11:16:00-04:00
draft: false
---

Do you repeatedly define the same field/attribute across different classes / entity types? For
example, you may have many different entities with an "id", a "name", etc. When an attribute
"belongs to" an entity, you need to repeatedly register specifications for each (re)definition: it's
a string, it needs to pass these tests to be considered valid, etc.

What if attributes were top-level? That is, you define them once and then freely associate them with
entities. This schema can be at the domain level, whereas application of attributes to define
entities can happen at the (well-named!) application level.

Applications can evolve independently of an upstream attribute schema, as each application entity is
an aggregation of attributes for a known execution and data context: for this process/function, what
attributes are required, and what does "valid entity" mean in this context?

[Attribute specs](https://docs.datomic.com/on-prem/schema/schema.html#attributes) may include an
identifier, value type (string, number, etc.), cardinality (either one or many values),
documentation, whether a value is unique across all entities, whether a value uniquely identifies
its entity, and validation functions.

When attribute specs are reused, entities are relieved of potentially inconsistent and error-prone
re-definition of attributes. Entity specs are then higher-level: they are about required attributes
and about entity-level validation -- constraints across attributes in the entity and perhaps across
other entities in the system.

{{< subscribe >}}