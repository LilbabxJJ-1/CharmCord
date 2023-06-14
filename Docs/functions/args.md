# $args
---
description: Used to grab any arguments that have/will be given when using commands
---

## Use

```python
bot.command(
    Name = "say",
    Code = """
        $sendMessage[$channelID; $args[1]!]
    """

    # If user did !say CharmCord, bot would reply 'CharmCord'
)
```

---

## Parameters

| Name      | Type           | Description                             | Required |
| --------- | -------------- | --------------------------------------- | -------- |
| Index     | `Int`          | The number arg you are looking for       | `true`   |
| Parameter | `String`       | The parameter description                | `false`  |