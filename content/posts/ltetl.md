---
title: "L⁻¹T⁻¹ETL"
date: 2021-07-23T13:13:34-04:00
draft: false
---

A lot of extract-transform-load (ETL) work requires unloading and un-transforming first. Rather than
\\(ETL\\), it's \\(L_A^{-1}T_A^{-1}ET_BL_B\\). What the data provider did is \\(A\\). What you want
to do is \\(B\\).

The data provider gave you a "dump" of their data. You don't know what it means. If you did, you
could extract (subset) from it according to your needs -- filter entities by some meaningful
criteria and collect selected attributes.

They had data in some intelligible form, extracted what they needed at the time, transformed it for
input to a processing/analysis system, and loaded the transformed extraction into that system. And
now you have an export from that system.

So, you need to reverse their loading and then their transforming (cf. "data munging/wrangling") in
order to align it to your conceptual model. Only then can you extract from it, subset it according
to your present needs. Then, you want to process/analyze it efficiently, so you transform it
according to the logical/external model of your processing/analysis system. Finally, you load it
into that system, which stores the data according to some physical/internal (on-disk / in-memory)
model.

You get results. You publish them. You publish the data. How? Do you publish an export of the
physical model? The cycle continues.

{{< subscribe >}}
