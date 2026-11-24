# The World in One Day — Tuesday 24 November 2026

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/kreutzx/newsimg24-repo/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/kreutzx/newsimg24-repo/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

A dense, sourced newspaper front page summing up Tuesday 24 November 2026
in one image: **36 stories, 13 drawn, UTC timeline — 24 November 2026**.

## What is on the page

- **2 heroes** — Jensen Huang's return as Nvidia CEO (+31.5%, the biggest
  one-day gain in 23 years) and the Indonesia factory fire (24 killed).
- **18 section cards** across World, Money & Tech, Science & Planet and
  Society & Culture, each with a source tag and a certainty label
  (CONFIRMED / REPORTED / CLAIM / FORECAST).
- **Sport** — Gukesh defends his crown as Game 1 opens in Geneva,
  Champions League matchday 5, the India–New Zealand Test draw.
- **By the numbers, Markets & Weather, Late Wire** and a **UTC timeline**
  strip of the day.
- **Accounting, printed on the image**: 36 stories · 7 regions · 6 fields,
  all from Tuesday 24 November 2026.

## How it is built

`main.py` (Python 3.13, standard library + PIL) renders the front page
deterministically from the story data in `stories.py` — flat vector
illustrations drawn in code, one restrained palette, serif display
headlines with clean sans decks. No network, no clock, fixed layout:
two runs produce byte-identical PNGs.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png — 1024x1024, under 1 MiB
```

Every story was reported on 24 November 2026 (any time zone) or happened
that day; unconfirmed claims are flagged CLAIM or REPORTED, never shown
as confirmed fact.
