# $memberJoined[option]

**Category:** Events  
**Returns:** Data about the most recent member who joined the server, based on the given option.

---

## 📝 Description

Returns specific information about the latest user who joined the server, based on the provided option.  
This function is typically used in combination with events like `$onJoin` to welcome or log new members.

You must provide a valid option string. Common options include `id`, `name`, `mention`, and more, depending on the data stored during the event.

---

## ⚙️ Usage

### 1. Get the ID of the member who joined
```txt
$memberJoined[id]
```

### 2. Get the username of the member who joined
```txt
$memberJoined[name]
```

### 3. Get the mention tag of the member who joined
```txt
$memberJoined[mention]
```

---