---
title: "Data-Driven Programming"
date: 2020-06-25T11:03:12-04:00
draft: false
---

Data-driven programming means that you change the logic of a program
by changing data rather than code.

A good example is [statistical spam filtering](http://www.catb.org/~esr/writings/taoup/html/ch09s01.html#bayes_spam
).[^taoup]
The conventional approach is to continually update and maintain code that describes
relevant patterns to match and that implements conditional logic based on
elaborate pattern-matching. Statistical filters, on the other hand, use classification data obtained from email users
 in order to assign weights to certain words and phrases, which are in turn fed to
 the filtering algorithm.
 
Raymond notes that
> experience with statistical filters seems to show that the particular learning algorithm
 used is
 far less important than the quality of the spam and nonspam data sets from which the learning algorithm computes its
  weights. So the results of statistical filters really are driven more by the shape of the data than by the
   algorithm.

This sentiment is echoed by Halevy, Norvig, and Pereira for language models for speech recognition and translation
:[^unreasonable]
> ...invariably, simple models and a lot of data trump more  elaborate models based on less data.

A popular alternative web-page path router for React applications, the Reach Router,
[dynamically assigns](https://reach.tech/router/ranking) each registered path a
 score in order to find the best match, rather than adhering
to some hard-coded control flow, as is conventional for such routers.

Aleph, a toolkit for data search, management and analysis in investigative reporting, ingests files
in a data-driven way:[^alephep]
> the ingestors then kind of branch out, and, basically what they're doing is they're
 [auctioning](https://github.com/alephdata/aleph/blob/aa447e62430a9ff594304dabb3ab223dbd1daba9/services/ingest-file/ingestors/manager.py#L89)
 off the files, saying 'hey, I've got a file, and its filename extension is so-and-so, and this is, like, the first
  five
  bytes, who wants to parse it?' And then all the different parsers kind of go and say 'hey, I can do that.'

I think that data-driven programming can be a useful approach for user interfaces across large, growing sets of
 heterogeneous data. Conventionally, when data is added, different forms of presentation are hard-coded to replace
 old forms in order to better accommodate qualitatively more data, new data types, etc. Instead, what if
 presentation components dynamically populated an interface based on the accessible data and its underlying ontology?

[^taoup]: Raymond, *The Art of Unix Programming*. Addison-Wesley, 2003.
[^unreasonable]: Halevy, Norvig, and Pereira,
"The Unreasonable Effectiveness of Data," IEEE Intelligent Systems, 24, 2, pp. 8-12, 2009.
[^alephep]: "Entity Extraction, Document Processing, And Knowledge Graphs For Investigative Journalists with
 Friedrich Lindenberg",
 `Podcast.__init__`, [episode 189](https://www.pythonpodcast.com/aleph-with-friedrich-lindenberg-episode-186/), 2018.

