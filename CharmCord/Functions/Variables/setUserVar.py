import json


async def setUserVar(args, Context):
    ag = args.split(";")
    user = ag[0].replace("<@", "").replace(">", "")
    var = ag[1]
    value = ag[2]
    serverID = Context.guild.id
    with open("variables.json", "r") as variables:
        total = json.load(variables)
    with open("variables.json", "w") as variables:
        try:
            total.update({f"{user}_{serverID}_{var}": int(value)})
        except:
            total.update({f"{user}_{serverID}_{var}": value})
        json.dump(total, variables)
    return
