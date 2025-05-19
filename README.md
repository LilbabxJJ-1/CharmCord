# <span style="color:pink">CharmCord</span>

### CharmCord: The Ultimate Python String-Based Package for Discord Bot Creators!

---

![logo](docs/logo.png)

## Stats ✨
![PyPI](https://img.shields.io/pypi/v/charmcord)
![PyPI - Downloads](https://img.shields.io/pypi/dm/charmcord?color=green&label=downloads)
![Downloads](https://static.pepy.tech/personalized-badge/charmcord?period=total&units=international_system&left_color=grey&right_color=green&left_text=downloads)
![PyPI - License](https://img.shields.io/pypi/l/charmcord)
![](https://tokei.rs/b1/github/tomschimansky/charmcord)
[![All Contributors](https://img.shields.io/badge/all_contributors-4-orange.svg?style=flat-square)](#contributors-)

---

## v1.0.0
### Finally out of the Beta Stage! Thank you for any support offered! More additions coming soon

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

Simple Bot Example:
```python
from CharmCord import charmclient

bot = charmclient(prefix="!", case_insensitive=False, intents='all')

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
