---
title: "A Set of Patterns as a Set of Directories"
date: 2025-07-09T19:37:41+02:00
draft: false
---

What does it look like to combine these patterns: domain-driven design, test-driven development, and event-driven microservices?

First two first. Design precedes development. Design and development of what? Services. So then, what does domain-driven design look like? It looks like commits within `domain/` before commits within `services/`. And then, what does test-driven development look like? It looks like commits within `tests/` before commits within `services/`. All together now: combining domain-driven design and test-driven development looks like commits first within `domain/`, followed by commits within `tests/`, followed by commits within `services/`.

And then what does it look like to fold in the pattern of event-driven microservices? It looks like commits within `domain/events[.py|/]` before commits within `services/`, and it looks like content (so maybe you don’t need new commits each time you add domain events) within `endpoints/` to ensure that all services are independently addressable and accessible outside of a service(s)-plus-endpoint(s) host process. That is, the “micro” part looks like external processes being able to invoke services à la carte.
