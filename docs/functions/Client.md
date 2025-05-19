# 🤖 Client (Bot) Functions

These functions return information about the bot itself — including its ID, username, avatar, and statistics such as guild count and latency.

They are useful when creating responses that reflect your bot's identity, logging bot stats, or debugging connection details.

---

## 🧭 Function Index

| Function                         | Summary |
|----------------------------------|---------|
| [`$botID`](botId)                | Returns the bot's user ID |
| [`$botName`](botName)            | Returns the bot's username |
| [`$botAvatar`](botavatar) | Returns the bot's avatar URL |
| [`$botMention`](botmention) | Returns a mention tag for the bot |
| [`$botGuilds`](botguilds) | Returns the number of servers the bot is in |
| [`$ping`](ping)           | Returns the bot’s latency in ms |
