---
title: "FAIR and Stages of Reusability"
date: 2020-09-11T11:55:41-04:00
draft: false
---

The four components of FAIR can be mapped to successive stages of reusability: possible, plausible, probable, and perishable.

The foundational principles of FAIR are Findability, Accessibility, Interoperability, and Reusability.[^fair]
Ultimately, FAIR is all about reuse, and it's helpful for me to think of the principles as successive stages of
increasing the chance that successful reuse can happen.

Findability is making reuse *possible*. If no one can discover your data via some open catalog, if even basic metadata is hidden in a silo, then reuse is simply not possible.

Accessibility is making reuse *plausible*. People and their designated software agents can not only identify relevant resources via metadata, but they can actually retrieve full data for inspection and evaluation. Now, it is plausible that your data may be reused.

Interoperability is making reuse *probable*. Not only is your data findable and accessible, but there is not too heavy a burden on someone to make your data compatible with their own data and processing tools. Your data is accessible in an open, standard format. You include a schema with the data, preferably in a machine-actionable format as well. Because an interested data consumer needn't do a prohibitive amount of data cleaning/munging, it is significantly more likely that your data may be reused.

Reusability, finally, is making reuse...*perishable*. Using a food analogy, let's say you have identified a potential ingredient for a recipe (findability); you know it is in stock at a nearby store (accessibility); and you have determined that it is indeed suitable for use with your kitchen tools, other ingredients you have on-hand for the recipe, etc. (interoperability). Finally, you can bring it home to your kitchen, but you won't necessarily be able to actually use it!

The warranties on and terms of use for data, its licenses, are important, analogous to "best by" dates, expiration dates, etc. on food. The reusability concern of FAIR does not guarantee reuse, but it again increases the likelihood of reuse because the terms and conditions of reuse are made more explicit and thus a consumer of your data can make a decision to reuse with confidence. Data with no license is like a food product with no expiration date -- does that mean it's forever usable, or will someone likely be unsure and thus choose not to reuse your data?

FAIR is all about reuse. I hope this conceptualization of FAIR via "four Ps" helps you understand ways you can progressively enhance your data dissemination tactics and thereby enhance your data's discoverability and reuse. 

[^fair]: Wilkinson, M., Dumontier, M., Aalbersberg, I. et al. *The FAIR Guiding Principles for scientific data management and stewardship*. Sci Data 3, 160018 (2016). https://doi.org/10.1038/sdata.2016.18
