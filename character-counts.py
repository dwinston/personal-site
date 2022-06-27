"""
Usage: python character-counts.py content/posts/post-title.md
"""

import sys


def remove_header(lines):
    first_bar_found = False
    for i, line in enumerate(lines):
        if line.startswith("---"):
            if first_bar_found:
                return lines[i+1:]
            else:
                first_bar_found = True
    raise ValueError("header not found")


def paragraphs(lines):
    ps = []
    p_lines = []
    for line in lines:
        if line == '':
            ps.append(p_lines)
            p_lines = []
        else:
            p_lines.append(line)
    return ps


if __name__ == "__main__":
    _, filename = sys.argv
    with open(filename) as f:
        lines = [l.strip() for l in f]
    ps = paragraphs((remove_header(lines)))
    ps = [p for p in ps if p]
    p_lengths = [len(" ".join(p)) for p in ps]
    first_p_length, whole_post_length = p_lengths[0], sum(p_lengths) + len(ps)
    print("First paragraph length:", first_p_length, "chars.")
    print("Whole post length:", whole_post_length, "chars.")
    if first_p_length > 280:
        print("First paragraph not OK for Twitter (max 280 chars).")
    if whole_post_length > 3000:
        print("Post not OK for LinkedIn (max 3000 chars).")
