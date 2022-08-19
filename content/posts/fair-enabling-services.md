---
title: "FAIR-Enabling Services"
date: 2022-08-18T22:14:09-04:00
draft: false
---

<small>(The following is a transcript of my recent [podcast
episode](https://podcast.polyneme.xyz/episodes/fair-enabling-services) on this topic.)</small>

There is a [FAIR Implementation Profile ontology](https://w3id.org/fair/fip/terms/FIP-Ontology), and
it talks about [FAIR-enabling resources](https://w3id.org/fair/fip/terms/FAIR-Enabling-Resource). So
these are corresponding to [questions](https://w3id.org/fair/fip/terms/FIP-Question). For each of
the fifteen [FAIR principles](https://w3id.org/fair/principles/terms/FAIR), this FAIR-enabling
resource, the idea is that you've identified a
[challenge](https://w3id.org/fair/fip/terms/FIP-No-Choice-Declaration) or you've made a
[choice](https://w3id.org/fair/fip/terms/FIP-Declaration) about some resource that's going to help
you fulfill that -- either that resource is
[available](https://w3id.org/fair/fip/terms/declares-current-use-of), or it's [planned](
https://w3id.org/fair/fip/terms/declares-planned-use-of), or it's
[proposed](https://w3id.org/fair/fip/terms/declares-planned-development-of), or you're going to
[phase it out](https://w3id.org/fair/fip/terms/declares-planned-replacement-of), that sort of thing.

Twelve FAIR-enabling resources have been identified as broad categories that help address each of
the challenges with FAIR principles. One is an [identifier
service](https://w3id.org/fair/fip/terms/Identifier-service). This is a service that provides for
any digital object, (1) algorithms guaranteeing global uniqueness; (2) a policy document that
guarantees persistence; and (3) resolution of the identifier to machine actionable metadata
describing the object and its location.

This is all into under Findable. Another FAIR-enabling resource is [metadata
schema](https://w3id.org/fair/fip/terms/Metadata-schema). So this would be a specification, a
schema, that specifies metadata fields describing attributes of data or other digital objects.
Another FAIR-enabling resource would be a [metadata-data linking
schema](https://w3id.org/fair/fip/terms/Metadata-data-linking-schema). So this would be,
specifically, a specification -- schema -- that provides a unique, persistent, ideally
bi-directional machine actionable link between metadata and the data they describe. And the final
FAIR-enabling resource for the Findable principles is a
[registry](https://w3id.org/fair/fip/terms/Registry), which is a service that indexes metadata and
data and provides a search over that index.

For Accessible, there are three identified FAIR-enabling resources. [Communication
protocol](https://w3id.org/fair/fip/terms/Communication-protocol): so this is a specification for
how messages are structured and exchanged. There's [authentication and authorization
service](https://w3id.org/fair/fip/terms/Authentication-and-authorization-service). So this is a
service that mediates access to digital objects according to specified conditions.

And another FAIR-enabling resource is a [metadata preservation
policy](https://w3id.org/fair/fip/terms/Metadata-preservation-policy). So this would be a document
that describes the conditions under which metadata are to be provisioned in the future, maybe part
of a data management plan.

Okay. Five more FAIR-enabling resources identified. We're going to Interoperability now. One is a
[knowledge representation language](
https://w3id.org/fair/fip/terms/Knowledge-representation-language): a language specification whereby
knowledge can be made processable by machines. Another FAIR-enabling resource is [structured
vocabulary](https://w3id.org/fair/fip/terms/Structured-vocabulary): a controlled list of uniquely
identified and unambiguous concepts with their definitions represented preferably using web
standards.

Finally, in Interoperable, a FAIR-enabling resource would be a [semantic
model](https://w3id.org/fair/fip/terms/Semantic-model), a specification that defines qualified
relations between entities describing data or other digital objects using structured vocabularies.

The two remaining FAIR-enabling resources, under Reusable, are (1) [data usage
license](https://w3id.org/fair/fip/terms/Data-usage-license) -- so that's a document that describes
the conditions under which a digital object can be legally used. And finally, a [provenance
model](https://w3id.org/fair/fip/terms/Provenance-model); a specification -- schema -- that
specifies metadata fields describing the origin and lineage of data or other digital objects.

So these are a bunch of FAIR-enabling resources. I was thinking about this a bit, and I wanted to
distinguish between things that actually have to be running in order for data to be alive and for
you to actually find it, access it, interoperate with it, reuse it, versus things that are resources
that those services will need that are more "one-time" things.

For example, a metadata schema isn't really a service, so to speak. It's something that you can do
and be done with. You might need to make revisions of it, so maybe there's some change management
procedure. But in terms of the actual service, it isn't quite like an identifier service, where you
want to be given an identifier and be able to know where to go, and resolve that identifier, and
determine if you have the right identifier and then get the data, get the metadata. So that's an
actual service that needs to be run. If not continuously, whenever you decide you need
identification, you can spin up that service and do that, but it's an actual service that needs to
be run in order for you to have living findability, accessibility, interoperability, reusability.

So of these 12 FAIR-enabling resources, I've thought about how to condense them into FAIR-enabling
_services_. What are the actual _services_ that are really important across these that someone needs
to worry about if they want a FAIR data ecosystem in their lab and their lifecycle for research,
that sort of thing.

I've identified these as (1) An identification service, an identifier service. You need to be able
to identify things. And this is identifying metadata, datasets, as well as vocabulary things. So
this spans, say, F1, the A principles, as well as I2 in terms of making a vocabulary FAIR, being
able to unambiguously identify vocabulary terms. So identification is a big service that's needed.

The second service is validation. So, you could be given a metadata schema and given statements and
assertions, but how do you know they actually conform to the schema? Are you going to look those up
by hand? Are you going to kind of cross check with a sheet of paper that you have in front of you
that says the schema? No, you really want a validation service that will validate statements
according to a schema that you're imposing.

The third service is indexing. So this is related to the registry. You need something that, given a
bunch of statements that have identifiers that resolve, a bunch of statements that are valid
according to the schema -- so you've identified, you validated. You then need to collect them and be
able to find what you need. And so that involves indexing. So that's an actual service where you can
search the index. An index is the basis of search. Otherwise you're just doing a full scan of all
your statements. You won't get any leverage. You won't be able to winnow down with any efficiency at
all. So this index thing, this ongoing indexing, where you have an index and you maintain an index
and when you identify new concepts or data, assign them identifiers, validate your statements about
them, you want to throw them in the index and you want your registry to re-index things. So that
indexing needs to be a service.

The fourth FAIR-enabling service to me is translation. So, this is the essence of interoperation.
This is the point of having a knowledge representation language and a semantic model where you're
defining qualified relations. The idea being, you have a bunch of metadata and you want to use it
for something else. So you need some service to actually translate it. If you have data in some
format, you want to be able to translate it. You want these qualified links to know that, if you
have metadata of this format, say of a schema.org Dataset and you want a DCAT Dataset, you know the
corresponding mapping and you can perform that translation. So that would be a FAIR-enabling service
that would leverage resources like semantic model, structured vocabulary, language -- ultimately, it
would leverage your index as well. So, translation would also be dependent on an index, just like
search is.

And the final service that I think is important here is tracing. So, given something, you want to
trace "where did it come from?", and how you can use it. So this connects directly to your, static
or not, policies about usage rights, data usage, and your provenance model. And this is how you can
actually trace where things are, to determine if you can reuse it. So this is something active that
you want. You want something, and again, this would ultimately leverage an index as well. So you'd
have a bunch of data objects and metadata objects and vocabulary terms, all of which would need to
be identified, so that'd be an identifying service. All of your statements about things, about
provenance, mapping for translation, indexing, all of that would have to be validated. So you have
the validation service, and then finally you have the indexing. And that puts everything in. And the
indexing is the basis of support for search, which I don't think needs to be a separate
FAIR-enabling service -- there are various ways of searching over an index, given it. But it also
enables this translation based on the semantics that you have in your model and your resources, and
tracing to determine, can I use this? What's the provenance of this? Was it based on things that
fell under this certain license? And so, depending on the license of my transformations, this is
what I can use it for.

So again, these FAIR-enabling services are: Identifying, Validating, Indexing, Translating, and
Tracing. And I hope to go into more detail about how these relate to the FAIR principles and the
resources, and sort of elaborate on them individually over the coming weeks.

{{< subscribe >}}
