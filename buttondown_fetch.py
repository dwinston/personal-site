"""
Fetch latest email created from Buttondown API and template a post for it.

Intended that you need to set
```
draft: false
```
manually and also set e.g.
```
tags:
- society-of-FAIR
```
manually.

Usage: python buttondown_fetch.py
"""

from pprint import pprint
import os
import subprocess

import requests
from dotenv import load_dotenv

load_dotenv(".env")

BASE_URL = "https://api.buttondown.email/v1"

HEADERS = {"Authorization": f"Token {os.getenv('BUTTONDOWN_API_KEY')}"}


def list_emails():
    url = BASE_URL+"/emails"
    results = []
    while True:
        rv = requests.get(url, headers=HEADERS)
        if rv.status_code != 200:
            raise Exception(rv.text)
        rj = rv.json()
        results.extend(rj["results"])
        if rj.get("next"):
            url = rj.get("next")
        else:
            break

    return results


if __name__ == "__main__":
    emails = list_emails()
    latest_first = sorted(emails, key=lambda e: e["publish_date"], reverse=True)
    email = latest_first[0]
    filename = f"posts/{email['slug']}.md"
    subprocess.run(["hugo", "new", filename], check=True)
    with open(f"content/{filename}", 'a') as f:
        f.write(email['body'])
        f.write('\n')
        f.write('{{< subscribe >}}')
    print("created", filename)