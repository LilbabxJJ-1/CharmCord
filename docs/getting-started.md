# 🚀 Getting Started with CharmCord

Welcome to **CharmCord** — a lightweight, string-based scripting layer built on top of `discord.py`. This guide will help you get your bot up and running in just a few minutes.

---

## 📦 Installation

To install CharmCord, run the following command in your terminal:

`pip install CharmCord`

This will install CharmCord along with any necessary dependencies like `discord.py`.

---

## 🧪 Minimal Bot Example

Here’s a quick example of how to make a functional bot:

1. Import the CharmCord client:

   `from CharmCord import charmclient`

2. Create the bot object:

   `bot = charmclient(prefix="!", case_insensitive=True, intents="all")`

3. Set the `on_ready` message:

   `bot.on_ready(Code="$console[Bot is ready!]")`

4. Add a basic ping command:

   ```txt
   bot.command(
       name="ping",
       code="""
       $sendMessage[$channelID; Pong! $ping]
       """
   )
   ```

5. Run your bot with:

   `bot.run("YOUR_BOT_TOKEN")`


### Final

```python
from CharmCord import charmclient

bot = charmclient(prefix="!", case_insensitive=True, intents='all')

bot.on_ready(
    code="$console[$botName is online!]"
)

bot.command(
    name="Ping",
    code="""
    $sendMessage[$channelID;Pong! $ping]
    """,
)

bot.run("TOKEN HERE")
```
---

## 🧭 CharmCord Basics

CharmCord allows you to write bot logic using structured strings. Here's an example of a conditional:

If the user types `!cool`, your bot can respond with:

```txt
bot.command(
    name="cool",
    code="""
        $if[$args[1]==cool]
            $sendMessage[$channelID; You're cool 😎]
        $else
            $sendMessage[$channelID; Try being cool next time!]
        $endIf
""")
```

no decorators — just readable logic.

---

## 📘 What to Read Next

- [Function Reference](functions/Messages.md) — learn about every built-in function
- [Architecture](architecture.md) — understand how CharmCord interprets and runs your code
- [Sandbox](sandbox.md) — (if implemented) try a live tester



Made with 💖 by Jade. CharmCord exists to make bots more magical, accessible, and fun ✨
