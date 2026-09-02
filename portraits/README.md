# Portraits

Web-ready faces for the wanted posters. Credspin looks in here automatically — no config,
no rebuild.

## Naming

Lowercase the contender's name and turn every run of non-alphanumeric characters into a
single hyphen. `Mary-Sue O'Brien` → `mary-sue-o-brien`.

Filenames **must be lowercase** — GitHub Pages is case-sensitive, so `Ahmad.jpg` would not
be found even though it works on a Mac.

Extensions are tried in this order: `.jpg`, `.jpeg`, `.png`, `.webp`

## Shape

Roughly 3:4 portrait — the frame crops to fill, centred. 450×600 is plenty; the frame is
156×188 CSS px, so that covers a 2× display with room to spare.

## Regenerating from the originals

The full-size sources live in `../wanted images/`. Rebuild this folder with:

```sh
python3 tools/make-portraits.py
```

It crops each source to 3:4, downscales to 450×600 with Lanczos, and writes a lowercase
JPEG named after the contender's slug. ~3 MB of PNGs becomes ~230 KB of JPEGs.

Faces that don't sit centred in their source get an entry in the script's `FACE_X` map
(name → x of the face centre in the original), so the crop follows the face instead of the
frame. `Maaz` is the current example.

> `sips -c` only ever crops from the centre — its `--cropOffset` flag is silently ignored
> for this — which is why the build uses Pillow.

## No file? No problem

Click any contender's frame in The Posse to attach a photo from your machine. It's cropped
and downscaled to 220×264 and kept in `localStorage`, so it survives a reload on that
browser but isn't committed anywhere.

Anyone still without a face rides as **"this person is missing"** — a `?` over a hatted
silhouette, which is a perfectly respectable look for a wanted poster.
