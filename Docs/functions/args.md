---
description: Used to grab any arguments that have/will be given when using command
---

# args

```python
bot.command(
    Name = "say",
    Code = """
        $sendMessage[$channelID; $args[1]!]
    """
)
```

Parameters:&#x20;

| Name      | Type                                 | Description                                                                                     | Required                             |
| --------- | ------------------------------------ | ----------------------------------------------------------------------------------------------- | ------------------------------------ |
| **Index** | <mark style="color:blue;">Int</mark> | The number arg that you are looking for, starting at 1 and going up. 1 being the first argument | <mark style="color:red;">True</mark> |

