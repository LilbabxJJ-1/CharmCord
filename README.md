# CharmCord

### CharmCord is the best python string-based package for Discord bot creators!


![PyPI](https://img.shields.io/pypi/v/aoipy)
![PyPI - Downloads](https://img.shields.io/pypi/dm/aoipy?color=green&label=downloads)
![Downloads](https://static.pepy.tech/personalized-badge/aoipy?period=total&units=international_system&left_color=grey&right_color=green&left_text=downloads)
![PyPI - License](https://img.shields.io/pypi/l/aoipy)
![](https://tokei.rs/b1/github/tomschimansky/aoipy)
[![All Contributors](https://img.shields.io/badge/all_contributors-2-orange.svg?style=flat-square)](#contributors-)
![logo](https://github.com/LilbabxJJ-1/AoiPy/blob/master/CharmCord%20logo.png)

### Using AoiPy

1 - `pip install AoiPy`

2 - Import AoiClient

```python
from CharmCord import CharmClient
```

3 -  Example:

```python

from CharmCord import CharmClient
# ---------------Imports--------------------

bot = CharmClient(prefix="!", case_insensitive=False, intents=("all",))

bot.onReady(
    Code="$pyEval[print('Bot is Ready')]"
)

bot.command(
    Name="Ping",
    Code="""
    $sendMessage[$channelID; Pong!! $ping]
    """
)


bot.run("*******<<TOKEN>>***********")
```

## New and still a work in progress

## Contributors ✨

<a href="https://github.com/LilbabxJJ-1/AoiPy2.0/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=LilbabxJJ-1/AoiPy2.0"  alt="aoi.py-contributors"/>
</a>
