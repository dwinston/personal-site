---
title: "Migrating Conflicts Between Agents to Higher Levels"
date: 2022-04-06T16:46:31-04:00
draft: false
tags:
- society-of-FAIR
---

Many children not only like to build, they also like to knock things down -- to hear the complicated noises and watch so many things move at once. 

Let's imagine a sibling agent to [*Builder*](https://donnywinston.com/posts/the-world-of-blocks/) called *Wrecker*, whose specialty is knocking things down:

![wrecker](https://files.polyneme.xyz/dropshare/wrecker-cRAwagc53l.png)

Suppose *Wrecker* gets aroused, but there's nothing in sight to smash. Then *Wrecker* will have to get some help -- by putting *Builder* to work, for example.

But what if, at some later time, *Wrecker* considers the tower to be high enough to smash, while *Builder* wants to make it taller still? Who could settle that dispute?

Is the decision left to *Wrecker*, who activated *Builder* in the first place? What if both were activated by a higher-level agent, *Play-with-Blocks*? What if that agent in turn was activated by a *Play* agent, who may be in conflict with *Eat* and *Sleep*?

![conflict-builder-wrecker](https://files.polyneme.xyz/dropshare/conflict-builder-wrecker-OciBzr2npH.png)

A child's play is not an isolated thing. It always happens in the context of other real-life concerns. Whatever we may chose to do, there are always other things we'd also like to do.

In single-thread, synchronous computer programming, prolonged conflict may be avoided. A function A may call another function B in its body and wait for B to return. If B encounters trouble, it can raise an exception for A to catch. The chain of command for conflict resolution can be clear.

In the case of asynchronous, independent agents like *Builder* and *Wrecker*, what is the effect of prolonged conflict? Perhaps the conflict tends to weaken their mutual superior, *Play-with-Blocks*. In turn, this could reduce *Play-with-Blocks*'s ability to suppress *its* rivals. Next, if that conflict isn't settled soon, it could weaken *Play* at the next-highest level. Then, *Eat* or *Sleep* might seize control.

*Data, data everywhere, but not a value to validate...*

{{< subscribe >}}