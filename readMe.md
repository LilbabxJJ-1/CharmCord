# AoiPy
### Aoi.py is the best python string-based package for Discord bot creators!
Latest Update: 05/28/23

![PyPI](https://img.shields.io/pypi/v/aoipy)
![PyPI - Downloads](https://img.shields.io/pypi/dm/aoipy?color=green&label=downloads)
![Downloads](https://static.pepy.tech/personalized-badge/aoipy?period=total&units=international_system&left_color=grey&right_color=green&left_text=downloads)
![PyPI - License](https://img.shields.io/pypi/l/aoipy)
![](https://tokei.rs/b1/github/tomschimansky/aoipy)

![AoiPY](https://github.com/LilbabxJJ-1/Aoipy/blob/master/aoipy/AOIpy%20(1).png)
### Using AoiPy
1 - `pip install AoiPy`

2 - Import Bot, Commands, etc

```python
from Aoipy import Bot, Commands, AoiEvents
```

3 -  Example:

```python

from Aoipy import Bot, Commands, AoiEvents
# ---------------Imports--------------------

bot = Bot(prefix="!", case_insensitive=False, intents=("all",))
events = AoiEvents()
command = Commands().command

events.onReady(
    code="$pyeval[print('Bot is Ready')]"
)

command(
    Name="Ping",
    Code="""
    $send[1112301680839643156; Pong!!]
    """
)


bot.run("*******<<TOKEN>>***********")
```

## New and still a work in progress
