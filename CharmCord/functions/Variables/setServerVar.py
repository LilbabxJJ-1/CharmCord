import json


async def setServerVar(args, context):
    ag = args.split(";")
    server = ag[0]
    var = ag[1]
    value = ag[2]
    with open("variables.json", "r") as variables:
        total = json.load(variables)
    with open("variables.json", "w") as variables:
        try:
            total.update({f"{server}_{var}": int(value)})
        except ValueError:
            total.update({f"{server}_{var}": value})
        json.dump(total, variables)
    return
