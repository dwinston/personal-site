---
title: "Relating the ISO 11179 Metadata Registry (MDR) Standard to Semantic Web Standards"
date: 2020-10-28T11:52:17-04:00
draft: false
---

This is a brief note on my perception of the ISO 11179 Metadata Registry (MDR) standard,
including my perception of its relation to W3C Semantic Web standards. Examples are
taken from [this Wikipedia article](https://en.wikipedia.org/wiki/ISO/IEC_11179).

In ISO 11179, there are _concepts_. There are relations of concepts to wider and more narrow concepts.
There are also relations between a concept and one or more _representations_ of the concept
(i.e. different terms/synonyms are used, but the concept is the same).

There are _object classes_. An example is a "person". Combining an object class with a
concept such as "income" forms a more specific _data element concept_, e.g. a person's income.
Different representations of a data element concept are _data elements_. Differences in
these representations may be due to the use of different terms/synonyms, and/or due to
different _value domains_.

An example of a value domain for the data element concept "sex of person" is "M=Male, F=Female,
U=Unknown". No correctness is implied by selection of a value domain -- it simply is in use or is not in use
by a given data element. {M,F,U} are permitted values for "sex of person" in a particular data set
where "sex of person" is the data element concept and e.g. "sex of individual where the value domain is {M,F,U}"
is a data element for that concept, where the specialized representation in this case comprises both a
synonym term ("individual" for the object class "person") and a value domain. Data sets are many-to-many wrt
data elements.

### Relation to Semantic Web standards

A concept seems like a [skos](https://www.w3.org/TR/skos-reference/):Concept entity, which relates
to e.g. skos:broader and skos:narrower concepts. Other SKOS relations can apply, e.g. skos:related,
skos:closeMatch, skos:exactMatch, etc. An object class seems like a
[rdfs](https://www.w3.org/TR/rdf-schema/):Class / [owl](https://www.w3.org/TR/owl2-overview/):Class.

A data element concept, an association of an object class with a conceptual characteristic, seems like
e.g.
```
IF   { :p a rdf:Property .
       :p rdfs:domain :MyObjectClass ;
          rdfs:range :MyCharacteristicConcept . }
THEN { :p a :MyDataElementConcept . }
```
and thus an rdf:Property can be a bridge for multiple perceived data element concepts. Or, you
can use one property name for each distinct data element concept.

A data element seems like something that can subclass an owl:Restriction entity, extend its rdfs:domain,
or both, e.g.
```
:MyDataElement
  a :MyDataElementConcept ;
  rdfs:subClassOf [ a owl:Restriction ;
                    owl:onProperty :p ;
                    owl:allValuesFrom :SomeSet ;
                    rdfs:domain :MySynonymOfObjectClass ] .
```
I haven't seem rdfs:domain used inside a owl:Restriction class, but owl:onProperty is singular and required,
so the semantics of rdfs:domain entailment via an owl:Restriction seems clear to me. There is likely a simpler
way, but this was merely an exercise in mental mapping. 