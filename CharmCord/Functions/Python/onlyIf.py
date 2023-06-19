import discord


async def onlyIf(args, context):
    choices = ["==", ">=", "<=", "!=", "<", ">"]
    operator_mapping = {
        "==": lambda x, y: x == y,
        "!=": lambda x, y: x != y,
        ">": lambda x, y: x > y,
        ">=": lambda x, y: x >= y,
        "<": lambda x, y: x < y,
        "<=": lambda x, y: x <= y,
    }
    if ";" in args:
        values = args.split(";")
        for i in choices:
            if i in args:
                if i in ["==", "!="]:
                    vals = values[0]
                    val1 = vals[0].strip()
                    val2 = vals[1].strip()
                else:
                    vals = values[0]
                    val1 = int(vals[0])
                    val2 = int(vals[1])
                result = operator_mapping.get(i, lambda x, y: None)(val1, val2)
                if result:
                    return True
                else:
                    if isinstance(context, discord.ApplicationContext):
                        await context.respond(values[1])
                    else:
                        await context.send(values[1])
                    return False
    else:
        value = args.split(";")
        for i in choices:
            if i in value[0]:
                if i in ["==", "!="]:
                    vals = args.split(i)
                    val1 = vals[0].strip()
                    val2 = vals[1].strip()
                else:
                    vals = args.split(i)
                    val1 = int(vals[0])
                    val2 = int(vals[1])
                result = operator_mapping.get(i, lambda x, y: None)(val1, val2)
                if result:
                    return True
                else:
                    return False
