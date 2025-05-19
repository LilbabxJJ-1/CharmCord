# $reactionRemoved[option]

**Category:** Events  
**Returns:** Data about the most recent reaction that was removed from a message, based on the given option.

---

## 📝 Description

Returns specific information about a removed reaction using the provided option key.  
This is typically used with events like `$onReactionRemove` to track or respond to users removing reactions, often used in role management or audit features.

You must supply a valid option such as `emoji`, `user`, `message`, or `channel`.

---

## ⚙️ Usage

### 1. Get the emoji that was removed
```txt
$reactionRemoved[emoji]
```

### 2. Get the user who removed the reaction
```txt
$reactionRemoved[user]
```

### 3. Get the message ID the reaction was removed from
```txt
$reactionRemoved[message]
```

### 4. Get the channel where the reaction was removed
```txt
$reactionRemoved[channel]
```

---