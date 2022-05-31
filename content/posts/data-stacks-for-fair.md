---
title: "Data Stacks for FAIR"
date: 2022-05-30T14:39:34-04:00
draft: false
---

I noticed a pattern at the top of each case study listed by [Stemma.ai](https://www.stemma.ai),
which provides data catalog software as a service based on the open-source
[Amundsen](https://www.amundsen.io/) code. Each case study's so-called "Data Stack" comprises up to
four distinct categories of functionality -- Data Catalog, Data Warehouse, ETL, and Business
Intelligence.

The "Data Stack" for each case study:
<br>

|Case|Data Catalog|Data Warehouse|ETL|Business Intelligence|
|---|---|---|---|---|
|[Lyft](https://www.stemma.ai/amundsen-case-studies/lyft)|Amundsen|Presto|Apache Airflow|Mode,Apache Superset|
|[Convoy](https://www.stemma.ai/stemma-case-studies/convoy)|Stemma|Snowflake|dbt, Apache Airflow|Tableau, Metabase|
|[iRobot](https://www.stemma.ai/stemma-case-studies/irobot)|Stemma|Amazon Athena|(blank)|Mode|
|[ING](https://www.stemma.ai/amundsen-case-studies/ing)|Amundsen|Trino (formerly, Presto SQL)|(blank)|Apache Superset|

<br>

These categories struck me in relation with the FAIR Principles[^fair]:

* A Data Catalog is about making data *Findable*.
* A Data Warehouse is about making data *Accessible*.
* An ETL platform, aka a Data Orchestration[^sda] platform, is about making data *Interoperable*.
* A Business Intelligence (BI) tool is about making data *Reusable*, aka Repurposeable.

It's encouraging to see high-level alignment between the FAIR Principles and a conceptualization of useful enterprise data systems in the corporate world. 

[^fair]: M. D. Wilkinson et al., "The FAIR Guiding Principles for scientific data management and stewardship," Sci Data, vol. 3, no. 1, p. 160018, Mar. 2016, doi: 10/bdd4.
[^sda]: Although a term I think may be more apt here than Data Orchestration, which has an imperative tone, is *Data Reconciliation*, which has a declarative tone -- see e.g. S. Ryza, "Introducing Software-Defined Assets", Dagster Blog, Mar. 2022. https://dagster.io/blog/software-defined-assets (accessed May 31, 2022).



