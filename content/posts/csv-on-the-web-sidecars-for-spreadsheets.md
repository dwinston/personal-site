---
title: "CSV on the Web: Sidecars for Spreadsheets"
date: 2021-04-14T10:46:35-04:00
draft: false
---

If you share data on the web as delimiter-separated values -- that is, as spreadsheets -- there is a
world of power-ups available to you.

The term "sidecar" is used for a functional addition. A motorcycle sidecar can carry things and
people. A Kubernetes sidecar container has access to the namespace and storage volumes of it's pod's
main container, and so supports auxiliary work. Unstructured documentation, e.g. a typical README
file, is not a sidecar.

The W3C's "CSV on the Web" (CSVW) working group published [seven
documents](https://github.com/w3c/csvw), including [a note on 25 identified use
cases](https://www.w3.org/TR/2016/NOTE-csvw-ucr-20160225/) and [a
primer](https://www.w3.org/TR/2016/NOTE-tabular-data-primer-20160225/) on effective use of its
recommendations in practice. In the simplest case, when you're serving a csv file like `mydata.csv`,
you also serve a JSON sidecar by adding `-metadata.json` to the name (e.g.
`mydata.csv-metadata.json`), and you use the CSVW vocabulary to provide extra information about your
data.

There are limits to the logic you can express using the CSVW vocabulary, and this is reasonable (cf.
the ["rule of least power"](https://www.w3.org/2001/tag/doc/leastPower.html))! The Shapes Constraint
Language (SHACL) vocabulary extends expression of logic to [JavaScript
functions](https://www.w3.org/TR/2017/NOTE-shacl-js-20170608/#h-js-functions) (Python functions seem
doable...) -- this could help to transform a spreadsheet's cell values to conform to a desired
schema.