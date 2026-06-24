# -*- coding: utf-8 -*-
"""Sync index.html Thai fallback text from js/i18n-data.js (th pack)."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "js" / "i18n-data.js"
INDEX = ROOT / "index.html"

ATTR_MAP = {
    "data-i18n-html": "inner",
    "data-i18n": "inner",
    "data-i18n-placeholder": "placeholder",
    "data-i18n-aria": "aria-label",
    "data-i18n-alt": "alt",
    "data-i18n-title": "title",
}


def load_th_pack() -> dict[str, str]:
    text = I18N.read_text(encoding="utf-8")
    start = text.index("  th: {")
    end = text.index("\n  }\n};", start)
    block = text[start:end]
    pack: dict[str, str] = {}
    for match in re.finditer(r'\n    ([a-zA-Z0-9_]+): ("(?:\\.|[^"\\])*")', block):
        pack[match.group(1)] = json.loads(match.group(2))
    return pack


def sync_index(pack: dict[str, str]) -> int:
    html = INDEX.read_text(encoding="utf-8")
    count = 0

    for attr, mode in ATTR_MAP.items():
        pattern = rf'<([^>]+)\b{attr}="([a-zA-Z0-9_]+)"([^>]*)>'
        for match in re.finditer(pattern, html):
            key = match.group(2)
            value = pack.get(key)
            if value is None:
                continue
            full_open = match.group(0)
            tag_name = match.group(1).split()[0]

            if mode != "inner":
                attrs = match.group(1) + attr + f'="{key}"' + match.group(3)
                attrs = re.sub(rf'\s{mode}="[^"]*"', "", attrs)
                new_open = f"<{attrs.strip()} {mode}=\"{value}\">"
                html = html.replace(full_open, new_open, 1)
                count += 1
                continue

            close = f"</{tag_name}>"
            close_idx = html.find(close, match.end())
            if close_idx == -1:
                continue
            html = html[: match.end()] + value + html[close_idx:]
            count += 1

    INDEX.write_text(html, encoding="utf-8")
    return count


def main() -> None:
    pack = load_th_pack()
    print("synced", sync_index(pack), "nodes")


if __name__ == "__main__":
    main()
