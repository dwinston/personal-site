---
title: "Lean Web - Principles of Lean Thinking applied to Web Development"
date: 2022-06-09T12:28:09-04:00
draft: false
---

[Lean manufacturing](https://en.wikipedia.org/wiki/Lean_manufacturing) aims to reduce waste in
production processes and to reduce response times to consumers from producers.

Womack and Jones[^1] authored five key principles for lean thinking in the context of manufacturing:

1. _Value_: Identify the value of a product to a consumer.
2. _Value Stream_ - Identify the minimal process (steps, time, information, material) to produce the value.
3. _Flow_: Make production flow through the steps.
4. _Pull_: Pull between the steps (rather than pushing intermediate "inventory" that may not be used).
5. _Perfection_: Reduce the number of steps and the amount of time, information, and material needed for production.

[Lean software development](https://en.wikipedia.org/wiki/Lean_software_development) aims to adapt
lean thinking to software development.

The Poppendiecks[^2] authored seven principles that don't directly provide qualified references to
Womack and Jones' principles. Here, I attempt to align their principles of software development to
the framework and terminology of Womack and Jones's lean thinking principles:

1. _Evaluate Late_: Decide on the end-value of a product to a consumer as late as possible. There is
   one value stream option per end-value option.

2. _Mind Value Stream Multiplicity and Looping_: With one value stream per end-value hypothesis, can
   value streams share structure to eliminate waste? Value streams may have loops (iterations) that
   must be particularly lean to support a high learning rate.

3. _Flow_: Make production flow for fast delivery and thus for rapid learning given the presence of
   loops in a value stream.

4. _Pull_: Pulling between steps empowers the team.

5. _Perfection_: Continuous refactoring facilitates ensuring integrity and optimizing the whole.


Now, I can couch a conceptualization of lean principles for web development, i.e. Lean Web
principles, with clear lineage to the lean thinking principles for manufacturing and through lean
principles for software development:

1. _Evaluate Resources Late_: Deal in data for as long as possible. Apply transformation logic later
   -- there are many applications. Apply presentation logic even later -- there are many modes of
   consumption for an application. See also: Perlis' epigram[^perlis]: "Functions delay binding;
   data structures induce binding. Moral: Structure data late in the programming process."

2. _Mind Value Stream Multiplicity and Looping_: Eliminate waste in process steps, time, information
   (configuration / manual signaling), and material (code, data, storage/compute infrastructure).
   Can web dev processes share logic? Pay particular attention to waste in value stream loops
   (iterations).

3. _Flow_: Choose continuous integration (CI) and continuous deployment (CD).

4. _Pull_: Choose distributed version control for code, data, and storage/compute
   infrastructure (as code).

5. _Perfection_: Can it all fit in your head, to facilitate conceptual integrity and strategic
   refactoring?

Finally, I am well aware of [Chris Ferdinandi](https://gomakethings.com/about/) and his excellent
exposition on [Lean Web thinking](https://leanweb.dev/) and associated [three
principles](https://leanweb.dev/ebook/lean-web-principles/). Here's how I think his principles may
map to those above:

1. _Embrace the Platform_: This relates to evaluating resources late. Can you exchange data as RDF
   (e.g. serialized as JSON-LD) over HTTP? Can you exchange logic for inference and validation as RDF
   data as well, via the RDFS/OWL and SHACL standards of the Web platform? Can you exchange logic for
   presentation as HTML (templates) and CSS? If your front-end requires operational processes, can that
   be done using vanilla JavaScript?

2. _Small and Modular_: This relates to minding value stream multiplicity and looping. There is a
   lot of opportunity to eliminate waste and reuse functionality (especially functionality provided by
   the platform!).

3. _The Web is for Everyone_: This relates to evaluating resources late (why prematurely optimize
   for applications and consumption use cases and thus exclude potential stakeholders?) and pulling
   (empower people by encouraging them to pull rather than telling them to pick up whatever is pushed).

[^1]: J. P. Womack and D. T. Jones, *Lean thinking: banish waste and create wealth in your corporation*. New York, NY: Simon & Schuster, 1996.

[^2]: M. Poppendieck and T. Poppendieck, *Lean software development: an agile toolkit*. Boston: Addison-Wesley, 2003.

[^perlis]: A. J. Perlis, “Special Feature: Epigrams on programming,” SIGPLAN Not., vol. 17, no. 9,
pp. 7–13, Sep. 1982, doi: 10.1145/947955.1083808. Online at
<http://www.cs.yale.edu/homes/perlis-alan/quotes.html>.
