#!/usr/bin/env python3
"""Check that every local link in the rendered Sphinx site resolves."""

from __future__ import annotations

import argparse
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class LinkCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attributes: list[tuple[str, str | None]]) -> None:
        attribute_name = "href" if tag in {"a", "link"} else "src" if tag in {"img", "script"} else None
        if attribute_name is None:
            return
        values = dict(attributes)
        value = values.get(attribute_name)
        if value:
            self.links.append(value)


def check_site(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []
    if not root.is_dir():
        return [f"rendered site directory does not exist: {root}"]
    if not (root / ".nojekyll").is_file():
        errors.append("rendered site is missing .nojekyll")

    for html_file in sorted(root.rglob("*.html")):
        parser = LinkCollector()
        parser.feed(html_file.read_text(encoding="utf-8"))
        for link in parser.links:
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc or link.startswith(("#", "mailto:", "data:", "javascript:")):
                continue
            path_text = unquote(parsed.path)
            if not path_text:
                continue
            if path_text.startswith("/"):
                target = root / path_text.lstrip("/")
            else:
                target = html_file.parent / path_text
            target = target.resolve()
            if root not in target.parents and target != root:
                errors.append(f"{html_file.relative_to(root)}: link escapes site root: {link}")
                continue
            if target.is_dir():
                target = target / "index.html"
            if not target.exists():
                errors.append(f"{html_file.relative_to(root)}: missing target for {link}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site_root", type=Path)
    arguments = parser.parse_args()
    errors = check_site(arguments.site_root)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print(f"Verified local links beneath {arguments.site_root}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
