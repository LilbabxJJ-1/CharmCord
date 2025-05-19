# $onMessage[option]

**Category:** Events  
**Returns:** Data about the message that triggered the event, based on the given option.

---

## 📝 Description

Returns specific information about a message that triggered a message event, using the provided option key.  
This function is typically used in response to message-based events like `$onMessageCreate`.

You must provide a valid option such as `id`, `content`, `author`, or `channel`.

---

## ⚙️ Usage

### 1. Get the message ID
```txt
$onMessage[id]
```

### 2. Get the message content
```txt
$onMessage[content]
```

### 3. Get the author of the message
```txt
$onMessage[author]
```

### 4. Get the channel where the message was sent
```txt
$onMessage[channel]
```
