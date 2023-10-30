import json


async def getUserVar(args, context):
    from CharmCord.utils.CharmCord import all_vars

    ag = args.split(";")
    user = ag[0].replace("<@", "").replace(">", "")
    serverID = context.guild.id
    var = ag[1]
    try:
        with open("variables.json", "r") as variables:
            total = json.load(variables)
            return total[f"{user}_{serverID}_{var}"]
    except KeyError:
        with open("variables.json", "r") as variables:
            total = json.load(variables)
        with open("variables.json", "w") as variables:
            total.update({f"{user}_{serverID}_{var}": all_vars[var]})
            json.dump(total, variables)
            return all_vars[var]
