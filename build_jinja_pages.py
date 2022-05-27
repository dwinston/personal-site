import json
import os
from collections import defaultdict
from operator import itemgetter

from jinja2 import Environment, FileSystemLoader, select_autoescape
from rdflib import Graph, RDF, RDFS, SKOS, Namespace, URIRef, DCTERMS

jinja_env = Environment(
    loader=FileSystemLoader("jinja_templates"),
    autoescape=select_autoescape(),
)


def display(item, g):
    label = item.n3(g.namespace_manager)
    if label.startswith("<") and label.endswith(">"):
        label = label[1:-1]
    if isinstance(item, URIRef):
        return f'<a href={str(item)}>{label}</a>'
    else:
        return label


def _build_page_of_resource_mappings(ttl_file_basename):
    g_vocab = Graph().parse("static/ontologies/skos.ttl")
    label_props = [RDFS.label] + [p for p in g_vocab.subjects(RDFS.subPropertyOf, RDFS.label)]
    note_props = [SKOS.note] + [p for p in g_vocab.subjects(RDFS.subPropertyOf, SKOS.note)]
    mapping_props = [SKOS.exactMatch] + [p for p in g_vocab.subjects(RDFS.subPropertyOf, SKOS.mappingRelation)]
    props_allowlist = label_props + note_props + mapping_props

    statements_for_resource = defaultdict(list)

    g = Graph()
    g.parse(f"static/{ttl_file_basename}.ttl")
    for p in props_allowlist:
        for s, o in g.subject_objects(p):
            r = display(s, g)
            statements_for_resource[r].append(
                dict(p=display(p, g), o=display(o, g)))

    statements_for_resource = {r: sorted(statements_for_resource[r], key=itemgetter("p"))
                               for r in sorted(statements_for_resource)}

    template = jinja_env.get_template("labels_and_notes.html")
    html = template.render(
        ttl_file_basename=ttl_file_basename,
        title=g.value(
            subject=URIRef(f"https://donnywinston.com/{ttl_file_basename}"),
            predicate=DCTERMS.title
        ),
        statements_for_resource=statements_for_resource
    )

    os.makedirs(f"static/{ttl_file_basename}", exist_ok=True)
    with open(f"static/{ttl_file_basename}/index.html", "w") as f:
        f.write(html)


def _build_elements_of_clojure_page():
    g = Graph()
    g.parse("static/elements_of_clojure.dw.ttl")
    g.bind("vaem", Namespace("http://www.linkedmodel.org/1.2/schema/vaem#"))

    scheme = g.value(predicate=RDF.type, object=SKOS.ConceptScheme)
    scheme_statements = []
    for p, o in g.predicate_objects(scheme):
        scheme_statements.append(dict(p=display(p, g), o=display(o, g)))
    scheme_statements = sorted(scheme_statements, key=itemgetter("p"))

    statements_for_concept = defaultdict(list)

    for concept in g.subjects(RDF.type, SKOS.Concept):
        c = display(concept, g)
        for p, o in g.predicate_objects(concept):
            statements_for_concept[c].append(
                dict(p=display(p, g), o=display(o, g)))
        statements_for_concept[c] = sorted(
            statements_for_concept[c], key=itemgetter("p")
        )
    statements_for_concept = {c: statements_for_concept[c] for c in sorted(statements_for_concept)}

    collections = []
    for c in g.subjects(RDF.type, SKOS.Collection):
        c_link = display(c, g)
        c_id = c_link.split(':')[-1][:-4]
        collections.append({
            "id": c_id,
            "link": c_link,
            "members": sorted([display(m, g) for m in g.objects(c, SKOS.member)])
        })
    coll_order = ["Names", "Idioms", "Indirection", "Composition"]
    collections = sorted(collections, key=lambda c: coll_order.index(c["id"]))

    template = jinja_env.get_template("skos_vocab.html")

    html = template.render(
        title=next(s for s in scheme_statements if "dcterms:title" in s["p"])["o"][1:-1],
        description=next(s for s in scheme_statements if "dcterms:description" in s["p"])["o"][1:-1],
        scheme_statements=scheme_statements,
        statements_for_concept=statements_for_concept,
        collections=collections,
    )

    os.makedirs("static/elements_of_clojure", exist_ok=True)
    with open("static/elements_of_clojure/index.html", "w") as f:
        f.write(html)


if __name__ == "__main__":
    #_build_elements_of_clojure_page()
    _build_page_of_resource_mappings("fair-vs-data-product-abcde")