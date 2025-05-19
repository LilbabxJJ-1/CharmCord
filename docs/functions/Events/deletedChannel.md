# $deletedChannel[option]

**Category:** Events  
**Returns:** Data about the most recently deleted channel, based on the given option.

---

## 📝 Description

Returns specific information about the last deleted channel by supplying an option key such as `id`, `name`, `type`, and more.

This is commonly used in event triggers like `$onChannelDelete` to log or react to channel deletions in a customizable way.

You must provide a valid option string. Available options are determined by the event data captured when a channel is deleted.

---

## ⚙️ Usage

### 1. Get the ID of the deleted channel
```txt
$deletedChannel[id]
```

### 2. Get the name of the deleted channel
```txt
$deletedChannel[name]
```

### 3. Get the channel type (e.g., text, voice)
```txt
$deletedChannel[type]
```

---