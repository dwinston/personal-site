---
title: "Lets Not Reinvent the Wheel"
date: 2021-04-19T16:55:20-04:00
draft: false
---

I was reading about hidden costs of "packaged" software solutions -- that is, using existing
software to solve problems -- and came across this sentence:[^1]

> While the packaged solution saved some money on development, they more than made up for it in
implementation.

Huh? I typically do not distinguish *development* from *implementation*. What McComb is calling
"implementation" I just call "installation". Weird.

He goes on to detail the following activities needed to "install" a packaged solution:

* *Configuration*. This can conceivably be nestled under "installation", but some software has hundreds or thousands of flags/settings, many of which may influence each other, making this a complex activity.

* *Modification or extension*. If the package doesn't do *exactly* what you want it to do, you need to modify or extend it. If you find you need to modify it, note that introducing a change late in a system's lifecycle is typically way more complex than doing it early. And you are doing it as late as possible!

* *Integration*. The cost of integrating the new thing with existing systems can be huge: multiply the number of existing touch points by the number for the package, and multiple again by the complexities of each.

* *Data conversion*. The package likely has a data model that is arbitrarily different from the one you have in place. In addition to the data being structured differently, does the new system have different ideas about data integrity and validation? Does it require new data?

* *Change management*. Are there new screens? New terms/labels? A new implicit/explicit work flow? A need for a whole slew of new workarounds? You may need to retrain people to use a system that isn’t on the whole easier, just different.

Wow. Although "configuration" can conceivably be nestled under the term "installation", the
modification/extension, integration, data conversion, and change management activities are better
subsumed by "implementation"! Consider yourself lucky if/when you are able to simply "pip install"
and lightly configure a package without needing to do any of the above.

Can you simply "install" that package? Or will you need to *implement* it? To what extent does the
existing wheel fit your vehicle?

[^1]: McComb, Dave. *Software Wasteland: How the Application-Centric Mindset is Hobbling our
Enterprises*. Technics, 2018.

{{< subscribe >}}