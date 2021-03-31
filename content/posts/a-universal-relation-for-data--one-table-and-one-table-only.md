---
title: "A Universal Relation for Data -- One Table and One Table Only"
date: 2021-03-17T14:44:19-04:00
draft: false
---

You have a variety of entities, each with a variety of attributes, and each involved in a variety of relationships.

One approach to manage such data is a collection/spreadsheet/table approach where you partition your entities. Each
entity has a primary address in a document/row in one collection/sheet/table. In that document/row, you will find its
ID, unique perhaps only in conjunction with the name of its collection/sheet/table of residence, plus the name of the
enclosing set-of-collections/sheets/tables.

In the partitioned-entities approach, an entity's attributes may be co-located with the entity in its document/row.
Relationships are expressed via "foreign keys", references to entities in other collections/sheets/tables via their IDs.
And the name of the foreign entity's collection/sheet/table of residence may not explicitly be recorded in this slot,
but rather may depend on application code or on database code that maintains schema awareness.

The partitioned-entities approach can become unwieldy with increases over time in variety -- of entities, attributes,
and relationships. When you recognize a new "kind" of entity, it could live in an existing named partition
(collection/spreadsheet/table). Your application code could then apply a predicate function over entity attributes to
say whether it's of the new kind or not. You could also cache such evaluations in a "tags" field in the document/row --
but it may be unwise to let this field grow without bound. How big can a single document/row be in your system? This
document/row-size concern also comes into play with an increasing number of attribute fields for an entity.

The new kind of entity could also live in a new named partition (collection/spreadsheet/table). With increases over time
of relationships of interest among entity types, it can become unwieldy to answer questions that span these
relationships. This is because queries will involve multiple joins that require knowing the primary residences of
entities (because their IDs are not universally unique, just within their residence namespaces) and where various
attributes live as well (i.e. the types of entities to which they "belong").

"It is hard to build robust systems: systems that have acceptable behavior over a larger class of situations than was
anticipated by their designers. The most robust systems are evolvable: they can be easily adapted to new situations with
only minor modification."[^1] There is a more robust approach to manage and query data that are likely to grow in
variety regarding types/labels/tags of entities, their attributes, and their relationships. This approach is based on a
universal relation -- one table, and one table only. In this approach, ingress is (or is isomorphic to) the RDF model
for encoding a graph of knowledge, and query/egress is (or is isomorphic to) Datalog. Databases such as Datomic, Grakn,
and TerminusDB focus on this approach, and many other databases can be configured to support it.

[^1]: Sussman, ["Building Robust
Systems"](http://groups.csail.mit.edu/mac/classes/symbolic/spring07/readings/robust-systems.pdf), from Readings for
6.891 - Adventures in Advanced Symbolic Programming, Massachusetts Institute of Technology, 2007.

{{< subscribe >}}

