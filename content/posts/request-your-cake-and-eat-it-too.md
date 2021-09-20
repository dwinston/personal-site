---
title: "Request Your Cake and Eat It Too"
date: 2021-09-20T14:04:24-04:00
draft: false
tags:
- code
---

I was alerted to a great discussion[^rcthread] about unifying versus partitioning data models. That
is, you have some data powering some part of your system, and you need to decide how to structure
that data and associate validation logic and behavior -- like calculating properties or triggering
other system actions -- with the bundle of data as it evolves over the course of some ongoing or
completing process.

The concrete example given is an application with a `/cakes` endpoint. You might `POST` a JSON
object to it with `{name,ingedients,inventor_id}` attributes, and get back a JSON object with
`{name,ingredients,id,status}` attributes. When you create a cake, the cake doesn't have an `id` in
the system, and it doesn't have a system `status`, e.g. "baking". Also, there may be cake attributes
that aren't assumed to be relevant in a response, e.g. a system ID for the cake's inventor.

Approaches to data modeling here include (1) having e.g. a `CreateCakeRequest` model for the `POST`
body and a `CreateCakeResponse` model for the response, and (2) having one `Cake` model that gets
passed around and updated. The former approach is one of partitioning and hand-off. The latter is
one of unifying the state space into a single data structure.

There are two other approaches I've seen and implemented that I guess technically take approach (2),
but also dispatch to approach (1) "under the hood". One tries to be principled and explicit about
the under-the-hood partitioning, and the other ~~just kinda wings it~~ emphasizes
flexibility.

The principled, explicit-partitions approach is exemplified by
[statecharts](/posts/statecharts-as-a-logic-of-effects/) in that your data model is a unified
"machine". Below I show a little Python pseudocode that reflects
[XState](https://xstate.js.org/docs/)'s JSON representation of a model. There is a privileged data
attribute called `state` that the machine runtime uses as a switch in order to respond to incoming
events/requests of the model. In this way, the "one" model dispatches to finitely many little
models, all of which have access to the `context` structure.

```python
create_machine({
    "id": "cake-machine",
    "initial": "emptiness",
    "context": {
        "inventor_id": None,
        "ingredients": [],
        "name": None,
        "cake_id": None,
    },
    "states": {
        "emptiness": {
            "on": {
                "CREATE": {
                    "target": "baking",
                    "actions": assign({
                        "inventor_id": "set_inventor_id",
                        "name": "set_name",
                        "ingredients": "set_ingredients",
                        "id": "set_id",
                    }),
                }
            }
        },
        "baking": {
            "on": {
               1800: {  # 30 minutes (30 * 60 seconds)
                   # ... check on cake ...
               } 
            }
        }
    }
}, {
    "actions": {
        "set_inventor_id": lambda context, event: event.inventor_id,
        "set_name": lambda context, event: event.name,
        "set_ingredients": lambda context, event: event.ingredients,
        "set_id": lambda _c, _e: generate_cake_id(database),
    }
})
```

A similar explicit-partitions approach is customary for Elm applications, where a unified model is
fed along with a message, i.e. an event/request, to a unified update function that again uses case
analysis to switch on the appropriate subspace of logic. In statecharts, the switch is on the state
attribute, whereas for Elm logic, the switch can be two-staged on the message type or model variant,
as both may be custom tagged-union types that are simple to switch on.

A less partition-oriented yet flexible approach is exemplified by the use of models that
cast/conform input data to their own little worlds and yet get persisted to the same underlying
unified data structure. I took this approach recently in implementing a superset of the Global
Alliance for Genomics and Health's (GA4GH) [Data Repository Service (DRS)
API](https://ga4gh.github.io/data-repository-service-schemas/preview/release/drs-1.0.0/docs/) in
Python using [Pydantic](https://pydantic-docs.helpmanual.io/) and
[FastAPI](https://fastapi.tiangolo.com/).

In the GA4GH DRS API, a
[`DrsObject`](https://ga4gh.github.io/data-repository-service-schemas/preview/release/drs-1.0.0/docs/#_drsobject)
is the central resource. It tells you about some bytes you can access somehow, like via a URL. Since
I added endpoints to create such objects and to tag them with "types" that are outside the scope of
the current API spec, I needed to have different models that present different interfaces to the
same underlying data, like a bunch of people all having different perspectives when standing around
an elephant. Pydantic helped with this because you can pass in extra fields to a model constructor,
and it simply ignores the extras. And FastAPI helped because you can assign Pydantic models to API
request and response objects per endpoint, which means I can yield the whole enchilada from an
endpoint function and FastAPI will feed it to the registered Pydantic response model to be slimmed
down / conformed for the client as per the OpenAPI contract.

Concretely, I have `DrsObjectBase`, `DrsObjectIn(DrsObjectBase)`, and `DrsObject(DrsObjectIn)`
Pydantic models ([code
here](https://github.com/microbiomedata/nmdc-runtime/blob/67c38b6ed1fcaa02417734eafd814d1fc3abc1e5/nmdc_runtime/api/models/object.py))
that power a family of FastAPI `/objects` endpoints ([code
here](https://github.com/microbiomedata/nmdc-runtime/blob/67c38b6ed1fcaa02417734eafd814d1fc3abc1e5/nmdc_runtime/api/endpoints/objects.py)),
and complementary `/object_types` models
([code](https://github.com/microbiomedata/nmdc-runtime/blob/67c38b6ed1fcaa02417734eafd814d1fc3abc1e5/nmdc_runtime/api/models/object_type.py))
and endpoints
([code](https://github.com/microbiomedata/nmdc-runtime/blob/67c38b6ed1fcaa02417734eafd814d1fc3abc1e5/nmdc_runtime/api/endpoints/object_types.py)).
All of the coordinated models (including validation via Pydantic `@*validator`-decorated methods)
and representational state transfer facilitated by the API are backed by a MongoDB collection that
stores one JSON object per `DrsObject`, including an embedded array of `types` that is shielded from
the read-only, spec-adhering DRS API endpoints.

Would I be better off with a partition-oriented data modeling approach for the DRS API
implementation? I'm not sure. In any case, it would need to be done "under the hood", e.g. with a
`_state` attribute or similar on the underlying MongoDB document in my case.

[^rcthread]: [Topic](https://recurse.zulipchat.com/#narrow/stream/18957-programming/topic/Thinking.20about.20data.20model)
on the [Recurse Center](https://www.recurse.com/)'s Zulip realm. Private to Recursers, but if this
post interests you, consider applying for a batch! Ping me if you have any questions.