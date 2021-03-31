---
title: "The QUDT System for Dimensional Analysis and Unit Conversions"
date: 2021-03-31T15:02:57-04:00
draft: false
---

In order to integrate quantitative data, you need to know (a) if units are commensurate, and (b) if so, how to do
conversions.

The Quantities, Units, Dimensions, and Types (QUDT) ontology serves three major purposes. First, it provides a global
reference for units via URIs; this helps avoid tacit conventions that are prone to misinterpretation. Second, it
provides for dimensional analysis via so-called "quantity kind" dimensional vectors; you can determine that each side of
an equation resolves to "length over time squared", for instance. Third, it provides for unit conversions.

Below is a concrete example of the kind of metadata available in QUDT. It is represented in the Turtle format for (I
hope) better readability than JSON, but this is easily converted to JSON.

The dump below is to facilitate me pointing out a few concrete features. First, notice that the "Acceleration" quantity
kind is linked to known applicable units across systems of units (Imperial, SI, etc.). Second, notice that
"Acceleration" links to a dimension vector that expresses an exponent of 1 for length and -2 for time, i.e. "length over
time squared". Finally, notice that each unit has a conversion multiplier relative to a common base unit (so it's not
important to know what that base unit is); some units also have a conversion offset, e.g. Celcius (unit:DEG_C) has a
qudt:conversionOffset of 273.15.

```turtle
@prefix quantitykind: <http://qudt.org/vocab/quantitykind/> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix qkdv: <http://qudt.org/vocab/dimensionvector/> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@prefix sou: <http://qudt.org/vocab/sou/> .

quantitykind:Acceleration
  a qudt:QuantityKind ;
  dcterms:description "Acceleration is the (instantaneous) rate of change of velocity. Acceleration may be either linear acceleration, or angular acceleration. It is a vector quantity with dimension \\(length/time^{2}\\) for linear acceleration, or in the case of angular acceleration, with dimension \\(angle/time^{2}\\). In SI units, linear acceleration is measured in \\(meters/second^{2}\\) (\\(m \\cdot s^{-2}\\)) and angular acceleration is measured in \\(radians/second^{2}\\). In physics, any increase or decrease in speed is referred to as acceleration and similarly, motion in a circle at constant speed is also an acceleration, since the direction component of the velocity is changing."^^qudt:LatexString ;
  qudt:applicableUnit unit:CentiM-PER-SEC2 ;
  qudt:applicableUnit unit:FT-PER-SEC2 ;
  qudt:applicableUnit unit:G ;
  qudt:applicableUnit unit:GAL ;
  qudt:applicableUnit unit:IN-PER-SEC2 ;
  qudt:applicableUnit unit:KN-PER-SEC ;
  qudt:applicableUnit unit:KiloPA-M2-PER-GM ;
  qudt:applicableUnit unit:M-PER-SEC2 ;
  qudt:applicableUnit unit:MicroG ;
  qudt:applicableUnit unit:MilliG ;
  qudt:applicableUnit unit:MilliGAL ;
  qudt:dbpediaMatch "http://dbpedia.org/resource/Acceleration"^^xsd:anyURI ;
  qudt:hasDimensionVector qkdv:A0E0L1I0M0H0T-2D0 ;
  qudt:informativeReference "http://en.wikipedia.org/wiki/Acceleration"^^xsd:anyURI ;
  rdfs:isDefinedBy <http://qudt.org/2.1/vocab/quantitykind> ;
  rdfs:label "Acceleration"@en ;
  owl:sameAs quantitykind:LinearAcceleration ;
.
qkdv:A0E0L1I0M0H0T-2D0
  a qudt:QuantityKindDimensionVector_CGS ;
  a qudt:QuantityKindDimensionVector_ISO ;
  a qudt:QuantityKindDimensionVector_Imperial ;
  a qudt:QuantityKindDimensionVector_SI ;
  qudt:dimensionExponentForAmountOfSubstance 0 ;
  qudt:dimensionExponentForElectricCurrent 0 ;
  qudt:dimensionExponentForLength 1 ;
  qudt:dimensionExponentForLuminousIntensity 0 ;
  qudt:dimensionExponentForMass 0 ;
  qudt:dimensionExponentForThermodynamicTemperature 0 ;
  qudt:dimensionExponentForTime -2 ;
  qudt:dimensionlessExponent 0 ;
  qudt:hasReferenceQuantityKind quantitykind:LinearAcceleration ;
  qudt:hasReferenceQuantityKind quantitykind:ThrustToMassRatio ;
  qudt:latexDefinition "\\(L T^-2\\)"^^qudt:LatexString ;
  rdfs:isDefinedBy <http://qudt.org/2.1/vocab/dimensionvector> ;
  rdfs:label "A0E0L1I0M0H0T-2D0" ;
.
unit:FT-PER-SEC2
  a qudt:DerivedUnit ;
  a qudt:Unit ;
  dcterms:description "\\(\\textit{Foot per Square Second}\\) is an Imperial unit for \\(\\textit{Linear Acceleration}\\) expressed as \\(ft/s^2\\)."^^qudt:LatexString ;
  qudt:conversionMultiplier 0.3048 ;
  qudt:definedUnitOfSystem sou:IMPERIAL ;
  qudt:definedUnitOfSystem sou:USCS ;
  qudt:expression "\\(ft/s^{2}\\)"^^qudt:LatexString ;
  qudt:hasDimensionVector qkdv:A0E0L1I0M0H0T-2D0 ;
  qudt:hasQuantityKind quantitykind:Acceleration ;
  qudt:iec61360Code "0112/2///62720#UAA452" ;
  qudt:ucumCode "[ft_i].s-2"^^qudt:UCUMcs ;
  qudt:ucumCode "[ft_i]/s2"^^qudt:UCUMcs ;
  qudt:uneceCommonCode "A73" ;
  qudt:unitOfSystem sou:IMPERIAL ;
  rdfs:isDefinedBy <http://qudt.org/2.1/vocab/unit> ;
  rdfs:label "Foot per Square Second"@en ;
.
```

There are >1500 units spanning hundreds of quantity kinds and dimension vectors. New units [are
welcome](https://github.com/qudt/qudt-public-repo/wiki/Unit-Vocabulary-Submission-Guidelines).

I hope QUDT can help you in thinking about FAIR sharing of quantitative data.

{{< subscribe >}}