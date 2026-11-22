#!/usr/bin/env python3
"""
Look up arXiv identifiers by title.

The Uniworld book and the RH book both showed that an identifier recalled
from memory is more likely wrong than right. This script asks the arXiv API
for each title and prints the identifier, so that every citation in the
source ledger was looked up rather than remembered.

Usage:
    python3 research/scripts/arxiv_find.py "Title of the paper" "Another title"
    python3 research/scripts/arxiv_find.py --file titles.txt
"""
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

API = "http://export.arxiv.org/api/query"
NS = {"a": "http://www.w3.org/2005/Atom"}


def query(title: str, max_results: int = 5):
    params = {
        "search_query": f'ti:"{title}"',
        "start": 0,
        "max_results": max_results,
    }
    url = API + "?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url, timeout=45) as fh:
        body = fh.read()
    root = ET.fromstring(body)
    out = []
    for entry in root.findall("a:entry", NS):
        entry_title = " ".join(
            (entry.findtext("a:title", default="", namespaces=NS)).split()
        )
        entry_id = entry.findtext("a:id", default="", namespaces=NS)
        published = entry.findtext("a:published", default="", namespaces=NS)
        doi = entry.findtext("{http://arxiv.org/schemas/atom}doi", default="")
        journal = entry.findtext("{http://arxiv.org/schemas/atom}journal_ref", default="")
        out.append(
            {
                "title": entry_title,
                "id": entry_id.rsplit("/", 1)[-1],
                "published": published[:10],
                "doi": doi or "",
                "journal": journal or "",
            }
        )
    return out


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
            hits = query(title)
        except Exception as exc:  # network hiccup, not a reason to lose the list
            print("  LOOKUP FAILED:", exc)
            continue
        if not hits:
            print("  NO MATCH")
        for hit in hits:
            print(f"  arXiv:{hit['id']}  ({hit['published']})")
            print(f"    {hit['title']}")
            if hit["doi"]:
                print(f"    doi: {hit['doi']}")
            if hit["journal"]:
                print(f"    journal-ref: {hit['journal']}")
        time.sleep(3.0)  # arXiv asks for ~3 s between requests


if __name__ == "__main__":
    main(sys.argv)
