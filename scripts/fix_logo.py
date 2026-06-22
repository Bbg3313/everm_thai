# -*- coding: utf-8 -*-
"""Build EVERM Surgery Clinic logo PNGs from black-background master."""
from __future__ import annotations

from collections import deque
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "images" / "logo-source.png"
OUT = ROOT / "images" / "logo.png"
OUT_2X = ROOT / "images" / "logo@2x.png"
OUT_SVG = ROOT / "images" / "logo.svg"
OUT_FOOTER_SVG = ROOT / "images" / "logo-footer.svg"

VIEW_W = 1000
VIEW_H = 333


def is_black(r: int, g: int, b: int) -> bool:
    return r < 14 and g < 14 and b < 14


def is_content(r: int, g: int, b: int) -> bool:
    if not is_black(r, g, b):
        return True
    return False


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


def build_white_logo(raw: Image.Image) -> Image.Image:
    src = raw.convert("RGB")
    w, h = src.size
    px = src.load()
    bg = flood_edge_black(src)

    out = Image.new("RGBA", (w, h), (255, 255, 255, 255))
    op = out.load()
    for y in range(h):
        for x in range(w):
            r, g, b = px[x, y]
            if is_content(r, g, b) or (is_black(r, g, b) and not bg[y][x]):
                op[x, y] = (r, g, b, 255)

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


def fit_to_view(im: Image.Image, view_w: int, view_h: int) -> Image.Image:
    canvas = Image.new("RGBA", (view_w, view_h), (255, 255, 255, 255))
    pad_x, pad_y = 0.04, 0.08
    max_w = int(view_w * (1 - pad_x * 2))
    max_h = int(view_h * (1 - pad_y * 2))
    ratio = min(max_w / im.width, max_h / im.height)
    nw, nh = max(1, int(im.width * ratio)), max(1, int(im.height * ratio))
    resized = im.resize((nw, nh), Image.Resampling.LANCZOS)
    canvas.paste(resized, ((view_w - nw) // 2, (view_h - nh) // 2), resized)
    return canvas


def write_svg(path: Path, png_name: str) -> None:
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {VIEW_W} {VIEW_H}">
  <title>EVERM Surgery Clinic</title>
  <image href="{png_name}" x="0" y="0" width="{VIEW_W}" height="{VIEW_H}" preserveAspectRatio="xMidYMid meet"/>
</svg>
"""
    path.write_text(svg, encoding="utf-8")


def main() -> None:
    if not SOURCE.is_file():
        raise SystemExit(f"Source not found: {SOURCE}")

    logo = trim_pad(build_white_logo(Image.open(SOURCE)), pad=6)
    logo.save(OUT, "PNG", optimize=True)

    logo_2x = logo.resize((logo.width * 2, logo.height * 2), Image.Resampling.LANCZOS)
    logo_2x.save(OUT_2X, "PNG", optimize=True)

    write_svg(OUT_SVG, "logo.png")
    write_svg(OUT_FOOTER_SVG, "logo.png")
    print("Saved", OUT, logo.size)


if __name__ == "__main__":
    main()
