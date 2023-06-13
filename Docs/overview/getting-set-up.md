---
description: >-
  Congratulations! You're now ready to unleash the power of CharmCord and build
  incredible Discord bots. Explore the extensive documentation, tap into the
  vibrant developer community
---

# 🛠 Getting set up

<details>

<summary>Step 1: Installing CharmCord</summary>

Need Python 3.5 and Above

```bash
pip install CharmCord
```

</details>

<details>

<summary>Step 2: Imports</summary>

<pre class="language-python"><code class="lang-python">from CharmCord import CharmClient

<strong>...
</strong></code></pre>

</details>

<details>

<summary>Step 3: Creating a CharmCord Bot Instance</summary>

Bot Instance with Commands

<pre class="language-python" data-overflow="wrap"><code class="lang-python">from CharmCord import CharmClient

# ---------------Imports--------------------
bot = CharmClient(prefix="!", case_insensitive=True, intents=("all",))

<strong>bot.command(
</strong>    Name='Ping',
    Aliases=["pg"],
    Code="""
    $sendMessage[$channelID; $ping Pong!]
    """
)
</code></pre>

Bot Instance with Events and Activities

{% code overflow="wrap" %}
```python
from CharmCord import CharmClient, setActivity

# ---------------Imports--------------------
act = setActivity(type="watching", message="My friends")
bot = CharmClient(prefix="!", case_insensitive=True, intents=("all",), activity=act)

bot.onReady(code="""$pyeval[print('Bot is online!')]""")

bot.command(
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

Lastly and most simple, you will add

```python
bot.run("YOUR-TOKEN-HERE")
```

And enjoy simple bot creation!

</details>
