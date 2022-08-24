from pathlib import Path
import re
import sys

import rdflib
import requests

filepath = sys.argv[1]
assert filepath.endswith(".md")

lines_raw = Path(filepath).read_text().splitlines()

lines = []
prefixes = {}
in_preamble = False
for line in lines_raw:
    if line == "---":
        in_preamble = not in_preamble
        continue
    if in_preamble:
        continue

    if m := re.fullmatch(r"@prefix ([^:]*): <([^<].+)> .", line):
        prefixes[m.group(1)] = m.group(2)
    else:
        lines.append(line)

known_prefix = "|".join([f"(?:{k})" for k in prefixes.keys()])
curie_pattern = rf"({known_prefix}):([\w\-]+?)[^\w\-]"
newlines = []
urls_to_check = set()
for line in lines:
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

for url in urls_to_check:
    r = requests.get(url, allow_redirects=True, headers={"Accept": "application/turtle"})
    r.raise_for_status()
    g = rdflib.Graph().parse(data=r.content, format="ttl")
    if rdflib.URIRef(url) not in g.subjects():
        raise Exception(f"{url} not resolved as text/turtle")

print(prefixes)
for line in newlines:
    print(line)



