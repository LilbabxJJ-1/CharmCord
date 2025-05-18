# 📬 Message Functions

This section covers all CharmCord functions related to sending, editing, deleting, and interacting with messages — including replies, embeds, and message metadata.

Whether you're building a bot that sends dynamic responses or reacts to user input, these are the tools you'll be using the most.

---

## 🧭 Function Index

| Function | Summary |
|----------|---------|
| [`$sendMessage`](#sendmessagechannelid-message) | Sends a basic message to a specified channel |
| [`$editMessage`](#editmessagemessageid-newcontent) | Edits an existing message |
| [`$deleteMessage`](#deletemessagemessageid) | Deletes a message by ID |
| [`$sendEmbed`](#sendembedchannelid-title-message-color-imageurl-footer) | Sends an embed with custom content |
| [`$waitMessage`](#waitmessagechannelid-userid-everyone-timeouterrormessage-return) | Waits for a message from a user |
| [`$message`](#message-no-args) | Returns the raw message content |
| [`$messageID`](#messageid-no-args) | Gets the ID of the triggering message |
| [`$mentions`](#mentionsindex) | Gets mentioned user ID by position |
| [`$messageAuthor`](#messageauthorchannelid-messageid) | Returns the author of a message |
| [`$messageContent`](#messagecontentchannelid-messageid) | Returns the content of a specific message |

---