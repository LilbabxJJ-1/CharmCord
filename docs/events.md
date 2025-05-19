# 🔁 Event Functions

CharmCord allows you to attach event-driven code to common Discord bot events, such as messages, reactions, channel updates, and member joins. These events behave similarly to `discord.py` events, but let you run **CharmCord-style string commands** when they occur.

---

## 🧠 How Events Work

When an event like `on_message` or `on_ready` is triggered, CharmCord automatically:

1. Captures relevant data into the `options` dictionary
2. Parses and executes the CharmCord code you registered for that event
3. Supports all `$` functions, including conditionals, message sends, variables, and more

---

## ⚙️ Available Events

### ✅ `on_ready(code: str)`

Triggered when the bot becomes ready.

- Parses and executes the code once on startup.
- Syncs slash commands automatically.

---

### 💬 `on_message(code: str)`

Triggered every time a message is received.

- Populates `options['onMessage']` with data like:
  - `channelid`
  - `guildid`
  - (Other attributes are currently stubbed or pending expansion)

---

### 🎉 `on_member_join(code: str)`

Fires when a user joins a guild.

- Stores:
  - `memberJoined.id`
  - `memberJoined.guildid`

---

### 📨 `on_reaction_add(code: str)`

Fires when a user adds a reaction to a message.

- Stores:
  - `reactionAdded.name` / `id`
  - `bot_reacted`
  - `users_reacted[]`
  - `count`, `msgid`, `username`, `userid`, etc.

---

### 🗑 `on_reaction_remove(code: str)`

Triggered when a reaction is removed from a message.

- Captures the same data structure as `on_reaction_add`, stored in `reactionRemoved[...]`

---

### 🛠 `on_channel_updated(code: str)`

Runs when a channel is updated (name, topic, delay, etc).

- Populates:
  - `oldChannel[...]`
  - `newChannel[...]`

Attributes include:
- `name`, `id`, `type`, `guildid`, `nsfw`, `slowmode_delay`, `category`, and `categoryid`

---

### ❌ `on_channel_deleted(code: str)`

Triggered when a channel is deleted.

- Captures:
  - `deletedChannel.name`
  - `deletedChannel.id`
  - `deletedChannel.nsfw`
  - `deletedChannel.created`
  - `deletedChannel.guild`, etc.

---

## 🧪 Example Usage

```python
bot.on_ready(
    code="""
    $console[Bot is ready and events are listening!]
    """
)

bot.on_message(
    code="""
    $if[$message==hello]
      $sendMessage[$channelID; Hi there!]
    $endIf
    """
)

bot.on_member_join(
    code="""
    $sendMessage[$channelID; Welcome <@$memberJoined.id>!]
    """
)
```

---

## 📦 Behind the Scenes

When you attach an event (like `on_message()`), CharmCord:

- Stores key variables inside the `options` dictionary
- Parses the CharmCord code with `no_arguments()` and `find_bracket_pairs()`
- Supports over 170+ functions in the same syntax as regular commands

---

## 📘 Related Pages

- [Messages](Messages.md) — Send, edit, or delete messages
- [Users](Users.md) — Access user IDs, names, and mentions
- [Variables](Variables.md) — Store persistent data
