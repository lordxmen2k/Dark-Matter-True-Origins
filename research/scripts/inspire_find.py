#!/usr/bin/env python3
"""
Resolve papers to identifiers via the INSPIRE-HEP literature API.

Crossref is excellent for astronomy and general journals, but it failed to
resolve three APS papers from 2025 onward because APS changed its DOI scheme
mid-year, and it does not index arXiv preprints at all. INSPIRE indexes both
and is the reference database for particle physics, so it is used here to
close the gaps that Crossref leaves.

Usage:
    python3 research/scripts/inspire_find.py "Exact paper title"
    python3 research/scripts/inspire_find.py --file titles.txt
"""
import json
import sys
import time
import urllib.parse
import urllib.request

API = "https://inspirehep.net/api/literature"


def query(title: str, size: int = 3):
    params = {"q": f'title "{title}"', "size": str(size)}
    url = API + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=45) as fh:
        return json.load(fh).get("hits", {}).get("hits", [])


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
        except Exception as exc:
            print("  LOOKUP FAILED:", exc)
            continue
        if not hits:
            print("  NO MATCH")
        for hit in hits:
            meta = hit.get("metadata", {})
            titles_ = [t.get("title", "") for t in meta.get("titles", [])]
            dois = meta.get("dois", [])
            arxiv = [a.get("value", "") for a in meta.get("arxiv_eprints", [])]
            print("  TITLE:", titles_[0] if titles_ else "?")
            print("  arXiv:", ", ".join(arxiv) or "-")
            print("  DOI:", ", ".join(d.get("value", "") for d in dois) or "-")
            print("  JOURNAL:", meta.get("journal_ref", "-"))
            print("  DOC-TYPE:", meta.get("document_type", "-"))
            auths = [a.get("full_name", "") for a in meta.get("authors", [])[:4]]
            if auths:
                print("  AUTHORS:", ", ".join(auths))
        time.sleep(1.0)


if __name__ == "__main__":
    main(sys.argv)
