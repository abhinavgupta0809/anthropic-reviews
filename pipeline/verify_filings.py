"""Check every quote in analysis/filings.json against the saved S-1 text. Exits nonzero on a miss."""
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def normalize(text):
    text = text.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    text = re.sub(r"\s+", " ", text)
    return re.sub(r"\s+([,.;:])", r"\1", text).lower()


def main():
    source = ROOT / "data/filings/anthropic-s1-2026-10-26.txt"
    if not source.exists():
        print(f"Missing {source.name}; no check run")
        return 1
    filing = normalize(source.read_text(encoding="utf-8"))
    data = json.loads((ROOT / "analysis/filings.json").read_text(encoding="utf-8"))
    quotes = [row["quote"] for row in data["crosswalk"]] + data["support_quotes"]
    misses = [q for q in quotes if normalize(q) not in filing]
    print(f"{len(quotes) - len(misses)} of {len(quotes)} quotes matched")
    for miss in misses:
        print("MISS:", miss)
    return 1 if misses else 0


if __name__ == "__main__":
    sys.exit(main())
