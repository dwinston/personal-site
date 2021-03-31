---
title: "Version Control for Data"
date: 2021-03-10T14:36:58-04:00
draft: false
---

Git is the common tool for version control of code. How does it work? It works by grouping events about lines. Lines are
added or removed, and a group of add/remove events is a transaction, i.e. a "commit". A sequence of these
line-delta-group events can be replayed from the log to construct a snapshot of the codebase at any point in the commit
history.

Replaying a totally ordered log to construct a snapshot of state, i.e. state machine replication (aka "event sourcing"),
is an increasingly popular practice in distributed data systems. Git does this for line-delta encodings of collections
of text files, i.e. the stream of atomic changes to your codebase. Too bad your database isn't a set of files of
plaintext lines.

What is your database a set of? Can you delta-encode atomic changes to that set?

Documents and tables can be represented as graphs  -- sets of edges, with each edge connecting two nodes. Thus, an edge
could be the equivalent of a line. Shards of a graph (or separate named graphs) could be the equivalent of files. An
edge ledger, an accounting of the assertion and retraction of edges, could be the log, with atomic commits of sets of
edge events.

Databases like Datomic and TerminusDB do this today. Pervasive version control for data could enable scientists to more
unambiguously cite a dataset (e.g. as the result of query Q pointed at commit C of data repository R) and to collaborate
without fear on data repositories ("Oops, I messed up, let's undo that last data commit. Here's an updated commit.
Great, now the data passes the automated tests -- let's push an official release.").

{{< subscribe >}}