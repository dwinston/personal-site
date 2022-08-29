from pathlib import Path
import re
import sys

from rdflib import Graph
from rdflib.namespace import NamespaceManager
import rdflib.namespace
import requests

filepath = sys.argv[1]
assert filepath.endswith(".ttld")

all_ns = rdflib.namespace._NAMESPACE_PREFIXES_CORE

lines_raw = Path(filepath).read_text().splitlines()

lines_header = []
lines_body = []
prefixes = {}
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
        prefixes[m.group(1)] = m.group(2)
    else:
        lines_body.append(line)

used_prefix = "|".join([f"(?:{k})" for k in prefixes.keys()])
curie_pattern = rf"({used_prefix}):([\w\-]+?)[^\w\-]"
newlines = []
urls_to_check = set()
for line in lines_body:
    newline = line
    matches = list(re.finditer(curie_pattern, line))
    for m in matches:
        curie = m.group(0)
        pfx, term = m.groups()
        url = prefixes[pfx] + term
        urls_to_check.add(url)
        newline = newline.replace(
            curie,
            f'<a href="{url}">{curie}</a>',
            1
        )
    newlines.append(newline)

g = Graph()
namespace_manager = NamespaceManager(Graph())
g.namespace_manager = g.namespace_manager
all_ns = [n for n in g.namespace_manager.namespaces()]
# print(all_ns)

for url in urls_to_check:
    print(g.namespace_manager.qname(url))
    # r = requests.get(url, allow_redirects=True, headers={"Accept": "application/turtle"})
    # r.raise_for_status()
    # g = rdflib.Graph().parse(data=r.content, format="ttl")
    # if rdflib.URIRef(url) not in g.subjects():
    #     raise Exception(f"{url} not resolved as text/turtle")

# print(prefixes)
# for line in newlines:
#     print(line)



