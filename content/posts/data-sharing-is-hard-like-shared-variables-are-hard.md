---
title: "Data Sharing Is Hard Like Shared Variables Are Hard"
date: 2021-03-15T14:41:48-04:00
draft: false
---

If you write a program that references a variable, and that variable points to a value, you likely don't want that value
to change unless you're doing the changing. This gets tricky when you want to bring in more resources to help you get
the job done faster -- you might still be in control of the program, but the "you" in action may be multiple
cores/threads.

It can be hard and frustrating to revert to blocking and explicit hand-offs in your code: the performance gains might be
slight, or even if things run faster, your mental bandwidth in understanding more-complicated code and tracking down
subtle bugs might be significant, so is it really worth it?

Data sharing can be hard like shared variables can be hard. You want to get work done faster by bringing in more
(human + machine)
resources, and by always having up-to-date data across a collaboration, but you don't want data changing out
from under you while you're in the middle of running an analysis.

There are techniques to facilitate code concurrency on data with fewer headaches, and I think some of these techniques
can be adapted to facilitate concurrency among scientific-data collaborators.

{{< subscribe >}}

