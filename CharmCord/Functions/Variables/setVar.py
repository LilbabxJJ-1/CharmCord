import json


async def setVar(args, Context):
    from CharmCord.Classes.CharmCord import all_vars
    ag = args.split(";")
    try:
        with open("variables.json", "r") as var:
            total = json.load(var)
            try:
                total.update({ag[0]: int(ag[1])})
            except:
                total.update({ag[0]: ag[1]})
        with open("variables.json", "w") as var:
            json.dump(total, var)
    except KeyError:
        raise SyntaxError(f"{ag[0]} variable not set")