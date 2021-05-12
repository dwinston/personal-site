---
title: "Metamorphic Tests for Domain-Specific Properties"
date: 2021-05-10T08:11:49-04:00
draft: false
---

Many tests use *oracles*, where you know the answers for some inputs and you check those
correspondences.

To cover more of the input state space, you can generate random inputs and check some properties for
each corresponding output. You don't have an enumeration of exact answers like with oracles, but you
can check things like the output always being greater than zero, etc.

Sometimes, though, it's hard to assert properties of individual outputs that, across your state
space, hold for their inputs -- it may be easier to assert *output relationships* across the space.

Let's say you have a function \\(f_a\\) to compute some property of your input using method
\\(a\\), and another function \\(f_b\\) to compute that same property using method \\(b\\). Your
domain model tells you that method method \\(a\\) systematically underestimates the property value
relative to method \\(b\\), which is more accurate; you may use method \\(a\\) anyway for many inputs
because it's much more computationally efficient than method \\(b\\).

You can assert the metamorphic relation \\(f_a < f_b\\), and test on that,
even when it's hard to test via oracles or properties -- imagine in our example that it's hard to
determine output values a priori, and that it's also hard to even set upper or lower bounds on
individual outputs given their inputs.

While a lot of property-based testing highlights data-(structure-)specific properties, the positing
and testing of metamorphic relations can help you highlight domain-specific properties that hold
regardless of lower-level data representation. A good overview of metamorphic testing is
[here](https://www.hillelwayne.com/post/metamorphic-testing/), and an article on application to
testing bioinformatics programs is [here](https://doi.org/10.1186/1471-2105-10-24).

{{< subscribe >}}

