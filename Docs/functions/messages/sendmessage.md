---
description: Sends a message to the channel of the given ID
---

# sendMessage

```python
bot.command(
    Name = "send",
    Code = """
        $sendMessage[941931608582279178; This is a discord message]
    """
)
```

| Name       | Type                                                           | Description                                              | Required                             |
| ---------- | -------------------------------------------------------------- | -------------------------------------------------------- | ------------------------------------ |
| Channel ID | <mark style="color:blue;">Int</mark>                           | The ID of the channel the bot should send the message to | <mark style="color:red;">True</mark> |
| Message    | [<mark style="color:blue;">Any</mark>](#user-content-fn-1)[^1] | The content of the message                               | <mark style="color:red;">True</mark> |

[^1]: 
