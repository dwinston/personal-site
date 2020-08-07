---
title: "The Perils of Eager Type Inference"
date: 2020-08-07T10:57:34-04:00
draft: false
---

Microsoft Excel is known to, by default, convert gene names to dates and floating-point numbers. A gene symbol like SEP2 will become '2-Sep', and an accession ID like '2310009E13' will becomes '2.31E+13'. A comment article in Genome Biology found errors like this for approximately 20% of papers in leading genomics journals with supplementary Excel files.[^1] For Excel, "there is no way to turn this off."[^2]

Type inference is helpful technology. However, it works best when it is "lazy", "late-binding". If you enter a value that might be a date and then later try to apply a function that requires a date as input, for example to extract the year or month, *then* it is quite helpful for the system to assign a date type to the value. If another function call is attempted that requires another type as input, such as a text string or a number, then that is a problem, and the system should report the inconsistency.

With good wait-and-see type inference, one needn't define a value's type up front. However, eager systems like Excel leave one with no choice but to, for example, preformat cells as Text before entering data. This is like having to declare all of your variables' types up front in a program -- a lot of people would rather not, and that gets us all into trouble when systems like Excel try to help before it's clear what help is appropriate in a given context.

[^1]: https://genomebiology.biomedcentral.com/articles/10.1186/s13059-016-1044-7 (Aug 2016)
[^2]: https://support.microsoft.com/en-us/office/stop-automatically-changing-numbers-to-dates-452bd2db-cc96-47d1-81e4-72cec11c4ed8 (accessed 2020-08-07)