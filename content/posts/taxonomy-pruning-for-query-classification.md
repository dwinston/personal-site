---
title: "Taxonomy Pruning for Query Classification"
date: 2022-07-14T13:39:05-04:00
draft: false
---

When providing a search interface ([F4](https://w3id.org/fair/principles/terms/F4)), you can improve
[precision](https://en.wikipedia.org/wiki/Precision_and_recall#Precision) significantly by
classifying a user's query, assuming you are able to classify your content.

If you have a category taxonomy and labeled queries, you can train a classifier in order to
dynamically assign a category to a query. A benefit of taxonomic hierarchy is that, while a labeled
query may be labeled with a leaf node of the taxonomy, you can prune, i.e. "roll up", the taxonomy
to ensure sufficient signal for training. This helps to maintain
[recall](https://en.wikipedia.org/wiki/Precision_and_recall#Recall) when filtering query results by
the query's classification.