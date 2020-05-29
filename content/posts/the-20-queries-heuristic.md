---
title: "The \"20 Queries\" Heuristic"
date: 2020-05-29T09:41:50-04:00
draft: false
---

A scientific database cannot be everything to everyone. Jim Gray came up with the
"20 queries" heuristic. What are the 20 most important questions the researchers want
the data system to answer?[^grayslaws]

Five questions are not enough to see a broader pattern, and
100 questions would dilute focus.
Also, the relative information in queries ranked by importance is likely to be
logarithmic -- a "long tail" distribution.
Thus, you're not likely to get five times more information collecting 100 versus 20 queries.

The goal of this step in a design process is to bridge the semantic gap between the
vocabulary used in the
scientific domain and the schema of the database, and to help domain scientists and
database engineers discuss design trade-offs that result in performance trade-offs.

## Example Exercise

I went through this exercise for an existing database, that of the Materials Project (MP).[^mp]
MP has a discussion forum[^mpforum], which has been active for a few years.
Tens of threads have over a thousand views each. I went through the threads,
sorted by descending view count, to pick out 20 queries posed.

Obviously, many of the found queries are residual queries,
that is, queries that post authors were not able
to answer clearly using MP's existing interface. However, some of the queries were
straightforward to answer via the existing system, as evidenced by replies to those posts.
In either case,
the queries I picked are a collection both sought by users of the system and viewed by many other
active or potential users.

I focused on queries not about the methodology of data collection, but about obtaining
data, including metadata pertaining to understood methodology, e.g. parameter values supplied
to programmatic methods.

I collected approximately 20 queries -- I stopped myself at 24.
Some I formatted as questions, other as stated desires/intentions.
I then tried to identify clusters and thus intended query patterns.
I identified six clusters[^sevenplusorminustwo],
and I removed one query as a duplicate of another.
Here are my results:

* labels/comments to discover what properties are available and what they mean
    - What is the stability of this material with respect to decomposition?
    - I want magnetic properties of materials (e.g. total_magnetization).
    - I want to compare elasticity, like shear or bulk modulus, to 
    density, to make a plot, so in excel form.
    - What are the meanings of the components of Structures? Like what is a "matrix"?
    - Which structures have been experimentally verified?

* named restriction classes of materials
    - What materials belong to the Zintl phase?
    - What are the formation energies of sulfides, fluorides, and oxides?
    - I want perovskite material data.
    - What is the structure-property metadata for the 941 piezoelectric
    materials in de Jong et al.'s 2015 paper?

* entity types different than materials but related in applications
    - I want data on batteries that contain a material by ID, or by chemical composition.
    - I want XYZ files for a bunch of Li-ion battery electrolyte molecules.
    - I want the INCAR file that was used to optimize a structure (from the blessed Task).
    - What is the KPOINTS file used for the bandstructure calculation of GaP (mp-2490)?

* data to a spreadsheet (tsv,csv) format
    - How can I get basic information about Li-containing compounds
    above the hull, to a spreadsheet?
    - I want results sorted by increasing stability (decreasing e_above_hull).
    - How do I download a few properties, like density and energy, for all compounds,
    for input to machine learning?

* complex literal types
    - I am looking for XRD patterns of Co-Pd compounds.
    - I want dielectric tensor data.
    - What are CIF files for the different polymorphs of formula X?
    - What is the CIF for VO2 of space group P21/C?

* queries involving multiple values for a property/attribute
    - What materials have a band gap between 0.5 and 1.2 eV?
    - What materials are in the chemical system of Ge, Se, and O (so
    including binaries and pure elements)?
    - I want formation energies, etc. for materials with both Ti and O and nothing else.
    
This is only one step in a design process,
but I hope this example helps you better understand the "20 queries" heuristic
and how you might apply
it to your work in designing data systems appropriate for domain specialists.

[^grayslaws]: Szalay and Blakeley, "Gray's Laws: Database-centric Computing in Science", in *The Fourth Paradigm
: Data-Intensive Scientific Discovery*. Microsoft Research, 2009.
[^mp]: <https://materialsproject.org>.
[^mpforum]: <https://matsci.org/c/materials-project/>.
[^sevenplusorminustwo]:  I aim to chunk items recursively in groups of at most 5±2, a hedge on
[Miller's 7±2](https://en.wikipedia.org/wiki/The_Magical_Number_Seven,_Plus_or_Minus_Two).

