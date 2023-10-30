async def let(args, context):
    from CharmCord.tools import lets
    values = args.split(";")
    var = values[0]
    val = values[1]
    lets[var] = val
    return
