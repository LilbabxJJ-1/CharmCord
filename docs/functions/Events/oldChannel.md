# $oldChannel[option]

**Category:** Events  
**Returns:** Data about a channel **before** it was updated, based on the given option.

---

## 📝 Description

Returns specific information about a channel prior to being updated, using the provided option key.  
Typically used in update event triggers like `$onChannelUpdate` to compare changes between the old and new states.

You must provide a valid option such as `name`, `type`, or `topic` to retrieve the relevant data before the update occurred.

---

## ⚙️ Usage

### 1. Get the old name of the channel
```txt
$oldChannel[name]
```

### 2. Get the old channel type
```txt
$oldChannel[type]
```

### 3. Get the old channel topic (if applicable)
```txt
$oldChannel[topic]
```

---