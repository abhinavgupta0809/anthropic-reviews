"""Add newly scraped reviews to the kept corpus without changing any existing row.

Existing rows stay byte for byte. Only reviews newer than the previous run time are added.
The site builds its analysis on the 90-day window ending at the new run time (build_site_data.py);
older rows stay in the CSVs and on the Reviews tab.
"""
import argparse
from collections import Counter
import csv
import io
import json
from pathlib import Path

from . import config
from .common import ScrapeError, atomic_text, cli, dt, read_json, validate_row, write_json


def new_rows(scraped, existing_ids, previous_run, run_time):
    unique = {}
    for row in scraped:
        validate_row(row)
        if (row["review_text"].strip() and row["review_id"] not in existing_ids
                and dt(previous_run) < dt(row["timestamp"]) <= dt(run_time)):
            unique.setdefault(row["review_id"], row)
    return sorted(unique.values(), key=lambda r: (r["timestamp"], r["review_id"]))


def extend(data_dir, source_dir, since=None):
    """since: also add reviews from this time on that the earlier scrape missed (store feeds publish late)."""
    manifest, source = read_json(data_dir / "run.json"), read_json(source_dir / "run.json")
    previous, run_time = manifest["run_time_utc"], source["run_time_utc"]
    if dt(run_time) <= dt(previous) and not since:
        raise ScrapeError("New run time is not after the current run time")
    for name in ("play", "appstore"):
        if not read_json(source_dir / "interim" / f"{name}.meta.json").get("complete"):
            raise ScrapeError(f"{name}: scrape is not complete")
    raw_path = data_dir / "raw_reviews.csv"
    old_bytes = raw_path.read_bytes()
    with raw_path.open(encoding="utf-8", newline="") as handle:
        old = list(csv.DictReader(handle))
    scraped = []
    for name in ("play", "appstore"):
        with (source_dir / "interim" / f"{name}.jsonl").open(encoding="utf-8") as handle:
            scraped.extend(json.loads(line) for line in handle)
    added = new_rows(scraped, {r["review_id"] for r in old}, since or previous, run_time)
    if not added:
        raise ScrapeError("No new reviews; nothing written")
    buffer = io.StringIO(newline="")
    csv.DictWriter(buffer, fieldnames=config.COLUMNS).writerows(added)
    raw_path.write_bytes(old_bytes + buffer.getvalue().encode("utf-8"))
    daily = Counter((r["platform"], r["date_utc"]) for r in [*old, *added])
    with atomic_text(data_dir / "daily_true_counts.csv") as handle:
        writer = csv.writer(handle)
        writer.writerow(("platform", "date_utc", "count"))
        writer.writerows((p, d, n) for (p, d), n in sorted(daily.items()))
    if not since:
        history = [*manifest.get("previous_runs", []), previous]
        write_json(data_dir / "run.json", {**manifest, "run_time_utc": run_time, "previous_runs": history})
    counts = Counter(r["platform"] for r in added)
    with (data_dir / "volume_report.md").open("a", encoding="utf-8") as handle:
        handle.write(f"\n## Extension to {run_time}\n\nAdded {len(added)} reviews newer than {since or previous} "
                     f"(android {counts['android']}, ios {counts['ios']}). Kept corpus: {len(old) + len(added)}. "
                     f"Newest review: {added[-1]['timestamp']}.\n")
    print(f"Kept {len(old)} existing rows unchanged; added {len(added)}: {dict(counts)}; run time {run_time}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", type=Path, default=config.DATA_DIR)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--since", help="UTC ISO time; backfill reviews from here that an earlier scrape missed")
    args = parser.parse_args()
    extend(args.data_dir, args.source, args.since)


if __name__ == "__main__":
    cli(main)
