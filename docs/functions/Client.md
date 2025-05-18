# 🤖 Client (Bot) Functions

These functions return information about the bot itself — including its ID, username, avatar, and statistics such as guild count and latency.

They are useful when creating responses that reflect your bot's identity, logging bot stats, or debugging connection details.

---

## 🧭 Function Index

| Function | Summary |
|----------|---------|
| [`$botID`](#botid-no-args) | Returns the bot's user ID |
| [`$botName`](#botname-no-args) | Returns the bot's username |
| [`$botAvatar`](#botavatar-no-args) | Returns the bot's avatar URL |
| [`$botMention`](#botmention-no-args) | Returns a mention tag for the bot |
| [`$botGuilds`](#botguilds-no-args) | Returns the number of servers the bot is in |
| [`$ping`](#ping-no-args) | Returns the bot’s latency in ms |
