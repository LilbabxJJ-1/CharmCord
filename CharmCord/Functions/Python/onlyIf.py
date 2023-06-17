import discord


async def onlyIf(args, context):
    choices = ["==", ">=", "<=", "!=", "<", ">"]
    if ";" in args:
        value = args.split(";")
        for i in choices:
            if i in value[0]:
                if i in ["==", "!="]:
                    vals = value[0].split(i)
                    vals[0]
                    vals[1]
                else:
                    vals = value[0].split(i)
                    int(vals[0])
                    int(vals[1])
                test = eval(f"val1 {i} val2")
                if test:
                    return True
                else:
                    if isinstance(context, discord.ApplicationContext):
                        await context.respond(value[1])
                    else:
                        await context.send(value[1])
                    return False
    else:
        value = args.split(";")
        for i in choices:
            if i in value[0]:
                if i in ["==", "!="]:
                    vals = args.split(i)
                    vals[0]
                    vals[1]
                else:
                    vals = args.split(i)
                    int(vals[0])
                    int(vals[1])
                test = eval(f"val1 {i} val2")
                if test:
                    return True
                else:
                    return False
