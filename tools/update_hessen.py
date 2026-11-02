#!/usr/bin/env python3
"""Hessen Mobil feeds to same-origin public snapshots; no personal locations stored."""
import json
import os
import pathlib
import urllib.request
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent
DEST = ROOT / "data"
DEST.mkdir(exist_ok=True)
FEEDS = {
    "hessen-roadworks": "https://verkehrsservice.hessen.de/syncdata/poiroadworks.json",
    "hessen-daily": "https://verkehrsservice.hessen.de/syncdata/poidora.json",
}

def utc_now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")

def fetch(url):
    request = urllib.request.Request(url, headers={
        "Accept": "application/json",
        "User-Agent": "StreckenRadar/0.5 (+https://github.com/bernd72/StreckenRadar)",
    })
    with urllib.request.urlopen(request, timeout=35) as response:
        payload = response.read(8_000_001)
        if len(payload) > 8_000_000:
            raise ValueError("Feed unexpectedly large")
        data = json.loads(payload.decode("utf-8-sig"))
        if not isinstance(data, dict) or not isinstance(data.get("features"), list):
            raise ValueError("Unexpected JSON: expected GeoJSON features array")
        lm = response.headers.get("Last-Modified")
        return data, lm

def main():
    successes = 0
    for name, url in FEEDS.items():
        file = DEST / (name + ".json")
        prior = {}
        if file.exists():
            try:
                prior = json.loads(file.read_text(encoding="utf-8"))
            except (ValueError, OSError):
                pass
        now = utc_now()
        document = {
            "source": "Verkehrsservice Hessen / Hessen Mobil",
            "source_url": url,
            "checked_at": now,
            "success": False,
            "upstream_last_modified": None,
            "data": None,
        }
        try:
            payload, modified = fetch(url)
            document.update(success=True, upstream_last_modified=modified, data=payload)
            successes += 1
            print(name, "success:", len(payload["features"]), "features", "modified", modified)
        except Exception as exc:
            document["error"] = str(exc)[:160]
            # Keep prior payload for offline analysis only. The app must not treat it as current.
            print(name, "FAILED:", type(exc).__name__, str(exc)[:160])
        file.write_text(json.dumps(document, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    if not successes:
        print("No Hessen feeds available; status snapshots still updated so the app can report errors.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
