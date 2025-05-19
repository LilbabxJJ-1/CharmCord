# ⚡ Event Functions

CharmCord includes support for reactive, event-based logic. These functions are automatically triggered by specific Discord events — such as messages, joins, reactions, or channel changes.

Use them to create automated responses, logs, or dynamic behaviors without needing to hard-code every trigger in Python.

---

## 🧭 Function Index

| Event Function                        | Trigger |
|---------------------------------------|---------|
| [`$onMessage`](onMessage)             | Triggered when a message is sent |
| [`$memberJoined`](memberJoined)       | Triggered when a user joins a server |
| [`$deletedChannel`](deletedChannel)   | Triggered when a channel is deleted |
| [`$newChannel`](newChannel)           | Triggered when a new channel is created |
| [`$oldChannel`](oldChannel)           | Triggered when a channel is updated |
| [`$reactionAdded`](reactionAdded)     | Triggered when a reaction is added |
| [`$reactionRemoved`](reactionRemoved) | Triggered when a reaction is removed |
