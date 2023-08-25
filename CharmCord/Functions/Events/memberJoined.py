from CharmCord.Functions.Events import options


async def memberJoined(emp, context, options=options.options):
    return options["memberJoined"]['id']