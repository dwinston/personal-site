---
title: "GUIs and APIs Are Both Human Interfaces"
date: 2022-04-05T11:18:11-04:00
draft: false
---

GUIs and APIs are both human interfaces. They both frame perspectives on data/operation service
offerings so that human beings can navigate and consume them. The human being in the case of APIs is
the application programmer, a subset of users. GUIs are applications, so it is natural to expect an
API’s capabilities to be a superset of a corresponding GUI’s — application programmers program the
GUI using the API.

Your resource service interface is not necessarily understandable -- discoverable, crawl-able --  by
machines. APIs are generally not machine-actionable interfaces.

Nor is it necessarily wise that a given API be made machine-actionable. This would result in a
two-audience problem. With two different target audiences, humans and machines, how could an API
serve both well?

I used to think that GUIs were for humans and APIs were for machines. I now have a SICP-esque
perspective on APIs: they "must be written for people to read, and only incidentally for machines to
execute."[^sicp]

[^sicp]: H. Abelson, G. J. Sussman, and J. Sussman, *Structure and Interpretation of Computer
Programs*, 2nd ed. MIT Press, 2002.
