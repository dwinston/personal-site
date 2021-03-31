---
title: "A CSV File That Knows Its Schema and Context"
date: 2021-03-23T14:50:31-04:00
draft: false
---

Have you ever given or gotten data as CSV? Are the meanings of the columns always clear? How are they made clear? Are
the given column labels/names and the given file/sheet names always enough?

If additional information beyond the CSV file is needed, how is that facilitated? A separate README file that travels
with the CSV as part of a zipped archive file? What happens when the archive is unzipped and the CSV gets shared via
email without the README also attached? Whoops.

It's hard to keep data together with its schema and context. Links help. It's great when a scientific article links out
to references via unambiguous DOIs. It's great when a web page with an embedded data table links out to another web page
for more context.

JSON-LD makes JSON data Linked Data. What would "CSV-LD" look like?

The term "CSV-LD" was previously used to describe a [now-obsoleted precursor](https://github.com/gkellogg/csv-ld) to the
[CSV on the Web (CSVW) metadata specifications](https://www.w3.org/2013/csvw/wiki/Main_Page); both approaches require a
second file, a JSON-LD template document, to be shared along with a CSV file.

I'm preparing a talk for [csv,conf](https://csvconf.com/) in May about an approach that, in contrast, requires only a
CSV file from the data producer, one that includes links to CSVW-powered metadata. It is primarily intended to be a way
to use Linked Data as part of spreadsheet-based data entry; to facilitate data validation, display, and conversion of
CSV into other formats via use of CSV on the Web (CSVW) metadata; and to build FAIR data services.

{{< subscribe >}}
