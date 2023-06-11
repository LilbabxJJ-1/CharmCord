import json


async def getUserVar(args, Context):
    from Aoipy.Classes.AoiPyClient import all_vars
    ag = args.split(";")
    user = ag[0]
    var = ag[1]
    try:
        with open("variables.json", "r") as vars:
            total = json.load(vars)
            return total[f"{user}_{var}"]
    except KeyError:
        with open("variables.json", "r") as vars:
            total = json.load(vars)
        with open("variables.json", "w") as vars:
            total.update({f"{user}_{var}": all_vars[var]})
            json.dump(total, vars)
            return all_vars[var]

