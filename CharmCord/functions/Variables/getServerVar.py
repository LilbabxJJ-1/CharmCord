import json


async def getServerVar(args, context):
    from CharmCord.utils.CharmCord import all_vars

    ag = args.split(";")
    server = ag[0]
    var = ag[1]
    try:
        with open("variables.json", "r") as variables:
            total = json.load(variables)
            return total[f"{server}_{var}"]
    except KeyError:
        with open("variables.json", "r") as variables:
            total = json.load(variables)
        with open("variables.json", "w") as variables:
            total.update({f"{server}_{var}": all_vars[var]})
            json.dump(total, variables)
            return all_vars[var]
