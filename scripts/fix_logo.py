# -*- coding: utf-8 -*-
"""Rebuild EVERM logo assets from master PNG — transparent header + gold-frame footer."""
from __future__ import annotations

import base64
import io
from collections import deque
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent
SOURCE = Path(
    r"C:\Users\MSI\.cursor\projects\c-Users-MSI-Desktop\assets"
    r"\c__Users_MSI_AppData_Roaming_Cursor_User_workspaceStorage_empty-window_images"
    r"_image-fa6c81e8-da42-443b-9c15-44f70ec092ae.png"
)
ARCHIVE = ROOT / "images" / "logo-source.png"
OUT = ROOT / "images" / "logo.png"
OUT_2X = ROOT / "images" / "logo@2x.png"
OUT_SVG = ROOT / "images" / "logo.svg"
OUT_FOOTER = ROOT / "images" / "logo-footer.png"
OUT_FOOTER_SVG = ROOT / "images" / "logo-footer.svg"

VIEW_W = 1000
VIEW_H = 333


def is_bg(r: int, g: int, b: int, a: int) -> bool:
    if a < 8:
        return True
    return r < 28 and g < 28 and b < 28


def flood_bg_transparent(im: Image.Image) -> Image.Image:
    w, h = im.size
    px = im.load()
    seen = [[False] * w for _ in range(h)]
    q: deque[tuple[int, int]] = deque()

    for x in range(w):
        for y in (0, h - 1):
            if is_bg(*px[x, y]):
                q.append((x, y))
    for y in range(h):
        for x in (0, w - 1):
            if is_bg(*px[x, y]):
                q.append((x, y))

    while q:
        x, y = q.popleft()
        if x < 0 or y < 0 or x >= w or y >= h or seen[y][x]:
            continue
        c = px[x, y]
        if not is_bg(*c):
            continue
        seen[y][x] = True
        px[x, y] = (0, 0, 0, 0)
        q.extend([(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)])
    return im


def trim_alpha(im: Image.Image, pad: int = 4) -> Image.Image:
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


def build_logo(raw: Image.Image, scale: int = 1) -> Image.Image:
    im = raw.convert("RGBA")
    if scale > 1:
        im = im.resize((im.width * scale, im.height * scale), Image.Resampling.LANCZOS)
    im = flood_bg_transparent(im)
    return trim_alpha(im, pad=6)


def write_svg(path: Path, png: Image.Image, view_w: int, view_h: int) -> None:
    buf = io.BytesIO()
    png.save(buf, format="PNG", optimize=True)
    b64 = base64.b64encode(buf.getvalue()).decode("ascii")
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {view_w} {view_h}">
  <title>EVERM Surgery Clinic</title>
  <image xlink:href="data:image/png;base64,{b64}" x="0" y="0" width="{view_w}" height="{view_h}" preserveAspectRatio="xMidYMid meet"/>
</svg>
"""
    path.write_text(svg, encoding="utf-8")


def fit_to_view(im: Image.Image, view_w: int, view_h: int, pad_x: float = 0.04, pad_y: float = 0.08) -> Image.Image:
    canvas = Image.new("RGBA", (view_w, view_h), (0, 0, 0, 0))
    max_w = int(view_w * (1 - pad_x * 2))
    max_h = int(view_h * (1 - pad_y * 2))
    ratio = min(max_w / im.width, max_h / im.height)
    nw, nh = max(1, int(im.width * ratio)), max(1, int(im.height * ratio))
    resized = im.resize((nw, nh), Image.Resampling.LANCZOS)
    ox = (view_w - nw) // 2
    oy = (view_h - nh) // 2
    canvas.paste(resized, (ox, oy), resized)
    return canvas


def build_footer_logo(logo: Image.Image, view_w: int, view_h: int) -> Image.Image:
    """White-backed logo for dark footer; gold frame comes from existing .logo-footer CSS."""
    canvas = Image.new("RGBA", (view_w, view_h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(canvas)

    margin_x = int(view_w * 0.03)
    margin_y = int(view_h * 0.06)
    radius = 14

    draw.rounded_rectangle(
        (margin_x, margin_y, view_w - margin_x, view_h - margin_y),
        radius=radius,
        fill=(255, 255, 255, 255),
    )

    inner = fit_to_view(logo, view_w - margin_x * 2, view_h - margin_y * 2, pad_x=0.06, pad_y=0.12)
    inner_layer = Image.new("RGBA", (view_w, view_h), (0, 0, 0, 0))
    inner_layer.paste(inner, (margin_x, margin_y), inner)
    return Image.alpha_composite(canvas, inner_layer)


def main() -> None:
    if not SOURCE.is_file():
        raise SystemExit(f"Source not found: {SOURCE}")

    raw = Image.open(SOURCE).convert("RGBA")
    ARCHIVE.parent.mkdir(parents=True, exist_ok=True)
    raw.save(ARCHIVE, "PNG")

    logo = build_logo(raw, scale=1)
    logo.save(OUT, "PNG", optimize=True)

    logo_2x = logo.resize((logo.width * 2, logo.height * 2), Image.Resampling.LANCZOS)
    logo_2x.save(OUT_2X, "PNG", optimize=True)

    header_canvas = fit_to_view(logo, VIEW_W, VIEW_H)
    write_svg(OUT_SVG, header_canvas, VIEW_W, VIEW_H)

    footer_canvas = build_footer_logo(logo, VIEW_W, VIEW_H)
    footer_canvas.save(OUT_FOOTER, "PNG", optimize=True)
    write_svg(OUT_FOOTER_SVG, footer_canvas, VIEW_W, VIEW_H)

    print("Saved", OUT, logo.size)
    print("Saved", OUT_SVG)
    print("Saved", OUT_FOOTER)
    print("Saved", OUT_FOOTER_SVG)


if __name__ == "__main__":
    main()
