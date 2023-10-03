from CharmCord.Functions.Events import options


async def memberJoined(emp, context, opt=options.options):
    return opt["memberJoined"]['id']
