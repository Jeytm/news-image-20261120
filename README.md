# The World in One Day — Friday, 20 November 2026

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/Jeytm/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/Jeytm/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

One image summing up Friday 20 November 2026's world news, drawn in code
with Pillow (`render.py`) — six verified stories, each corroborated by at
least two independent sources:

1. **Trump puts the Iran decision off to 2027** — "We'll see what happens
   after Jan 1" (Reuters; The Times of India).
2. **ICJ: Myanmar committed genocide** — 9–6 ruling on the Rohingya,
   ~10,000 killed in 2017, reparations ordered (BBC; Reuters; AP).
3. **Cyclone Akvan nears landfall** — due ashore by noon on the
   Andhra–Odisha coast; 100,000+ evacuated (The Hindu; IMD).
4. **Drone raid damages two embassies in Kyiv** — one killed, five hurt;
   Austrian and Dutch missions hit (AFP; Euronews).
5. **GTA VI: $1.84bn in a single day** — 19.05m copies sold, past The
   Odyssey's $1.805bn box office (Sensor Tower via Reuters; Forbes).
6. **Nicholls rescues New Zealand** — 113 not out lifts the hosts from
   70/5 to 243/5 on day one vs India (ESPNcricinfo; NZ Herald).

Entry for the make.fun competition
[`news-image-20261120`](https://make.fun/bounty/news-image-20261120)
($250 USDC, 50 places).

## Run it

```sh
python3 render.py          # redraws entry.png (1024x1024, deterministic)
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py   # copies entry.png to out/
```

`main.py` (Python 3.13, standard library only) validates `entry.png`
(PNG magic bytes) and copies it to `$MAKEFUN_OUTPUT_DIR`. Two runs write
identical bytes.

License: MIT.
