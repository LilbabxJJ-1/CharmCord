---
description: >-
  Congratulations! You're now ready to unleash the power of AoiPy and build
  incredible Discord bots. Explore the extensive documentation, tap into the
  vibrant developer community
---

# 🛠 Getting set up



<details>

<summary>Step 1: Installing Aoi.Py</summary>

Need Python 3.5 and Above

```bash
pip install Aoipy
```

</details>

<details>

<summary>Step 2: Imports and bot instance</summary>

```python
from Aoipy import AoipyClient, Command,...
```

_As of update 0.11.3 you can Import the **Client**, **Command**, **Event**, and **setActivity** Function_

</details>

<details>

<summary>Step 3: Creating a AoiPy Bot Instance</summary>

Bot Instance with Commands



{% code overflow="wrap" %}
```python
from Aoipy import AoipyClient, Commands, AoiEvents, setActivity

# ---------------Imports--------------------
commands = Commands().command
bot = AoipyClient(prefix="!", case_insensitive=True, intents=("all",))

commands(
    Name='Ping',
    Aliases=["pg"],
    Code="""
    $sendMessage[$currentChannelID[]; Pong!]
    """
)
```
{% endcode %}

Bot Instance with Events and Activities

{% code overflow="wrap" %}
```python
from Aoipy import AoipyClient, Commands, AoiEvents, setActivity

# ---------------Imports--------------------
commands = Commands().command
event = AoiEvents()
act = setActivity(type="watching", message="My friends")
bot = AoipyClient(prefix="!", case_insensitive=True, intents=("all",), activity=act)

event.onReady(code="""$pyeval[print('Bot is online!')]""")

commands(
    Name='Ping',
    Aliases=["pg"],
    Code="""
    ...... Code ...... 
    """
)
```
{% endcode %}

</details>

<details>

<summary>Step 4: Add the run method</summary>

Lastly and most simple you will add

```python
bot.run("YOUR-TOKEN-HERE")
```

And enjoy simple bot creation!

</details>
