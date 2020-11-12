---
title: "Shaping Up With Sequence Diagrams"
date: 2020-11-12T11:43:07-05:00
draft: false
---

A sequence diagram can serve as a fat-marker sketch of a happy-path checklist
for a spike.

Let's unpack that mouthful. First, the [fat-marker
sketch](https://basecamp.com/shapeup/1.3-chapter-04#fat-marker-sketches) is an
idea well-described in Ryan Singer's book [Shape
Up](https://basecamp.com/shapeup/webbook), based on software design practices at
[Basecamp](https://basecamp.com/). It's a way to roughly shape a
two-dimensional layout for a user interface when consideration of those two
spatial dimensions is essential to articulate the intended user
experience.

[Breadboarding](https://basecamp.com/shapeup/1.3-chapter-04#breadboarding),
another shaping technique discussed in the book, narrows focus to three design
elements: *places*, *affordances*, and *connection lines*. Each place has
affordances, and connection lines show how affordances take a user from place to
place. Whereas fat-marker sketching addresses spatial concerns,
breadboarding narrows focus to logical concerns only.

A [sequence diagram](https://en.wikipedia.org/wiki/Sequence_diagram) can be
rough like breadboarding, with a focus on connection lines among places, where
the "places" are participants/actors. The connection lines in such a diagram
are the arrows between lifelines. Consider these arrows as items on a checklist,
so that the arrow labels are checklist-item labels.

A sequence diagram rises to the level of a fat-marker sketch when considering
dimensionality. Fat-marker sketches deal with the two spatial dimensions on a
user's screen. With sequence diagrams, there is one logical dimension -- the
identity of a participant/actor process, which may be physically in the same
"place" as another participant/actor or not -- and one temporal dimension, that
of [epochal
time](https://github.com/matthiasn/talk-transcripts/blob/9f33e07ac392106bccc6206d5d69efe3380c306a/Hickey_Rich/AreWeThereYet.md#user-content-slide-31).

Overall, a sequence diagram may be read as detailing a single path, e.g. a
"happy path" for a core use case, through the effective
[statechart](https://statecharts.github.io/) of the system as a whole. The
result of building out this whole-system ("end-to-end") use case, of [geting one
integrated slice
done](https://basecamp.com/shapeup/3.2-chapter-11#integrate-one-slice), is known
as a [spike](https://wiki.c2.com/?SpikeSolution).

Thus, a sequence diagram can serve as a fat-marker sketch of a happy-path
checklist for a spike, with each labeled arrow corresponding to an item to
implement and check off.

[Here are a few example sequence
diagrams](https://github.com/polyneme/maggtomic/blob/f632832dafc01184beccb225f8b0a600c46bda6e/README.md#sequence-diagrams-for-use-case-happy-paths)
that I used to shape up some imagined spikes for a project I'm working on now. I
made the diagrams with [this browser-based
tool](https://www.websequencediagrams.com/). Let me know if you find this
framing of sequence diagrams helpful in your work.