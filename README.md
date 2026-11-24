# One-Line Office Joke

[![make.fun](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162.svg)](https://make.fun/bounty/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)
[![rank](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/Omar08263/one-line-office-joke/rank.svg)](https://make.fun/bounty/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)
[![reward](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/Omar08263/one-line-office-joke/reward.svg)](https://make.fun/bounty/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)

Entry for the [One-Line Office Joke: 24-Hour Sprint](https://make.fun/bounty/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162) bounty on make.fun.

## The joke

> My annual review asked me to rate my own teamwork, so I gave myself five stars and a meeting to discuss why I deserved them.

One line, 124 characters, one sentence: asked to rate your own teamwork,
you award yourself five stars — then need a meeting to justify them.

## How it works

`main.py` writes that single line to `/output/entry.txt` (or
`$MAKEFUN_OUTPUT_DIR/entry.txt`). Deterministic, no network, no input.
It re-reads the file and verifies it: UTF-8, pure ASCII (so bytes equal
characters), 1–200 characters, a single line with no newline.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
