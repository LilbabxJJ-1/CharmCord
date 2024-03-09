from CharmCord.functions.Events import options


async def memberJoined(option, context, opt=options.options):
    return opt["memberJoined"][option.lower()]
