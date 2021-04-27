---
title: "Statecharts as a Logic of Effects"
date: 2021-04-27T12:07:36-04:00
draft: false
---

Do your programs only compute pure *functions* of data, or do they also perform *effects* such as
dynamically reading input, writing output, transitioning database state, making network requests,
etc.?

One sense of the term "logic" is as a general subject, i.e. the study of how to draw valid
conclusions. Another sense is as a particular language, i.e. ***a logic*** for representing
information along with a set of inference rules that specify exactly what conclusions can be drawn
from what premises.

To ensure the reliability of your functions and of your data at rest, you may use type annotations,
assertions, database system affordances such as schema declarations, etc. Ideally, these tools help
you express both your domain logic and your application-specific logic.

Statecharts[^harel] are a formal extension of finite state machines for modeling stateful, reactive
systems. Extensions include guarded transitions, managed effects, extended state (context),
orthogonal (parallel) states, and hierarchical (nested) states. The formalism has been standardized
as [SCXML](https://www.w3.org/TR/scxml/). [XState](https://xstate.js.org/docs/) is a popular
implementation that adheres to SCXML while providing a JSON syntax and execution via
JavaScript/TypeScript.

Statecharts help to ensure a logic of effects. Effects are managed and executed by the system; you
needn't execute them within your functions, i.e. as "side-effects" of a function's transformation of
input to output. In the taxonomy of statechart effects, there are "fire-and-forget" effects such as
*actions* and *activities*, as well as "invoked" effects such as *promises*, *callbacks*,
*observables*, and other *machines* that can send and receive events to/from the invoking
statechart.

Crucially, a statechart interpreter cancels the execution of / discards the results of effects when
there is a finite state transition -- this logic is managed by the system. And unlike finite state
machines, a statechart can have "extended state", i.e. context. In other words, you can have an
"infinite" state space as long as you carve your universe of state into a finite number of
partitions; you might say that a statechart is a partitioned-state machine. This partitioning
facilitates a logic of managed effects.

[^harel]: Harel, David. “Statecharts: A Visual Formalism for Complex Systems.” Science of Computer
Programming 8, no. 3 (June 1, 1987): 231–74. [https://doi.org/10/b97n8k](https://doi.org/10/b97n8k).

{{< subscribe >}}