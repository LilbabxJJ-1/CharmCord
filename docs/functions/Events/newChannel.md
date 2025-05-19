# $newChannel[option]

**Category:** Events  
**Returns:** Data about the most recently created channel, based on the given option.

---

## 📝 Description

Returns specific information about a newly created channel using the provided option key.  
This function is typically used in event triggers like `$onChannelCreate` to access or log information when a new channel is made.

You must supply a valid option such as `id`, `name`, or `type` to retrieve corresponding data.

---

## ⚙️ Usage

### 1. Get the ID of the new channel
```txt
$newChannel[id]
```

### 2. Get the name of the new channel
```txt
$newChannel[name]
```

### 3. Get the channel type (e.g., text, voice)
```txt
$newChannel[type]
```

---