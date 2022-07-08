---
title: "An Objective Function for Code Refactoring"
date: 2022-07-08T08:29:31-04:00
draft: false
---

Have you ever set an objective function for code refactoring, where, for every proposed total change
(e.g. reviewable pull request), you seek to maximize the change in this function? An example:[^img]

\\[ \log_2(pct_{LOC\\_tested})  * pct_{importables\\_documented} * pct_{LOC\\_nostate} \over n_{LOC} \\]

Good (numerator stuff):
- Percent Lines of Code (LOC) covered by a test. Sublinear growth here, i.e. diminishing returns on "getting to 100%". An off-the-shelf tool like [Coverage.py](https://coverage.readthedocs.io/) will be fine here.
- Percent "public" units, i.e. non-underscored module importables - functions, classes, constants, variables/objects, covered by [tutorial/how-to-guide/explanation (so excluding reference) documentation](https://diataxis.fr/). Maximizes code consumers' ability to understand functionality without have to dive into the codebase. Prior art on measuring this [here](https://simonwillison.net/2018/Jul/28/documentation-unit-tests/).
- Percent LOC unaffected by state (i.e. avoiding getting values from or calling methods on long-living references). Pure-functional code is easier to reason about (e.g. via a simple [substitution mode of execution](https://mitpress.mit.edu/sites/default/files/sicp/full-text/sicp/book/node10.html)) and thus more maintainable. My strategy for measuring this would be to designate certain (sub)packages/modules as purely functional.

Bad (denominator stuff):
- total LOC

What metrics correlate with code-refactoring success in your experience? These? Others?

[^img]: If the equation doesn't render for you: <img title="refactoring-objective-function" alt="refactoring-objective-function.png"
     width="80%"
     src="/img/refactoring-objective-function.png"
/>