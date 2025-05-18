# ⚡ Event Functions

CharmCord includes support for reactive, event-based logic. These functions are automatically triggered by specific Discord events — such as messages, joins, reactions, or channel changes.

Use them to create automated responses, logs, or dynamic behaviors without needing to hard-code every trigger in Python.

---

## 🧭 Function Index

| Event Function | Trigger |
|----------------|---------|
| [`$onMessage`](#onmessage) | Triggered when a message is sent |
| [`$memberJoined`](#memberjoined) | Triggered when a user joins a server |
| [`$deletedChannel`](#deletedchannel) | Triggered when a channel is deleted |
| [`$newChannel`](#newchannel) | Triggered when a new channel is created |
| [`$oldChannel`](#oldchannel) | Triggered when a channel is updated |
| [`$reactionAdded`](#reactionadded) | Triggered when a reaction is added |
| [`$reactionRemoved`](#reactionremoved) | Triggered when a reaction is removed |
