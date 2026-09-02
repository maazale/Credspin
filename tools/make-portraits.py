#!/usr/bin/env python3
"""Rebuild portraits/ from the full-size sources in "wanted images/".

Crops each source to 3:4, downscales to 450x600 and saves a lowercase JPEG
named after the contender's slug — the same slug index.html computes.
"""
import os, re, sys
from PIL import Image

SRC, DST = 'wanted images', 'portraits'
W, H, QUALITY = 450, 600, 82

# faces that sit off-centre: name -> x of the face centre in the source
FACE_X = {'Maaz': 370}

def slugify(s):
    return re.sub(r'^-+|-+$', '', re.sub(r'[^a-z0-9]+', '-', s.lower().strip()))

def main():
    os.makedirs(DST, exist_ok=True)
    total = 0
    for fn in sorted(os.listdir(SRC)):
        if not fn.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            continue
        name = os.path.splitext(fn)[0]
        im = Image.open(os.path.join(SRC, fn)).convert('RGB')
        w, h = im.size
        cw = int(h * W / H)
        if cw <= w:                                  # crop the sides
            cx = FACE_X.get(name, w // 2)
            left = max(0, min(w - cw, cx - cw // 2))
            im = im.crop((left, 0, left + cw, h))
        else:                                        # too narrow: crop top/bottom
            ch = int(w * H / W)
            top = max(0, (h - ch) // 2)
            im = im.crop((0, top, w, top + ch))
        out = os.path.join(DST, slugify(name) + '.jpg')
        im.resize((W, H), Image.LANCZOS).save(out, 'JPEG', quality=QUALITY, optimize=True)
        size = os.path.getsize(out); total += size
        print('%-14s -> %-22s %6.1f KB' % (fn, out, size / 1024))
    print('total: %.1f KB' % (total / 1024))

if __name__ == '__main__':
    sys.exit(main())
