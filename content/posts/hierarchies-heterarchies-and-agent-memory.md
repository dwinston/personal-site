---
title: "Hierarchies, Heterarchies, and Agent Memory"
date: 2022-04-10T10:34:01-04:00
draft: false
tags:
- society-of-FAIR
---

In a hierarchy, each agent only acts on behalf of one other agent:

```python
from rdflib import Graph
from rdflib.namespace import RDF, PROV

def hierarchy(graph):
    return all(
        len(set(graph.objects(agent, PROV.actedOnBehalfOf))) <= 1
        for agent in graph.subjects(RDF.type, PROV.Agent)
    )

hierarchy(Graph().parse(data="""
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix :     <http://example.com/> .

:doc
    a prov:Agent;
.

:sleepy
    a prov:Agent;
    prov:actedOnBehalfOf :doc;
.

:sneezy
    a prov:Agent;
    prov:actedOnBehalfOf :doc;
.

""")) # True
```

Hierarchies do not always work. Sometimes, for example, agents need to use each other's skills:

```python
def heterarchy(graph):
    return not hierarchy(graph)

heterarchy(Graph().parse(data="""
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix :     <http://example.com/> .

:doc
    a prov:Agent;
.

:sleepy
    a prov:Agent;
    prov:actedOnBehalfOf :sneezy, :doc;
.

:sneezy
    a prov:Agent;
    prov:actedOnBehalfOf :sleepy, :doc;
.

""")) # True
```

In heterarchies, per-agent working memory becomes critical: an agent must keep track of what next to do in a job A if it starts a job B before A is done. In hierarchies, priority and preemption can straightforwardly waterfall down from the top supervisor.

{{< subscribe >}}