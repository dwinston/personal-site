import json
import sys
from pathlib import Path

import requests
import tqdm

filename_in = sys.argv[1]
assert filename_in.endswith(".json")
with open(filename_in) as f:
    fair_enabling_resources = json.load(f)

# docs_out = open("/Users/dwinston/fip_fers.jsonl", "w")
#
# filename_out = filename_in[:-5] + ".md"
# for fer in tqdm.tqdm(fair_enabling_resources):
#     url, name = fer["id"], fer["name"]
#     assert url.startswith("http")
#     r = requests.get(url, headers={"Accept": "application/ld+json"})
#     r.raise_for_status()
#     doc = r.json()
#     docs_out.write(json.dumps(doc) + "\n")
#
# docs_out.close()

from pprint import pprint

fers_info = []

# XXX I couldn't figure out how to load conneg'd RDF into rdflib, so the below is super hacky.

for fer, s_graphs in zip(
        fair_enabling_resources,
        Path("/Users/dwinston/fip_fers.jsonl").read_text().splitlines()
        ):
    fer_info = {"id": fer["id"]}
    graphs = json.loads(s_graphs)
    for g in graphs:
        if g["@id"].endswith("#assertion") and 'https://w3id.org/fair/fip/terms/Identifier-service' in g["@graph"][0]["@type"]:
            fer_info["label"] = g["@graph"][0]["http://www.w3.org/2000/01/rdf-schema#label"][0]["@value"]
            fer_info["comment"] = g["@graph"][0]["http://www.w3.org/2000/01/rdf-schema#comment"][0][
                "@value"]
            fers_info.append(fer_info)

for fer_info in fers_info:
    print(f'- [{fer_info["label"]}]({fer_info["id"]})\n\n  {fer_info["comment"]}\n\n')
