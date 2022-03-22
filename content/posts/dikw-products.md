---
title: "DIKW Bases and Products"
date: 2022-03-22T09:40:15-04:00
draft: false
mermaid: true
---

"Self-describing" data products include/contain/link to any "knowledge products"
(schema, ontology, etc.) they were informed by.

In the sense of the data-information-knowledge-wisdom (DIKW) conceptualization, are there
*information products*?

Perhaps self-describing *information products* include/contain/link to any "wisdom products" (usage
context! impact of previous decisions!) they were informed by?

I started thinking about all this after listening to the conversation with Shane Gibson on [a recent
Catalog and Cocktails
episode](https://anchor.fm/datadotworld/episodes/Agile-like-a-fox--but-for-data--WShane-Gibson-from-AgileData-io-e1fqtu2).

See below for my first-draft rough sketch of how various DIKW "bases" (so not just databases) can
inform corresponding DIKW "products" as part of a process of ongoing improvement of operationalizing
digital assets for research and business functions.

{{<mermaid>}}
flowchart TD
    DB[(data base)] -->|facts| DX[transform]
    KB[(knowledge base)] -->|schema| DX[transform]
    DX[transform] -->|tables,JSON documents| DP[/data products/]
    FB[(information base)] -->|frames,templates| DPX[transform]
    DP -->|understood facts| DPX[transform]
    DPX -->|reports,figures,dashboards,views| IP[/information products/]
    IP -->|interpretation,interaction| HD[fa:fa-user human decisions]
    HD -->|desired interventions| DCB[(decision base)]
    DCB -->|applicable rules,logic| DCX[transform]
    DP --> DCX[transform]
    DCX[transform] -->|actions to take| DCP[/decision products/]
    WB[(wisdom base)] -->|metrics,indicators| WX[transform]
    DP --> WX[transform]
    DCP -->|action taken| WX
    WX -->|performance| WP[/wisdom products/]
    HD -->|experience| WB
    WP -->|impact of previous decisions| DPX
{{</mermaid>}}