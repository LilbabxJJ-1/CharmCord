# 🧍 User Functions

These functions provide access to information about users — including message authors, mentioned users, user IDs, usernames, and more. They also allow sending DMs and checking permissions.

Use them when you need to customize behavior based on the user interacting with the bot.

---

## 🧭 Function Index

| Function | Summary |
|----------|---------|
| [`$authorID`](#authorid-no-args) | Gets the ID of the message author |
| [`$authorName`](#authorname-no-args) | Gets the name of the message author |
| [`$userID`](#useridmention) | Gets the ID of a mentioned user |
| [`$userName`](#usernamemention) | Gets the username of a mentioned user |
| [`$userMention`](#usermentionuserid) | Converts a user ID to a mention tag |
| [`$hasPerm`](#haspermpermission) | Checks if the user has a specific permission |
| [`$sendDM`](#senddmuserid-message) | Sends a direct message to the user |

