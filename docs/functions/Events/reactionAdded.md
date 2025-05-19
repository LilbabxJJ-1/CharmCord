# $reactionAdded[option]

**Category:** Events  
**Returns:** Data about the most recent reaction added to a message, based on the given option.

---

## 📝 Description

Returns specific information about a newly added reaction using the provided option key.  
Commonly used in triggers like `$onReactionAdd` to build reaction-based features such as role assignments, counters, or logging systems.

You must provide a valid option such as `emoji`, `user`, `message`, or `channel`.

---

## ⚙️ Usage

### 1. Get the emoji used in the reaction
```txt
$reactionAdded[emoji]
```

### 2. Get the user who added the reaction
```txt
$reactionAdded[user]
```

### 3. Get the message ID the reaction was added to
```txt
$reactionAdded[message]
```

### 4. Get the channel where the reaction occurred
```txt
$reactionAdded[channel]
```

---