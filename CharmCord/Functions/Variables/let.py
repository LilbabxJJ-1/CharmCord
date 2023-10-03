async def let(args, Context):
    from CharmCord.tools import lets
    values = args.split(";")
    var = values[0]
    val = values[1]
    lets[var] = val
    return
