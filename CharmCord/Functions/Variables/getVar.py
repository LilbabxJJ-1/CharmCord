import json


async def getVar(name, Context):
    try:
        with open("variables.json", "r") as var:
            total = json.load(var)
            return total[name]
    except KeyError:
        raise SyntaxError(f"{name} variable not set")
