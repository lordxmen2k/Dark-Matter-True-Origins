#!/usr/bin/env python3
"""
Look up DOIs by title against the Crossref bibliographic query API.

arXiv covers the preprints; a great many of the sources this book leans on
are published articles with no arXiv version (the Bullet Cluster paper, the
DESI data releases, the early-detection papers). Their identifiers must be
looked up the same way: by title, against the registry, never from memory.

Usage:
    python3 research/scripts/crossref_find.py "Title of the paper"
    python3 research/scripts/crossref_find.py --file titles.txt
"""
import json
import sys
import time
import urllib.parse
import urllib.request

API = "https://api.crossref.org/works"
POLITE = "Dark-Matter-True-Origins/1.0 (mailto:editorial@ticointernet.example)"


def query(title: str, rows: int = 4):
    params = {
        "query.bibliographic": title,
        "rows": str(rows),
        "select": "DOI,title,author,container-title,issued,volume,page,type,is-referenced-by-count",
        "mailto": "editorial@ticointernet.example",
    }
    req = urllib.request.Request(
        API + "?" + urllib.parse.urlencode(params),
        headers={"User-Agent": POLITE},
    )
    with urllib.request.urlopen(req, timeout=45) as fh:
        data = json.load(fh)
    return data["message"]["items"]


def main(argv):
    titles = []
    if len(argv) > 1 and argv[1] == "--file":
        with open(argv[2], encoding="utf-8") as fh:
            titles = [line.strip() for line in fh if line.strip() and not line.startswith("#")]
    else:
        titles = argv[1:]

    for title in titles:
        print("=" * 78)
        print("QUERY:", title)
        try:
            items = query(title)
        except Exception as exc:
            print("  LOOKUP FAILED:", exc)
            continue
        if not items:
            print("  NO MATCH")
        for it in items:
            t = " ".join((it.get("title") or ["?"])[0].split())
            c = (it.get("container-title") or [""])[0]
            issued = it.get("issued", {}).get("date-parts", [[None]])[0]
            year = issued[0] if issued and issued[0] else "?"
            authors = ", ".join(
                f"{a.get('family','?')}" for a in (it.get("author") or [])[:3]
            )
            print(f"  DOI: {it.get('DOI','')}")
            print(f"    {t}")
            print(f"    {authors} | {c} | {year} | vol {it.get('volume','')} p {it.get('page','')}")
        time.sleep(1.0)


if __name__ == "__main__":
    main(sys.argv)
