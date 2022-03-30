---
title: "Components and Connections"
date: 2022-03-30T15:05:42-04:00
draft: false
tags:
- society-of-FAIR
---

An agent like *Builder* is not merely a collection of parts like *Find*, *Get*, *Put*, and all the rest. *Builder* would not work at all unless those agents were linked to one another by a suitable network of interconnections:

![agents-by-themselves-and-in-bureaucracy](https://files.polyneme.xyz/dropshare/agents-by-themselves-and-in-bureaucracy-WDrJoLTNjp.png)

Could you predict what *Builder* does from knowing just that left-hand list above? Of course not. First, we must know how each separate part works. Second, we must know how each part interacts with those to which it is connected. And third, we have to understand how all these local interactions combine to accomplish what that system *does* -- as seen from the outside.

There is lots of prior art for understanding combinations of component interactions, whether as expression trees or wiring diagrams. Computer programming has traditionally emphasized the former, but note how *Move* has two "parents" in the diagram above.

I leave you with the intro to the last chapter of [^1]:

> Decades of programming experience have taken a toll on our collective imagination. We come from a culture of scarcity, where computation and memory were expensive, and concurrency was difficult to arrange and control. This is no longer true. But our languages, our algorithms, and our architectural ideas are based on those assumptions. Our languages are basically sequential and directional -- even functional languages assume that computation is organized around values percolating up through expression trees. Multidirectional constraints are hard to express in functional languages.
 
> ### Escaping the Von Neumann straitjacket
> The propagator model of computation provides one avenue of escape. The propagator model is built on the idea that the basic computational elements are propagators, autonomous independent machines interconnected by shared cells through which they communicate. Each propagator machine continuously examines the cells it is connected to, and adds information to some cells based on computations it can make from information it can get from others. Cells accumulate information and propagators produce information.

> Since the propagator infrastructure is based on propagation of data through interconnected independent machines, propagator structures are better expressed as wiring diagrams than as expression trees. In such a system partial results are useful, even though they are not complete. For example, the usual way to compute a square root is by successive refinement using Heron's method. In traditional programming, the result of a square root computation is not available to subsequent computations until the required error tolerance is achieved. By contrast, in an analog electrical circuit that performed the same function, the partial results could be used by the next stages as first approximations to their computations. This is not an analog/digital problem—it is organizational. In a propagator mechanism the partial results of a digital process can be made available without waiting for the final result.

[^1]: C. Hanson and G. J. Sussman, Software design for flexibility: how to avoid programming yourself into a corner. Cambridge: The MIT Press, 2021.

{{< subscribe >}}