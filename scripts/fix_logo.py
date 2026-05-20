# -*- coding: utf-8 -*-
"""Transparent logo from user master file — no white box, minimal touch-up."""
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


def is_background(r, g, b, a):
    if a < 10:
        return True
    if r > 238 and g > 238 and b > 238:
        return True
    if r > 230 and g > 230 and b > 234 and max(r, g, b) - min(r, g, b) < 12:
        return True
    return False


def is_black_artifact(r, g, b, a):
    return a > 180 and r < 35 and g < 35 and b < 35


def fix_black_artifacts(im):
    w, h = im.size
    px = im.load()
    x0 = int(w * 0.38)
    for _ in range(3):
        for y in range(1, h - 1):
            for x in range(x0, w - 1):
                r, g, b, a = px[x, y]
                if not is_black_artifact(r, g, b, a):
                    continue
                neighbors = []
                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nr, ng, nb, na = px[x + dx, y + dy]
                    if na > 180 and nr > 110 and ng > 110 and nb > 115:
                        neighbors.append((nr, ng, nb))
                if len(neighbors) >= 2:
                    px[x, y] = (
                        sum(c[0] for c in neighbors) // len(neighbors),
                        sum(c[1] for c in neighbors) // len(neighbors),
                        sum(c[2] for c in neighbors) // len(neighbors),
                        a,
                    )
    return im


def flood_transparent(im):
    w, h = im.size
    px = im.load()
    seen = [[False] * w for _ in range(h)]
    q = deque()
    for x in range(w):
        for y in (0, h - 1):
            if is_background(*px[x, y]):
                q.append((x, y))
    for y in range(h):
        for x in (0, w - 1):
            if is_background(*px[x, y]):
                q.append((x, y))
    while q:
        x, y = q.popleft()
        if x < 0 or y < 0 or x >= w or y >= h or seen[y][x]:
            continue
        c = px[x, y]
        if not is_background(*c):
            continue
        seen[y][x] = True
        px[x, y] = (c[0], c[1], c[2], 0)
        q.extend([(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)])
    return im


def trim_alpha(im, pad=2):
    bbox = im.getbbox()
    if not bbox:
        return im
    x1, y1, x2, y2 = bbox
    return im.crop(
        (max(0, x1 - pad), max(0, y1 - pad), min(im.width, x2 + pad), min(im.height, y2 + pad))
    )


def main():
    raw = Image.open(SOURCE).convert("RGBA")
    ARCHIVE.parent.mkdir(parents=True, exist_ok=True)
    raw.save(ARCHIVE, "PNG")

    # 2x only — keeps edges sharp, avoids upscale blur
    im = raw.resize((raw.width * 2, raw.height * 2), Image.Resampling.LANCZOS)
    im = fix_black_artifacts(im)
    im = flood_transparent(im)
    im = trim_alpha(im, pad=4)

    im.save(OUT, "PNG")
    im2 = im.resize((im.width * 2, im.height * 2), Image.Resampling.LANCZOS)
    im2.save(OUT_2X, "PNG")
    print("Saved", OUT, im.size)


if __name__ == "__main__":
    main()
