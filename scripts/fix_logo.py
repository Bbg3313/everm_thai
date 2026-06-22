# -*- coding: utf-8 -*-
"""Build transparent EVERM Surgery Clinic logo PNGs from black-background master."""
from __future__ import annotations

from collections import deque
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "images" / "logo-source.png"
OUT = ROOT / "images" / "logo.png"
OUT_2X = ROOT / "images" / "logo@2x.png"

SUBTITLE_X = 360
SUBTITLE_Y = 205


def is_black(r: int, g: int, b: int) -> bool:
    return r < 16 and g < 16 and b < 16


def is_blue(r: int, g: int, b: int) -> bool:
    return b >= 40 and b > r + 10


def is_grey(r: int, g: int, b: int) -> bool:
    avg = (r + g + b) / 3
    spread = max(r, g, b) - min(r, g, b)
    return 50 <= avg <= 150 and spread <= 40


def is_colored(r: int, g: int, b: int) -> bool:
    return is_blue(r, g, b) or is_grey(r, g, b) or max(r, g, b) >= 20


def flood_edge_black(im: Image.Image) -> list[list[bool]]:
    w, h = im.size
    px = im.load()
    bg = [[False] * w for _ in range(h)]
    q: deque[tuple[int, int]] = deque()

    for x in range(w):
        for y in (0, h - 1):
            if is_black(*px[x, y]):
                q.append((x, y))
    for y in range(h):
        for x in (0, w - 1):
            if is_black(*px[x, y]):
                q.append((x, y))

    while q:
        x, y = q.popleft()
        if x < 0 or y < 0 or x >= w or y >= h or bg[y][x]:
            continue
        if not is_black(*px[x, y]):
            continue
        bg[y][x] = True
        q.extend([(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)])
    return bg


def near_blue(im: Image.Image, x: int, y: int, radius: int = 6) -> bool:
    px = im.load()
    w, h = im.size
    for yy in range(max(0, y - radius), min(h, y + radius + 1)):
        for xx in range(max(0, x - radius), min(w, x + radius + 1)):
            if is_blue(*px[xx, yy]):
                return True
    return False


def build_transparent_logo(raw: Image.Image) -> Image.Image:
    src = raw.convert("RGB")
    w, h = src.size
    px = src.load()
    bg = flood_edge_black(src)

    out = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    op = out.load()
    for y in range(h):
        for x in range(w):
            r, g, b = px[x, y]
            if is_colored(r, g, b):
                op[x, y] = (r, g, b, 255)
                continue
            if not is_black(r, g, b):
                continue
            if y >= SUBTITLE_Y and x >= SUBTITLE_X:
                continue
            if not bg[y][x] or near_blue(src, x, y):
                op[x, y] = (35, 24, 21, 255)

    bbox = out.getbbox()
    return out.crop(bbox) if bbox else out


def trim_pad(im: Image.Image, pad: int = 8) -> Image.Image:
    bbox = im.getbbox()
    if not bbox:
        return im
    x1, y1, x2, y2 = bbox
    return im.crop(
        (
            max(0, x1 - pad),
            max(0, y1 - pad),
            min(im.width, x2 + pad),
            min(im.height, y2 + pad),
        )
    )


def main() -> None:
    if not SOURCE.is_file():
        raise SystemExit(f"Source not found: {SOURCE}")

    logo = trim_pad(build_transparent_logo(Image.open(SOURCE)), pad=6)
    logo.save(OUT, "PNG", optimize=True)

    logo_2x = logo.resize((logo.width * 2, logo.height * 2), Image.Resampling.LANCZOS)
    logo_2x.save(OUT_2X, "PNG", optimize=True)
    print("Saved", OUT, logo.size, "mode=RGBA transparent")


if __name__ == "__main__":
    main()
