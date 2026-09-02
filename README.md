# Credspin

An elimination roulette wheel. Add your options, spin, and the wheel knocks one out every round — whatever survives to the end is the winner.

**Live:** https://maazale.github.io/Credspin/

## What it does

- Add options one at a time, or paste a whole list (newline / comma separated)
- **Within Credminds** loads the team roster in one click
- Every spin eliminates the option under the pointer; the remaining slices smoothly re-flow to fill the wheel
- Last option standing gets the trophy, confetti, and a rematch button
- Knockout history, round counter, shuffle, and reset
- Board state persists in `localStorage`

## Details

- Single self-contained `index.html` — no build step, no dependencies, no bundler
- Canvas wheel with eased 4–6s spin, per-peg tick sounds, and a pointer that kicks off each boundary
- Background roulette theme synthesized live in WebAudio (no audio files), ducked while spinning, toggleable
- Confetti engine, animated aurora background, spring-in components
- Responsive to 390px, and respects `prefers-reduced-motion`

## Running it

Open `index.html` in a browser. That's it.

---

Built by [Credminds](https://www.credminds.com/).
