import json


async def setUserVar(args, Context):
    ag = args.split(";")
    user = ag[0]
    var = ag[1]
    value = ag[2]
    with open("variables.json", "r") as vars:
        total = json.load(vars)
    with open("variables.json", "w") as vars:
        try:
            total.update({f"{user}_{var}": int(value)})
        except:
            total.update({f"{user}_{var}": value})
        json.dump(total, vars)
    return
