---
title: "Linting for Lawmakers"
date: 2020-05-14T17:30:12-04:00
draft: false
---

Laws are rules that a particular community recognizes
as regulating the actions of its members. From this definition, Serena Peruzzo
detailed how she sought to use tools from Natural Language Processing (NLP) to
"find a representation of the rules that makes them more accessible and understandable."[^sereprz]

One proposed use case is to identify and highlight ambiguities. NLP of laws as written could help feed back
to lawmakers what parts may be confusing, where a benchmark for "confusing" could map to a
specific natural language model used by a specific dependency parser; for example,
Peruzzo used the default English model of the spaCy library's parser for her study.[^spacy] 

Challenges for such a use case include syntactic complexity -- convoluted sentences -- and
domain specificity.  This reminds me of linting for writing computer-program text.[^lint]
Many programming communities recognize certain rules as regulating the actions of their members
with regard to formatting their program text to better facilitate collaboration. Such "style guides"
are written in natural language for humans to read, but they are also accessible in representations
that allow tools to identify and highlight specific suggestions for a programmer within their
text editor.[^pep8]

Programmers are "lawmakers" in a way -- their programs pertain to control flow conditional on
 situational contexts such as program state and data values. A programmer who reads another's code may find
 certain sections ambiguous, meaning they find it difficult to predict the program behavior, and they need to
 refer to other sections of the code -- perhaps unit tests! -- to gain confidence in their mental model of the
 program's rules.

Scientific publication also involves a kind of "lawmaking" in the proposing of novel and useful
constructs for the governance of reason. A manuscript author may offer equations that
 pertain to observed behavior, or offer guidelines for interpreting specific results using specific
 assumptions. One possibility that excites me is mapping parsed graph representations
 (like that produced by spaCy's dependency parser) to candidate linked data resources. Then, inference
 could help perform "ontology linting" that nudges scientists to discover and reuse open,
 domain-specific vocabularies that in turn would enhance the discoverability of their associated ideas.

[^sereprz]: Peruzzo,
[Improving Law Interpretability with NLP](https://github.com/sereprz/improving-interpretability-with-nlp).
[csv,conf,v5](https://csvconf.com/) conference, 2020.
[^spacy]: <https://pypi.org/project/spacy/>.
[^lint]: <https://en.wikipedia.org/wiki/Lint_(software)>
[^pep8]: For example, [PEP 8](https://www.python.org/dev/peps/pep-0008/) is a style guide for Python code, and
 [flake8](https://pypi.org/project/flake8/) is a linter for PEP 8.