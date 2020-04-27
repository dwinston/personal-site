---
title: "The WYSIWYG Publication"
date: 2020-04-24T15:19:00-04:00
draft: false
---

I was fascinated as I skimmed over a publication detailing a network analysis of crystalline materials.[^aykol]
It's "Open Access", meaning I don't have to pay to read the text and figures. There was one figure that had neat
 data-driven graphics for two separate materials, one stacked on top of the other.
 
 I wondered what the graphics would look like for some of the other 22,600 materials considered
 by the study. But there was nowhere to click or mouseover to get that party started. Of course not. But why not?
 
## Linked open data
 
Tim Berners-Lee presented a 5-star rating system for linked open data.[^5star]
The figure I liked in the publication, a PNG image, counts as 1-star open data. It really is better than nothing. 

Furthermore, a web app[^materialnet] was developed to explore the underlying data driving
the figure, but that doesn't have functionality to reproduce the figure. I mention it only as an example of 2-star
 open data, in the sense that one could obtain some data from the app in a structured way using non-standard code to
  automate browser actions, if one so chose.
  
The article also links to 3-star data. The data is obtained by downloading a zip file
 containing a plaintext license file (CC-BY-4.0, great!), a CSV file, and two JSON files. This is good -- all
 non-proprietary formats. Three stars.
 
The data in the files don't use HTTP URIs to identify things.
This is not necessarily a big deal if specialists in a domain implicitly share
conventions/ontologies around naming things (including relationships) and expressing data values, but it
poses friction, especially for automated reuse.

For example, I may be pretty sure that the string key value
"Mn3TeO6" in the giant JSON object comprising one of the JSON files
is a reduced (unit cell) chemical formula for a specific known phase of a crystalline material, but I don't know.
With linked data, HTTP URIs are used as names for things so that people can look up those names. If the
key value was `<https://www.nature.com/articles/s41467-019-10030-5/Mn3TeO6>`, and I could query for metadata relating
to that resource (using open linked-data standards like RDF and SPARQL), then I could more confidently interpret the
 data. This would be 4-star data.

Linking to other people's data to provide context, like setting that key to be
[`<https://materialsproject.org/materials/mp-18795>`](https://materialsproject.org/materials/mp-18795), or at least
 linking to it via an RDF property
 like [`rdfs:seeAlso`](https://www.w3.org/TR/rdf-schema/#ch_seealso), would make it 5-star data.
 
## Representing knowledge with computation
 
Unfortunately, even 5-star data doesn't get me my parameterized figure UI, which I want one click away from the static
 figure embedded in the publication's online text. Not directly. Some application code needs to run. But, that
 application code could be data-driven, and with 5-star data it could be *principally* data-driven. A data model with
 ontology as a first-class citizen means there is no need for a "convention over configuration" stance: conventions
  themselves become eminently configurable.
  
Ultimately, data-driven UI can be so seamless that there is no shuffling among, say, an IDE, a collection of Jupyter
 notebooks, web apps, and document typesetting systems like LaTeX that deliver a published article.
  The idea that people today are still [trying to understand cancer by staring
  at a text editor is appalling](https://www.theatlantic.com/technology/archive/2017/09/saving-the-world-from-code/540393/).
  Researchers need tools for What You See Is What You Get (WYSIWYG) workflows, shareable with their peers and beyond.

[^aykol]: Aykol et al., ["Network analysis of synthesizable materials discovery"](https://www.nature.com/articles/s41467-019-10030-5), *Nature Communications* (2019).
[^materialnet]: Choudhury et al., ["MaterialNet: A web-based graph explorer for materials science data"](https://doi.org/10.21105/joss.02105), Journal of Open Source Software (2020).
[^5star]: Tim Berners-Lee,
["Linked Data: Is your Linked Open Data 5 Star?"](https://www.w3.org/DesignIssues/LinkedData.html#fivestar), 2010.