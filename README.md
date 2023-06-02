# AoiPy
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
### Aoi.py is the best python string-based package for Discord bot creators!


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
from Aoipy import AoipyClient, Commands, AoiEvents
```

3 -  Example:

```python

from Aoipy import AoipyClient, Commands, AoiEvents
# ---------------Imports--------------------

bot = AoipyClient(prefix="!", case_insensitive=False, intents=("all",))
events = AoiEvents()
command = Commands().command

events.onReady(
    code="$pyEval[print('Bot is Ready')]"
)

command(
    Name="Ping",
    Code="""
    $sendMessage[$currentChannelID[]; Pong!!]
    """
)


bot.run("*******<<TOKEN>>***********")
```

## New and still a work in progress


Our Contributors! ✨
<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/jagg3127"><img src="https://avatars.githubusercontent.com/u/61505193?v=4?s=100" width="100px;" alt="jagg3127"/><br /><sub><b>jagg3127</b></sub></a><br /><a href="https://github.com/LilbabxJJ-1/AoiPy2.0/commits?author=jagg3127" title="Code">💻</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!