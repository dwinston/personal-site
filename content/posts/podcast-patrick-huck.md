---
title: "Interview with Patrick Huck, on implementing FAIR for computed materials data"
date: 2022-07-21T11:01:58-04:00
draft: false
---

This week on Machine-Centric Science, I interviewed Patrick Huck, currently staff on the Materials
Project at the Lawrence Berkeley National Laboratory in Berkeley, California. We talk about choices
and considerations in implementing FAIR.

[LISTEN NOW »](https://share.transistor.fm/s/dc5be09e)

There are show notes at the link above. Also, I tried to summarize our discussion as a [draft FAIR
Implementation Profile
(FIP)](https://np.petapico.org/RARgDGc4UYSdRmNq-BtZ4_Gd0ZvE08yms-Ew__tGwbolE).

# Talking Points

Career paths for people that are scientists AND software engineers.

The U.S. Department of Energy Office of Scientific and Technical Information (OSTI) DOI Service.

What gets a DOI? Granularity of resources.

Partnering with the Novel Materials Discovery (NOMAD) Laboratory for accessing raw data.

Modeling: with Python classes and with OpenAPI.

API Gateway design for authentication and authorization.

Provenance: for calculation workflows and for structure sourcing (credit to submitters!).

# Quotable Quotes

"I think that's a big topic in science generally. What are the career paths for people that are
software engineers that are also scientists or maybe scientists first and software engineers second,
and have gone that route? It's not like there's H indexes for people like me in terms of
publications."

"[OSTI] provides the infrastructure for minting those DOIs and making sure that those links are
always live. We've become over the years with now, I think 147,000 DOIs, their biggest data client."

"We use what's called robocrystallographer, which gets descriptions based on machine learning that
we get based on the information that we calculate about that structure. And then we can take that
description auto generated from our database entries and send it as metadata for the DOIs."

"It's kind of transparent without even knowing that there's an API behind it. To the extent that
sometimes people talk about the API and they actually mean the client. I think that's a good thing.
People in our space expect those things to be pretty transparent."

"I don't think that guarantees longevity on the scale of glacial times."

"There's a lot going on in terms of making data FAIR. It's a little easier for making documents
FAIR, like having PDFs findable. On the data level, it becomes a little bit more complicated. And I
think that we should strive to get as close as possible to get to FAIR, but it might not for be
feasible for every domain."

# Sharing is caring!

If you enjoyed this episode, please consider sharing it with a few friends who might find it useful.
Thanks!
