#!/usr/bin/env python3
"""Synchronize course module downloads from their canonical sources.

Download URLs stay under _static/notebooks/. This local export does not deploy
anything. Only the kinetics module, not its notebooks, is newly exported.
"""
from __future__ import annotations

import argparse
from pathlib import Path

REPOSITORY = Path(__file__).resolve().parents[2]
NAMES = ("lesson_23.ipynb", "lesson_24.ipynb", "ne630_depletion.py", "ne630_kinetics.py")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="check without writing")
    args = parser.parse_args()
    # Read all inputs before changing any export.
    exports = [(REPOSITORY / "site/_static/notebooks" / name,
                ((REPOSITORY / "code" / name) if (REPOSITORY / "code" / name).is_file()
                 else (REPOSITORY / "notebooks" / name)).read_bytes()) for name in NAMES]
    mismatches = []
    for destination, content in exports:
        if destination.is_file() and destination.read_bytes() == content:
            continue
        if args.check:
            mismatches.append(str(destination.relative_to(REPOSITORY)))
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(content)
    if mismatches:
        for name in mismatches:
            print(f"Missing or stale export: {name}")
        return 1
    print(f"{'Verified' if args.check else 'Synchronized'} {len(exports)} course downloads.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
