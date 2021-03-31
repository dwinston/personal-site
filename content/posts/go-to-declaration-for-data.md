---
title: "Go-to-Declaration for Data"
date: 2021-03-30T15:01:17-04:00
draft: false
---

One of my favorite features of the PyCharm code editor is
[go-to-declaration](https://www.jetbrains.com/help/pycharm/navigating-through-the-source-code.html#go_to_declaration):
you can hold the control key and hover your mouse over a usage of a symbol, and you'll see a tooltip with a preview of
the declaration/definition of the symbol. Click it, and you'll jump to the definition, perhaps in another file. After
you've reviewed the definition, a keyboard shortcut gets you back to the usage point. You can do the same thing for the
type of a symbol, using shift-control instead of just control.

Other code editors have this capability, of course. It's doable because your usages of symbols unambiguously link to
their definitions. They have to, or the code wouldn't run.

Is your data structured so that you can straightforwardly provide go-to-definition links/tooltips in a web API/GUI
presenting your data? If not, how might you get there?

{{< subscribe >}}