---
description: Used to say how many arguments are needed
---

# argCheck

```python
bot.command(
    Name = "test",
    Code = """
        $argCheck[1;You need at least 1 argument]
        ...Code...
    """
)
```

Parameters

| Name      | Type                                  | Description                                                           | Required                              |
| --------- | ------------------------------------- | --------------------------------------------------------------------- | ------------------------------------- |
| Arg Count | <mark style="color:blue;">Int</mark>  | Total amount of arguments the user should provide                     | <mark style="color:red;">True</mark>  |
| Warning   | <mark style="color:blue;">Text</mark> | Warning sent to the user if the amount isn't at LEAST the given total | <mark style="color:red;">False</mark> |
