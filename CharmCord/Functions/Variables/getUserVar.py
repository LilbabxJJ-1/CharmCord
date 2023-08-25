import json


async def getUserVar(args, Context):
    from CharmCord.Classes.CharmCord import all_vars

    ag = args.split(";")
    user = ag[0]
    serverID = Context.guild.id
    var = ag[1]
    try:
        with open("variables.json", "r") as variables:
            total = json.load(variables)
            return total[f"{user}_{var}"]
    except KeyError:
        with open("variables.json", "r") as variables:
            total = json.load(variables)
        with open("variables.json", "w") as variables:
            total.update({f"{user}_{serverID}_{var}": all_vars[var]})
            json.dump(total, variables)
            return all_vars[var]
