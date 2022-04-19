---
title: "The Conservative Self"
date: 2022-04-18T22:00:01-04:00
draft: false
tags:
- society-of-FAIR
---

> To understand what we call the Self, we first must see what Selves are for. *One function of the Self is to keep us from changing too rapidly.*..If we changed our minds too recklessly, we could never know what we might want next. We'd never get much done because we could never depend on ourselves.

Consider Hickey's [epochal time model](https://donnywinston.com/posts/the-materials-paradigm-and-epochal-time/):

![epochal-time-model](https://files.polyneme.xyz/dropshare/epochal-time-model-JOZA7dl2S8.png)

What is the function here of Identity (i.e., the Self)? What makes a succession of states more than just a sequence of values?

Consider *identity* = *id* + *entity*. That is, an identity is a unique instance (with a primary key *id*) of an *entity* of a certain type.

What makes something an entity of a certain type? It must satisfy an [entity spec](https://docs.datomic.com/on-prem/schema/schema.html#entity-specs), i.e. maintain model invariants, including but not limited to the syntactic schema.

Can something have multiple "id-entities"? Sure. Something can be a Study with ID 123 as well as an Activity with ID 234 if (a) each value over time passes validation as both a Study and an Activity, and (b) each value over time resolves to the same unique individual within each of the Study and Activity model abstractions -- i.e., as a function of the data attributes that these models choose to consider in order to distinguish individuals, each value is a "state" of "the same" individual.

```ttl
# expression of a non-unique name assumption
study:123 owl:sameAs activity:234 .
```

To achieve conservation of id-entity, to successfully associate an id-entity -- an identity -- with a sequence of values, to proclaim that sequence to be a succession of states, is to feel confident that certain model invariants are being maintained across the values' history, that change is not reckless, that one can depend on something.

{{< subscribe >}}