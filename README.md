# <span style="color:pink">CharmCord</span>

### CharmCord: The Ultimate Python String-Based Package for Discord Bot Creators!

---

## Stats ✨
![PyPI](https://img.shields.io/pypi/v/charmcord)
![PyPI - Downloads](https://img.shields.io/pypi/dm/aoipy?color=green&label=downloads)
![Downloads](https://static.pepy.tech/personalized-badge/aoipy?period=total&units=international_system&left_color=grey&right_color=green&left_text=downloads)
![PyPI - License](https://img.shields.io/pypi/l/aoipy)
![](https://tokei.rs/b1/github/tomschimansky/aoipy)
[![All Contributors](https://img.shields.io/badge/all_contributors-4-orange.svg?style=flat-square)](#contributors-)

---

## v0.25.0

Function Additions

- `$addButton`
- `$addDropdown`
- `$dropdownOption`
- `$setGlobalUserVar`
- `$getGloablUserVar`
- `$interactionReply`

Deprecated Functions

- `$buttonSend`
- `$slashSend`

--- 
## <span style="color:pink">CharmCord</span> Setup

Install [CharmCord](https://pypi.org/charmcord) via pip:

```bash
pip install CharmCord
```
Warning: This package is still in beta. Use at your own risk. Feel free to report any issues you encounter.

Simple Bot Example:
```python
from CharmCord import CharmClient

bot = CharmClient(prefix="!", case_insensitive=False, intents=("all",))

bot.on_ready(
    Code="$console[Bot is Ready]"
)

bot.command(
    name="Ping", # Command Name
    code="""
    $sendMessage[$channelID; Pong!! $ping]
    """ # Command Code
)

bot.run("*******<<TOKEN>>***********")
```
---

## Contributors ✨

<a href="https://github.com/LilbabxJJ-1/CharmCord/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=LilbabxJJ-1/CharmCord"  alt="CharmCord-contributors"/>
</a>


Contributing
Contributions to CharmCord are welcomed and encouraged! If you'd like to contribute, please follow these guidelines:

--- 

- Fork the repository and clone it locally.
- Create a new branch for your feature or bug fix.
- Make your changes and test thoroughly.
- Ensure your code adheres to PEP8 standards.
- Commit your changes with descriptive commit messages.
- Push your branch to your fork and open a pull request against the main repository.
- After review, your pull request will be merged if approved.
  
Happy coding! 🚀
