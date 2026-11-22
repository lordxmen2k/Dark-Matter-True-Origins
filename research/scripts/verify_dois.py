#!/usr/bin/env python3
"""
Verify a list of DOIs against the Crossref registry.

An identifier recalled from memory is more likely wrong than right, and a
wrong DOI in a book's notes is a silent, permanent error. This script asks
Crossref what each DOI actually resolves to and prints the title, so the
source ledger can record the verification status per entry.

Usage:
    python3 research/scripts/verify_dois.py dois.txt
    python3 research/scripts/verify_dois.py 10.1103/PhysRevLett.135.011802 ...
"""
import json
import sys
import time
import urllib.request

API = "https://api.crossref.org/works/"
HEADERS = {"User-Agent": "Dark-Matter-True-Origins/1.0 (mailto:editorial@ticointernet.example)"}


def check(doi: str):
    url = API + doi
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=40) as fh:
            msg = json.load(fh)["message"]
    except Exception as exc:
        return {"doi": doi, "status": "NOT FOUND", "detail": str(exc)}
    title = " ".join((msg.get("title") or ["?"])[0].split())
    container = (msg.get("container-title") or [""])[0]
    issued = msg.get("issued", {}).get("date-parts", [[None]])[0]
    year = issued[0] if issued and issued[0] else "?"
    authors = ", ".join(a.get("family", "?") for a in (msg.get("author") or [])[:3])
    return {
        "doi": doi,
        "status": "VERIFIED",
        "title": title,
        "container": container,
        "year": year,
        "authors": authors,
        "volume": msg.get("volume", ""),
        "page": msg.get("page", ""),
    }


def main(argv):
    dois = []
    if len(argv) > 1 and argv[1].endswith(".txt"):
        with open(argv[1], encoding="utf-8") as fh:
            dois = [line.strip() for line in fh if line.strip() and not line.startswith("#")]
    else:
        dois = argv[1:]

    ok = 0
    for doi in dois:
        res = check(doi)
        if res["status"] == "VERIFIED":
            ok += 1
            print(f"OK   {doi}")
            print(f"     {res['authors']} | {res['title']}")
            print(f"     {res['container']} ({res['year']}) {res['volume']} {res['page']}")
        else:
            print(f"FAIL {doi}  -- {res['detail']}")
        time.sleep(0.6)
    print(f"\n{ok}/{len(dois)} verified")


if __name__ == "__main__":
    main(sys.argv)
