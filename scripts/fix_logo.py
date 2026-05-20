# -*- coding: utf-8 -*-
"""Rebuild transparent logo from user master — white edge flood only, repair text artifacts."""
from __future__ import annotations

from collections import deque
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SOURCE = Path(
    r"C:\Users\MSI\.cursor\projects\c-Users-MSI-Desktop\assets"
    r"\c__Users_MSI_AppData_Roaming_Cursor_User_workspaceStorage_426432740231e226486de95245d8a725_images"
    r"_image-b5da086b-2859-41ac-8753-80a5e76b3ebb.png"
)
OUT = ROOT / "images" / "logo.png"
OUT_2X = ROOT / "images" / "logo@2x.png"
ARCHIVE = ROOT / "images" / "logo-source.png"

# Brand grey from SURGERY CLINIC lettering
TEXT_GREY = (80, 80, 80)


def is_panel_white(r: int, g: int, b: int, a: int) -> bool:
    if a < 8:
        return True
    return r > 235 and g > 235 and b > 235


def is_letter_grey(r: int, g: int, b: int, a: int) -> bool:
    if a < 120:
        return False
    return 55 < r < 140 and 55 < g < 140 and 55 < b < 140 and max(r, g, b) - min(r, g, b) < 25


def is_black_artifact(r: int, g: int, b: int, a: int) -> bool:
    if a < 100:
        return False
    return r < 48 and g < 48 and b < 48


def flood_panel_transparent(im: Image.Image) -> Image.Image:
    w, h = im.size
    px = im.load()
    seen = [[False] * w for _ in range(h)]
    q: deque[tuple[int, int]] = deque()

    for x in range(w):
        for y in (0, h - 1):
            if is_panel_white(*px[x, y]):
                q.append((x, y))
    for y in range(h):
        for x in (0, w - 1):
            if is_panel_white(*px[x, y]):
                q.append((x, y))

    while q:
        x, y = q.popleft()
        if x < 0 or y < 0 or x >= w or y >= h or seen[y][x]:
            continue
        c = px[x, y]
        if not is_panel_white(*c):
            continue
        seen[y][x] = True
        px[x, y] = (255, 255, 255, 0)
        q.extend([(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)])
    return im


def repair_surgery_artifacts(im: Image.Image) -> Image.Image:
    w, h = im.size
    px = im.load()
    x0 = int(w * 0.34)
    y0 = int(h * 0.52)
    y1 = int(h * 0.98)

    for y in range(y0, y1):
        for x in range(x0, w):
            r, g, b, a = px[x, y]
            if not is_black_artifact(r, g, b, a):
                continue
            greys: list[tuple[int, int, int]] = []
            for dx in range(-3, 4):
                for dy in range(-3, 4):
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if nx < 0 or ny < 0 or nx >= w or ny >= h:
                        continue
                    nr, ng, nb, na = px[nx, ny]
                    if is_letter_grey(nr, ng, nb, na):
                        greys.append((nr, ng, nb))
            if greys:
                px[x, y] = (
                    sum(c[0] for c in greys) // len(greys),
                    sum(c[1] for c in greys) // len(greys),
                    sum(c[2] for c in greys) // len(greys),
                    a,
                )
            else:
                px[x, y] = (*TEXT_GREY, a)
    return im


def trim_alpha(im: Image.Image, pad: int = 6) -> Image.Image:
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


def build_from_source(raw: Image.Image, scale: int) -> Image.Image:
    if scale > 1:
        raw = raw.resize((raw.width * scale, raw.height * scale), Image.Resampling.LANCZOS)
    im = raw.convert("RGBA")
    im = repair_surgery_artifacts(im)
    im = flood_panel_transparent(im)
    return trim_alpha(im, pad=8)


def main() -> None:
    if not SOURCE.is_file():
        raise SystemExit(f"Source not found: {SOURCE}")

    raw = Image.open(SOURCE).convert("RGBA")
    ARCHIVE.parent.mkdir(parents=True, exist_ok=True)
    raw.save(ARCHIVE, "PNG")

    logo_1x = build_from_source(raw, scale=4)
    logo_1x.save(OUT, "PNG", optimize=True)

    logo_2x = logo_1x.resize(
        (logo_1x.width * 2, logo_1x.height * 2), Image.Resampling.LANCZOS
    )
    logo_2x.save(OUT_2X, "PNG", optimize=True)

    # Verify transparency (corners should be alpha 0)
    px = logo_1x.load()
    corners = [px[0, 0][3], px[logo_1x.width - 1, 0][3], px[0, logo_1x.height - 1][3]]
    print("Saved", OUT, logo_1x.size, "corner alpha:", corners)


if __name__ == "__main__":
    main()
