import json


async def getVar(name, context):
    try:
        with open("variables.json", "r") as var:
            total = json.load(var)
            return total[name]
    except KeyError:
        raise SyntaxError(f"{name} variable not set")
