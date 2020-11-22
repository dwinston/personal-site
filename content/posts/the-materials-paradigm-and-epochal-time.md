---
title: "The Materials Paradigm and Epochal Time"
date: 2020-11-22T08:26:16-05:00
draft: false
---

The materials paradigm[^paradigm_defn] may be represented in the form of a tetrahedron[^wikipedia],
illustrating a set of material concerns and how they are interrelated.

<a target="_blank" href="https://commons.wikimedia.org/w/index.php?curid=4198116">
<img width="90%" src="/img/materials_science_tetrahedron;structure,_processing,_performance,_and_proprerties.svg" alt="The materials science tetrahedron, which illustrates how a material's properties, processing, performance, and structure are interrelated. Source: <https://commons.wikimedia.org/w/index.php?curid=4198116>.">
</a>
<br><em>The materials science tetrahedron, which illustrates how a material's properties, processing, performance, and structure are interrelated (<a href="https://commons.wikimedia.org/w/index.php?curid=4198116">source</a>).</em>
<br><br>

What *is* a "material"? There is no label for it in the diagram above. And what
is the nature of the relationships among properties, processing, performance,
structure, and characterization in the diagram above? From the diagram, each
"edge" connecting "nodes" is indistinct -- it seems that everything connects to
everything else in the same way, except for characterization, which is a thing
that just floats in the middle, geometrically equidistant from every node in the
fully connected graph.

In *Process and Reality*, Whitehead elaborates on an epochal theory of
time[^whitehead], for which Hickey produced a useful diagram[^arewethereyet]
as part of his work to apply this model to programming language design. I
believe this diagram can be usefully related to that of the materials
paradigm tetrahedron. 

<a target="_blank" href="https://github.com/matthiasn/talk-transcripts/blob/9f33e07ac392106bccc6206d5d69efe3380c306a/Hickey_Rich/AreWeThereYet.md#user-content-slide-31">
<img src="/img/hickey_are-we-there-yet_epochal-time-model.jpg" width="100%"
alt="Epochal time model, from Rich Hickey's \"Are We There Yet\" talk."></a>
<br><em>Epochal time model, from Rich Hickey's "Are We There Yet" talk (<a href="https://github.com/matthiasn/talk-transcripts/blob/9f33e07ac392106bccc6206d5d69efe3380c306a/Hickey_Rich/AreWeThereYet.md">transcript</a>).</em>
<br><br>

Consider a given material structure as a *value*, an unchanging thing, as
opposed to a *variable*. Consider that this unchanging thing, this
structure-as-value, may be observed/perceived/remembered in a manner that does
not change it, that does not change the structure -- this is characterization.

Now, consider an event that, when it "happens" to a structure, when it applies
to a structure, results in a different structure, i.e. a different value is
observed after the event -- this is processing. Processing is a function
that takes one value to another value, one structure to another structure.

What, then, is a "material"? A material is a post hoc composition of structure
values, an identity *assigned* to a succession of values related by successive
processing events. A structure-as-value is associated with a
material-as-identity, and a value assigned to an identity may be termed a
"state" of that identity. The conceptually synthesized identity, the material,
"has" states, and through characterization, through observation/perception, a
state "has" *properties*. A property is an output value of a characterization
process that takes a structure as an input value.

What is perceived from a value may be termed a property of the value, and if the
input value is associated with an identity, the perception may be thought of as
a property of a state of the identity, or alternatively as a property of the
identity at a given moment in time, i.e. at a given state. Thus, a "material
property" is a characterization of one or more distinct structures identified as
a material via an epochal succession of processing events. When a material
"changes" via processing, its properties may "change" as well because the
observed properties depend on structures, on values, on "states" of a
"material", not on the post hoc material-as-identity.

In this model, time is not a continuously running clock. Time happens in
discrete steps, epochs, one-to-one with events that represent the processing of
values. A "state" is a snapshot, a material-as-identity's structure-as-value at
a given "moment"[^moment] "in time". This state is customarily extended by
idempotent characterization of that structure's properties-as-values.

Finally, what is material performance in terms of the epochal time model? Like
processing, which is a function taking one structure value (a material state) to
another structure value, and like characterization, which is also a function
taking one structure value to one or more property values, performance is a
function as well. Performance is a comparator that takes as input (a) some
assembly of a material's values (snapshot perceptions of selected states), and
(b) a collection of corresponding assemblies from other "materials" deemed
relevant for comparison, and outputs a value for performance as perceived
(characterized) by the function.

Just as the epochal time model was productively applied to the design and
implementation of the Clojure programming language, I hope that this model
as mapped to the elements of the materials-paradigm tetrahedron above can
be productively applied to the design and implementation of [materials research
management systems](/posts/headless-mrms/).

[^arewethereyet]: Rich Hickey. "Are We There Yet?", presented at the JVM Languages Summit, 2009 (<a href="https://github.com/matthiasn/talk-transcripts/blob/9f33e07ac392106bccc6206d5d69efe3380c306a/Hickey_Rich/AreWeThereYet.md">transcript</a>).
[^paradigm_defn]: par·a·digm (noun) - "a philosophical and theoretical framework of a scientific school or discipline within which theories, laws, and generalizations and the experiments performed in support of them are formulated". From <https://www.merriam-webster.com/dictionary/paradigm>, accessed 2020-11-22.
[^wikipedia]: <https://en.wikipedia.org/wiki/Materials_science>, accessed 2020-11-22.
[^whitehead]: Alfred North Whitehead, *Process and Reality: An Essay in Cosmology* (1929). Cambridge University Press.
[^moment]: Some evidence that the notion of a moment indicates epochal movement/processing: "contraction of *movimentum*, from *movere* "to move" (from Proto-Indo-European root *meue-*, 'to push away')." From <https://www.etymonline.com/word/moment>, accessed 2020-11-22.