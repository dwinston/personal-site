---
title: "A JSON File That Knows Its Schema and Context"
date: 2021-03-19T14:48:29-04:00
draft: false
---

If you provide JSON, either as files or as API responses, you might be one step away from ensuring that anyone
encountering that JSON has a portal to what it means. This step is to provide a single extra key-value pair in each JSON
document -- the key is "@context", and the value is a URL.

JSON-LD is "a JSON-based format to serialize Linked Data. The syntax is designed to easily integrate into deployed
systems that already use JSON, and provides a smooth upgrade path from JSON to JSON-LD. It is primarily intended to be a
way to use Linked Data in Web-based programming environments, to build interoperable Web services, and to store Linked
Data in JSON-based storage engines."[^1]

You don't necessarily have to provide comprehensive definitions of your JSON fields if someone else has already done a
good job. There are ways to provide formal "[crosswalks](https://en.wikipedia.org/wiki/Schema_crosswalk)" from your
field names to the names that others use.

[^1]: https://w3c.github.io/json-ld-syntax/

{{< subscribe >}}