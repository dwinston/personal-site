import json
import os
from collections import defaultdict
from operator import itemgetter

from jinja2 import Environment, FileSystemLoader, select_autoescape
from rdflib import Graph, RDF, SKOS, Namespace, URIRef

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


if __name__ == "__main__":
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

    template = jinja_env.get_template("skos_vocab.html")

    html = template.render(
        title=next(s for s in scheme_statements if "dcterms:title" in s["p"])["o"][1:-1],
        description=next(s for s in scheme_statements if "dcterms:description" in s["p"])["o"][1:-1],
        scheme_statements=scheme_statements,
        statements_for_concept=statements_for_concept,
    )

    os.makedirs("static/elements_of_clojure", exist_ok=True)
    with open("static/elements_of_clojure/index.html", "w") as f:
        f.write(html)
