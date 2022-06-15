---
title: "PageRank of Linked Open Vocabularies (LOV)"
date: 2022-06-15T13:28:17-04:00
draft: false
---

Datasets are easier to reuse if they use standards that are well-established, particularly in a given domain.

A first approach is to ask around -- ask people with whom you coauthor , people you trust in your field, etc.

A follow-on approach is to examine the "graph reputation" of relevant standards, particularly if they may be represented as resources with outbound links. We can use the PageRank algorithm, just like Google uses it to index the web of documents.

An an example, here I outline an initial approach to find the "most reputable" of [Linked Open Vocabularies'](https://lov.linkeddata.es/) 778 vocabularies.

My starting point is having the API responses for each vocabulary so that `lov` is a list of `dict`s, each with keys `url: str` and `api_response: dict`.

1. Collect all outbound links:
```python
for entry in lov:
    entry["outbound_links"] = entry.get("outbound_links", set())
    for version in entry["api_response"].get("versions", {}):
        for field, value in version.items():
            if field.startswith("rel") and isinstance(value, list):
                entry["outbound_links"] |= {v for v in value}
```
2. Prepare a stream of self_link, outbound_link pairs:
```python
with open("lov-outlinks.csv",'w') as f:
    for entry in lov:
        url = entry["url"]
        for link_url in entry["outbound_links"]:
            f.write(f"{url},{link_url}\n")
```
3. In a file, e.g. `lov_pagerank.py`:[^1]
```python
if __name__ == "__main__": # for `spark-submit`
    sc = SparkContext(appName="LovRankings")
    match_data = sc.textFile("lov-outlinks.csv")

    xs = match_data.map(get_linking).groupByKey().mapValues(initialize_for_voting)

    for i in range(20):
        if i > 0:
            xs = sc.parallelize(zs.items())
        acc = dict(xs.mapValues(empty_ratings).collect())
        zs = xs.aggregate(acc, allocate_points, combine_ratings)

    ratings = [(k, v["rating"]) for k, v in zs.items()]
    for i, (vocab, rating) in enumerate(
        sorted(ratings, key=lambda x: x[1], reverse=True)[:100]
    ):
        print("{:3}\t{:6}\t{}".format(i + 1, round(log2(rating + 1), 1), vocab))
```
where, above it:
```python
from math import log2
from pyspark import SparkContext
from toolz import assoc


def get_linking(line):
    return line.split(",")


def initialize_for_voting(outlinks):
    return {"outlinks": outlinks, "n_outlinks": len(outlinks), "rating": 100}


def empty_ratings(d):
    return assoc(d, "rating", 0)


def allocate_points(acc, new):
    _, v = new
    boost = v["rating"] / (v["n_outlinks"] + 0.01)
    for link in v["outlinks"]:
        if link not in acc.keys():
            acc[link] = {"outlinks": [], "n_outlinks": 0}
        link_rating = acc.get(link, {}).get("rating", 0)
        acc[link]["rating"] = link_rating + boost
    return acc


def combine_ratings(a, b):
    for k, v in b.items():
        try:
            a[k]["rating"] = a[k]["rating"] + b[k]["rating"]
        except KeyError:
            a[k] = v
    return a
```
And here is the output of `spark-submit lov_pagerank.py`:
```
  1       10.6  http://purl.org/dc/elements/1.1/
  2       10.3  http://www.w3.org/2000/01/rdf-schema#
  3       10.3  http://www.w3.org/1999/02/22-rdf-syntax-ns#
  4        9.0  http://www.w3.org/2004/02/skos/core#
  5        8.9  http://purl.org/dc/terms/
  6        6.3  http://xmlns.com/foaf/0.1/
  7        6.3  http://www.w3.org/2002/07/owl#
  8        6.3  http://purl.org/dc/dcmitype/
...
```
We can see at a glance the "most reputable" vocabularies, and they don't surprise me. What may be more helpful is to collect candidate vocabularies for your domain and focus on their relative scores in order to gauge whether any are "well-established" in a sense. Even more helpful may be to include multiple "types" of resources -- with standards linking to and being linked from various databases and policies. [FAIRSharing](https://fairsharing.org/) seems like it could eventually support open investigation of the latter kind.

[^1]: Adapted from J. T. Wolohan, *Mastering large datasets with Python: parallelize and distribute your Python code*. Shelter Island, NY: Manning Publications Co, 2019.

{{< subscribe >}}