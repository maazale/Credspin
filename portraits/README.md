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

The full-size sources live in `../wanted images/`. To rebuild this folder from them:

```sh
for f in "wanted images"/*.png; do
  base=$(basename "$f" .png)
  slug=$(echo "$base" | tr '[:upper:]' '[:lower:]' | sed -E 's/[^a-z0-9]+/-/g; s/^-+|-+$//g')
  sips -c 1024 768 "$f" --out /tmp/pc.png
  sips --resampleHeightWidth 600 450 /tmp/pc.png --out /tmp/pr.png
  sips -s format jpeg -s formatOptions 82 /tmp/pr.png --out "portraits/$slug.jpg"
done
```

That squeezes ~3.1 MB of PNGs down to ~400 KB of JPEGs.

## No file? No problem

Click any contender's frame in The Posse to attach a photo from your machine. It's cropped
and downscaled to 220×264 and kept in `localStorage`, so it survives a reload on that
browser but isn't committed anywhere.

Anyone still without a face rides as **"this person is missing"** — a `?` over a hatted
silhouette, which is a perfectly respectable look for a wanted poster.
