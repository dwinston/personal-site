from pathlib import Path
import re
import sys

from rdflib import Graph
from rdflib.namespace import NamespaceManager
import rdflib.namespace
import requests
from toolz import merge

filepath = sys.argv[1]
assert filepath.endswith(".ttld")

lines_raw = Path(filepath).read_text().splitlines()

lines_header = []
lines_body = []
prefixes_doc = {}
in_header = False
for line in lines_raw:
    if line == "---":
        in_header = not in_header
        lines_header.append(line)
        continue
    if in_header:
        lines_header.append(line)
        continue

    if m := re.fullmatch(r"@prefix\s+([^:]*):\s+<([^<].+)>\s+.", line):
        prefixes_doc[m.group(1)] = m.group(2)
    else:
        lines_body.append(line)

# XXX overwriting any supplied prefixes with
#   https://github.com/zazuko/rdf-vocabularies/blob/master/src/prefixes.ts
#   for now because I hardcode use of <https://prefix.zazuko.com/api/v1/autocomplete>.
#   Use <https://prefix.zazuko.com/> to check terms before including.
prefixes = {
    "acl": "http://www.w3.org/ns/auth/acl#",
    "as": "https://www.w3.org/ns/activitystreams#",
    "bibo": "http://purl.org/ontology/bibo/",
    "cc": "http://creativecommons.org/ns#",
    "cnt": "http://www.w3.org/2011/content#",
    "constant": "http://qudt.org/vocab/constant/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "ctag": "http://commontag.org/ns#",
    "dash": "http://datashapes.org/dash#",
    "dbo": "http://dbpedia.org/ontology/",
    "dc11": "http://purl.org/dc/elements/1.1/",
    "dcam": "http://purl.org/dc/dcam/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "dcmitype": "http://purl.org/dc/dcmitype/",
    "dcterms": "http://purl.org/dc/terms/",
    "discipline": "http://qudt.org/vocab/discipline/",
    "doap": "http://usefulinc.com/ns/doap#",
    "dpv": "http://www.w3.org/ns/dpv#",
    "dqv": "http://www.w3.org/ns/dqv#",
    "dtype": "http://www.linkedmodel.org/schema/dtype#",
    "duv": "http://www.w3.org/ns/duv#",
    "earl": "https://www.w3.org/ns/earl#",
    "ebucore": "http://www.ebu.ch/metadata/ontologies/ebucore/ebucore#",
    "exif": "http://www.w3.org/2003/12/exif/ns#",
    "foaf": "http://xmlns.com/foaf/0.1/",
    "frbr": "http://purl.org/vocab/frbr/core#",
    "geo": "http://www.opengis.net/ont/geosparql#",
    "geof": "http://www.opengis.net/def/function/geosparql/",
    "geor": "http://www.opengis.net/def/rule/geosparql/",
    "gml": "http://www.opengis.net/ont/gml#",
    "gn": "http://www.geonames.org/ontology#",
    "gr": "http://purl.org/goodrelations/v1#",
    "grddl": "http://www.w3.org/2003/g/data-view#",
    "gs1": "https://gs1.org/voc/",
    "gtfs": "http://vocab.gtfs.org/terms#",
    "http": "http://www.w3.org/2011/http#",
    "hydra": "http://www.w3.org/ns/hydra/core#",
    "ical": "http://www.w3.org/2002/12/cal/icaltzd#",
    "ldp": "http://www.w3.org/ns/ldp#",
    "locn": "http://www.w3.org/ns/locn#",
    "lvont": "http://lexvo.org/ontology#",
    "ma": "http://www.w3.org/ns/ma-ont#",
    "oa": "http://www.w3.org/ns/oa#",
    "og": "http://ogp.me/ns#",
    "org": "http://www.w3.org/ns/org#",
    "owl": "http://www.w3.org/2002/07/owl#",
    "prefix": "http://qudt.org/vocab/prefix/",
    "prov": "http://www.w3.org/ns/prov#",
    "qb": "http://purl.org/linked-data/cube#",
    "qkdv": "http://qudt.org/vocab/dimensionvector/",
    "quantitykind": "http://qudt.org/vocab/quantitykind/",
    "qudt": "http://qudt.org/schema/qudt/",
    "rdau": "http://rdaregistry.info/Elements/u/",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "rdfa": "http://www.w3.org/ns/rdfa#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "rev": "http://purl.org/stuff/rev#",
    "rico": "https://www.ica.org/standards/RiC/ontology#",
    "rif": "http://www.w3.org/2007/rif#",
    "rr": "http://www.w3.org/ns/r2rml#",
    "rss": "http://purl.org/rss/1.0/",
    "schema": "http://schema.org/",
    "sd": "http://www.w3.org/ns/sparql-service-description#",
    "sdmx": "http://purl.org/linked-data/sdmx#",
    "sem": "http://semanticweb.cs.vu.nl/2009/11/sem/",
    "sf": "http://www.opengis.net/ont/sf#",
    "sh": "http://www.w3.org/ns/shacl#",
    "shex": "http://www.w3.org/ns/shex#",
    "sioc": "http://rdfs.org/sioc/ns#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "skosxl": "http://www.w3.org/2008/05/skos-xl#",
    "sosa": "http://www.w3.org/ns/sosa/",
    "sou": "http://qudt.org/vocab/sou/",
    "ssn": "http://www.w3.org/ns/ssn/",
    "test": "http://www.w3.org/2006/03/test-description#",
    "time": "http://www.w3.org/2006/time#",
    "unit": "http://qudt.org/vocab/unit/",
    "v": "http://rdf.data-vocabulary.org/#",
    "vaem": "http://www.linkedmodel.org/schema/vaem#",
    "vann": "http://purl.org/vocab/vann/",
    "vcard": "http://www.w3.org/2006/vcard/ns#",
    "void": "http://rdfs.org/ns/void#",
    "vs": "http://www.w3.org/2003/06/sw-vocab-status/ns#",
    "wdr": "http://www.w3.org/2007/05/powder#",
    "wdrs": "http://www.w3.org/2007/05/powder-s#",
    "wgs": "http://www.w3.org/2003/01/geo/wgs84_pos#",
    "xhv": "http://www.w3.org/1999/xhtml/vocab#",
    "xkos": "http://rdf-vocabulary.ddialliance.org/xkos#",
    "xml": "http://www.w3.org/XML/1998/namespace/",
    "xsd": "http://www.w3.org/2001/XMLSchema",
}

