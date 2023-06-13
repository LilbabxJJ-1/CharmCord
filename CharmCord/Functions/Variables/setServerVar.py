import json


async def setServerVar(args, Context):
    ag = args.split(";")
    server = ag[0]
    var = ag[1]
    value = ag[2]
    with open("variables.json", "r") as vars:
        total = json.load(vars)
    with open("variables.json", "w") as vars:
        try:
            total.update({f"{server}_{var}": int(value)})
        except ValueError:
            total.update({f"{server}_{var}": value})
        json.dump(total, vars)
    return
