# AGENT.md — Museum of the Year 3000 entry

## What this is
A make.fun program entry for competition `u-donrulezz-museum-of-the-year-3000-b727a0bb`
("Museum of the Year 3000"). The program writes exactly one line — the museum
label a museum in the year 3000 puts beside an ordinary object from today —
to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).

## Run
```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```
Pure Python 3 standard library only (`os` import). No network, no secrets,
no environment-driven content: the entry text is a fixed string in `main.py`.

## Files
- `main.py` — the entry program.
- `README.md` — description + run instructions.
- `LICENSE` — MIT.
- `.makefun/owner.json` — owner wallet (Solana).
