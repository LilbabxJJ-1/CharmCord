import json


async def setGlobalUserVar(args, context):
    ag = args.split(";")
    user = ag[0].replace("<@", "").replace(">", "")
    var = ag[1]
    value = ag[2]
    with open("variables.json", "r") as variables:
        total = json.load(variables)
    with open("variables.json", "w") as variables:
        try:
            total.update({f"{user}_{var}": int(value)})
        except:
            total.update({f"{user}_{var}": value})
        json.dump(total, variables)
    return
