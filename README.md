# Credspin

An elimination roulette wheel with a Western problem. Round up your options, give the wheel a
turn, and every spin knocks one out — whoever's still standin' at the end takes the pot.

**Live:** https://maazale.github.io/Credspin/

## What it does

- Add options one at a time, or paste a whole roster (newline / comma separated)
- **Credminds crew** loads the team in one click
- Every draw eliminates the option under the pointer; the remaining slices smoothly re-flow to fill the wheel
- Last one standin' gets the poster, the harmonica and a rematch
- Boot Hill knockout history, showdown counter, shuffle, and reset
- Board state persists in `localStorage`

## The look

Sundown in the territory — a banded sun sinking behind layered mesas, saguaro silhouettes,
drifting dust and tumbleweeds rolling the horizon.

- Tooled-leather panels with brass rivets, swinging in like saloon doors
- Wagon-wheel canvas: saddle-stud rim, brass pegs, revolver-cylinder hub
- Brass cartridge pointer that kicks off every peg
- The logo wears a cowboy hat — and tips it when you hover
- Eliminations arrive as a nailed-up **WANTED** poster, shot through with bullet holes
- Muzzle flash and screen recoil on every kill

## Portraits

Every contender gets a face on the wanted poster, on their chip in The Posse, and on their
marker in Boot Hill.

- Drop a **lowercase** file into `portraits/` named after the contender — `ahmad.jpg`,
  `mary-sue.png` — and it's picked up automatically (`.jpg`, `.jpeg`, `.png`, `.webp`)
- Or click any contender's frame in The Posse to attach a photo from your machine; it's
  cropped to 220×264 and kept in `localStorage`
- Anyone without a photo rides as **"this person is missing"** — a `?` over a hatted
  silhouette, which is a perfectly respectable look for a wanted poster

Sources live in `wanted images/`; `python3 tools/make-portraits.py` rebuilds `portraits/`
from them. See [`portraits/README.md`](portraits/README.md) for the naming rules.

## Sound

- Background cowboy standoff theme on a loop, ducked while the wheel spins, toggleable
- Effects synthesized live in WebAudio: dry cylinder clicks per peg, a six-shooter report with
  low thump and ricochet tail, and a lonesome harmonica for the survivor

## Details

- Single self-contained `index.html` — no build step, no dependencies, no bundler
- Canvas wheel with an eased 4–6s spin and slices that tween into place
- Confetti engine throwing gold coins, sheriff stars and casings
- Responsive down to narrow phones, and respects `prefers-reduced-motion`

## Running it

Open `index.html` in a browser. That's it. (The theme needs
`Cowboy Standoff Music Sound Effect.mp3` sitting next to it.)

---

Built by [Credminds](https://www.credminds.com/).
