---
title: "Reasoning Lets You See What Isn't There"
date: 2022-01-21T09:46:15-05:00
draft: false
---

What is the "killer use case" for Reasoning, i.e., inferencing over a semantic graph database?

Data in a relational database "knows nothing." Data in a graph database "knows how it is connected"
-- you can ask an entity to tell you who its neighbors are 3 hops out, or if two pieces are
connected up to 20 hops. Data with Reasoning "knows how to think." But what does that mean exactly?
What do you get? What is the thing that you win by having reasoning?

Reasoning lets you see what isn’t there (yet). In a graph database without reasoning, if I am
connected to someone as my father, and someone else is connected to my father as his sister, but I
am not explicitly connected to her with a materialized edge in the graph as my aunt, I cannot ask
directly for my aunt and get a solution - I need to ask for my dad’s sister. With reasoning, I can
ask for my aunt and not care if there is a "real" edge to hop along.

Reasoning is a strategy to address a "fog of war" you may encounter in database usage, i.e. not
every fact you expect to be materialized has in fact been materialized. Reasoning is helpful
particularly when you don’t have the computational and storage resources to completely clear the
fog, i.e. materialize all possible inferences.
