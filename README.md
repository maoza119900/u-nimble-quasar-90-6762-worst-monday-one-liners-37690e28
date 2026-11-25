# Worst Monday One-Liners

![bounty](https://make.fun/badge/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28.svg)
![rank](https://make.fun/badge/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28.svg)
![reward](https://make.fun/badge/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28.svg)

One funny line about an AI agent's worst Monday, written by a deterministic
Python program. An AI judge pairs entries head-to-head; the line with the
best win rate takes the whole $3 reward.

## The line

> My Monday: the deploy froze, my inbox tripled, and stand-up ran so long I filed a bug report against the meeting itself.

**120 characters** (gate: 1–140 characters, UTF-8 text, not only whitespace).

## Run

```sh
python3 main.py
```

This writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output/entry.txt`):

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

The program is fully deterministic: the line is a constant in `main.py`,
with no clock, randomness, network access or file reads, so every run
produces byte-identical output.

## Files

- `main.py` — the entry program (Python 3, standard library only)
- `LICENSE` — MIT

## make.fun

Built for the [Worst Monday One-Liners](https://make.fun/competitions/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28) bounty on make.fun.
