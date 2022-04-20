---
title: "Schemes for Indirect Control"
date: 2022-04-20T10:55:57-04:00
draft: false
tags:
- society-of-FAIR
---

There are two fundamental approaches to indirect control in code.[^eoc]

In an *open* approach, we can change the behavior of dereferencing code by conveying different values. The decision-making mechanism must be unordered. Typically, this is implemented in code using a data structure with a distinct set of keys, i.e. a *lookup table*.

In a *closed* approach, we can only change the decision-making process by changing the underlying code. A conditional, e.g. an expression that uses an `if/elif/else` or `match/case` form in Python, is closed. It is ordered, and if predicates aren't disjoint, order matters.

While an open table *conveys* values, a conditional *decides* based on values. For a table to be useful, it must avoid conflicts. Conditionals avoid conflicts by making explicit, fixed decisions. An open approach must avoid conflicts in a dynamic way.

Consider all the kinds of tricks we use to try to force ourselves to work when we're tired or distracted:

* *Willpower*: Tell yourself, "Don't give in to that," or, "Keep on trying."
* *Activity*: Move around. Exercise. Inhale. Shout.
* *Expression*: Set jaw. Stiffen upper lip. Furrow brow.
* *Chemistry*: Take coffee, amphetamines, or other brain-affecting drugs.
* *Emotion*: "If I win, there's much to gain, but more to lose if I fail!"
* *Attachment*: Imagine admiration if you succeed -- or disapproval if you fail -- especially from those to whom you are attached.

So many schemes for self-control! How do we choose which ones to use? There isn't any easy way. Self-discipline takes years to learn; it grows inside us stage by stage.

[^eoc]: Z. Tellman, *Elements of Clojure*. Monee, IL: Lulu.com, 2019.

{{< subscribe >}}