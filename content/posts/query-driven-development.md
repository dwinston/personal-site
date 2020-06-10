---
title: "Query-Driven Development"
date: 2020-06-10T11:30:37-04:00
draft: false
---

You've collected a sample of important questions that you want a data system to answer.[^1]
How do you ensure the system will be able to answer those particular questions?
You might have the questions "in mind" as you design and develop a data model, process recorded observations to fit
 that model, write queries against that model, and process query results into readable answers. However, it may take
 considerable effort to translate both your questions into queries and query results into answers.
 
You can save effort by practicing wishful thinking. Imagine a query language that supports low-effort expression of your
questions and low-effort interpretation of query results. Express your queries in that language. The terms and
 constructs you use in your query expressions will naturally guide the development of the rest of the system. You can
 choose your own adventure with query languages: from off-the-shelf options such as SQL and MongoDB, to bespoke
 domain-specific languages, both programmatic (e.g., APIs and client libraries) and visual (e.g., browser-based apps).

[^1]: [The "20 Queries" Heuristic](/posts/the-20-queries-heuristic)
