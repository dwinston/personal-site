import os
import re
import subprocess
from pathlib import Path

import requests
from markdown import markdown, Markdown

BASE_URL = "https://api.buttondown.email/v1"

HEADERS = {"Authorization": f"Token {os.getenv('BUTTONDOWN_API_KEY')}"}


def post_email(filepath: str):
    url = BASE_URL + "/emails"
    raw_txt = Path(filepath).read_text()
    md = Markdown(extensions=["meta", "extra"])
    html = md.convert(raw_txt)
    subject = md.Meta["title"][0].strip("\"'")
    rv = requests.post(url, headers=HEADERS, json={"body": html, "subject": subject})
    rv.raise_for_status()


def posts_upserted():
    return subprocess.check_output(
        "git diff --name-only HEAD~1 HEAD -- content/posts/*.md", shell=True
    ).decode().splitlines()


def was_published(filepath: str):
    return bool(
        subprocess.check_output(
            "git diff HEAD~1 HEAD -- " + filepath + " grep '+draft: false'", shell=True
        ).strip()
    )


if __name__ == "__main__":
    for post in posts_upserted():
        if was_published(post):
            print("Emailing ", post)
            post_email(post)