prefixes_additional = {
    "fair": "https://w3id.org/fair/principles/terms/",
    "fip": "https://w3id.org/fair/fip/terms/",
}
prefixes_additional = merge(prefixes_additional, prefixes_doc)
for p, url in prefixes_additional.items():
    if p not in prefixes:
        prefixes[p] = url
    else:
        raise ValueError("DANGER: Attempt to clobber conventiional prefix!")

PUNCTUATION = "?.:;!-/'\")[],"


def get_known_uris(uri_pattern, localid_pfx="dfn-"):
    from bs4 import BeautifulSoup
    import requests
    html_doc = requests.get(uri_pattern).text
    soup = BeautifulSoup(html_doc, 'html.parser')
    localids = [
        tag.get("id") for tag in
        soup.find_all(lambda tag: tag.has_attr("id") and tag.get("id").startswith(localid_pfx))]
    return [(uri_pattern + '#' + id_) for id_ in localids]


KNOWN_URIS = set((Path(__file__).parent / "static" / "known_uris.txt").read_text().splitlines())

used_prefix = "|".join([f"(?:{k})" for k in prefixes.keys()])
curie_pattern = rf"({used_prefix}):([\w\-]+?)[^\w\-]"
newlines = []
expansions_to_check = {}
for line in lines_body:
    newline = line
    matches = list(re.finditer(curie_pattern, line))
    for m in matches:
        curie = m.group(0).rstrip().rstrip(PUNCTUATION)
        pfx, term = [g.rstrip().rstrip(PUNCTUATION) for g in m.groups()]
        url = prefixes.get(pfx) + term
        expansions_to_check[curie] = url
        if url in KNOWN_URIS:
            newline = newline.replace(
                curie,
                f'<a href="{url}">{curie}</a>',
                1
            )
        else:
            newline = newline.replace(
                curie,
                f'<a title="{url}" href="https://prefix.zazuko.com/{curie}">{curie}</a>',
                1
            )
    newlines.append(newline)


for curie, url in expansions_to_check.items():
    if url in KNOWN_URIS:
        continue

    r = requests.get(
        f"https://prefix.zazuko.com/api/v1/autocomplete?case=true&expand=true&q={curie}",
        allow_redirects=True,
        headers={"Accept": "application/json"}
    )
    r.raise_for_status()
    found = r.json()
    if not found:
        raise ValueError(f"no match for curie {curie}")
    assert found[0] == url, f"expansion of curie {curie} is disputed! Fetched: <{found[0]}>"


with open(filepath.replace(".ttld", ".md"), "w") as f:
    f.write("\n".join(lines_header + newlines))

