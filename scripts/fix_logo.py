# -*- coding: utf-8 -*-
"""Build transparent EVERM Surgery Clinic assets (PNG + scalable SVG)."""
from __future__ import annotations

import base64
import io
import re
from collections import deque
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "images" / "logo-source.png"
OUT = ROOT / "images" / "logo.png"
OUT_2X = ROOT / "images" / "logo@2x.png"
OUT_SVG = ROOT / "images" / "logo.svg"
OUT_FOOTER_SVG = ROOT / "images" / "logo-footer.svg"
VECTOR_LIGHT = ROOT / "images" / ".logo-vector-light.svg"
VECTOR_FOOTER = ROOT / "images" / ".logo-vector-footer.svg"

SUBTITLE_X = 360
SUBTITLE_Y = 205
SUBTITLE_GREY_Y = 200

SVG_VIEWBOX = (1000, 332.63)


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


def subtitle_bbox(logo: Image.Image) -> tuple[int, int, int, int]:
    px = logo.load()
    xs: list[int] = []
    ys: list[int] = []
    for y in range(SUBTITLE_GREY_Y, logo.height):
        for x in range(logo.width):
            r, g, b, a = px[x, y]
            if a and is_grey(r, g, b):
                xs.append(x)
                ys.append(y)
    if not xs:
        return (380, 210, logo.width - 8, logo.height - 8)
    pad = 4
    return (
        max(0, min(xs) - pad),
        max(0, min(ys) - pad),
        min(logo.width, max(xs) + pad + 1),
        min(logo.height, max(ys) + pad + 1),
    )


def extract_subtitle(logo: Image.Image) -> Image.Image:
    x1, y1, x2, y2 = subtitle_bbox(logo)
    return logo.crop((x1, y1, x2, y2))


def goldize_subtitle(im: Image.Image) -> Image.Image:
    out = im.copy()
    px = out.load()
    for y in range(out.height):
        for x in range(out.width):
            r, g, b, a = px[x, y]
            if a < 8:
                continue
            lum = (r + g + b) / (3 * 255)
            px[x, y] = (
                int(140 + 90 * lum),
                int(110 + 70 * lum),
                int(60 + 50 * lum),
                a,
            )
    return out


def png_to_data_uri(im: Image.Image) -> str:
    buf = io.BytesIO()
    im.save(buf, format="PNG", optimize=True)
    encoded = base64.b64encode(buf.getvalue()).decode("ascii")
    return f"data:image/png;base64,{encoded}"


def map_logo_rect_to_svg(
    logo: Image.Image,
    rect: tuple[int, int, int, int],
) -> tuple[float, float, float, float]:
    x1, y1, x2, y2 = rect
    sx = SVG_VIEWBOX[0] / logo.width
    sy = SVG_VIEWBOX[1] / logo.height
    return (x1 * sx, y1 * sy, (x2 - x1) * sx, (y2 - y1) * sy)


def strip_vector_subtitle(svg: str) -> str:
    svg = re.sub(r'<path class="cls-6"[^/]*/>', "", svg)
    svg = re.sub(r"<title>[^<]*</title>", "<title>EVERM Surgery Clinic</title>", svg, count=1)
    return svg


def build_hybrid_svg(template: str, logo: Image.Image, subtitle: Image.Image, gold: bool = False) -> str:
    svg = strip_vector_subtitle(template)
    if gold:
        subtitle = goldize_subtitle(subtitle)
    x1, y1, x2, y2 = subtitle_bbox(logo)
    sx, sy, sw, sh = map_logo_rect_to_svg(logo, (x1, y1, x2, y2))
    href = png_to_data_uri(subtitle)
    image_tag = (
        f'<image href="{href}" x="{sx:.2f}" y="{sy:.2f}" '
        f'width="{sw:.2f}" height="{sh:.2f}" preserveAspectRatio="xMidYMid meet"/>'
    )
    return svg.replace("</svg>", f"{image_tag}</svg>")


def ensure_vector_templates() -> None:
    import subprocess

    if VECTOR_LIGHT.is_file() and VECTOR_FOOTER.is_file():
        return
    VECTOR_LIGHT.parent.mkdir(parents=True, exist_ok=True)
    for commit_path, dest in (
        ("1c064fe:images/logo.svg", VECTOR_LIGHT),
        ("1c064fe:images/logo-footer.svg", VECTOR_FOOTER),
    ):
        result = subprocess.run(
            ["git", "show", commit_path],
            cwd=ROOT,
            check=True,
            capture_output=True,
        )
        dest.write_bytes(result.stdout)


def main() -> None:
    if not SOURCE.is_file():
        raise SystemExit(f"Source not found: {SOURCE}")

    ensure_vector_templates()
    logo = trim_pad(build_transparent_logo(Image.open(SOURCE)), pad=6)
    subtitle = extract_subtitle(logo)

    logo.save(OUT, "PNG", optimize=True)
    logo.resize((logo.width * 2, logo.height * 2), Image.Resampling.LANCZOS).save(
        OUT_2X, "PNG", optimize=True
    )

    light_template = VECTOR_LIGHT.read_text(encoding="utf-8")
    footer_template = VECTOR_FOOTER.read_text(encoding="utf-8")
    OUT_SVG.write_text(build_hybrid_svg(light_template, logo, subtitle), encoding="utf-8")
    OUT_FOOTER_SVG.write_text(
        build_hybrid_svg(footer_template, logo, subtitle, gold=True),
        encoding="utf-8",
    )
    print("Saved", OUT, logo.size)
    print("Saved", OUT_SVG, OUT_FOOTER_SVG)


if __name__ == "__main__":
    main()
