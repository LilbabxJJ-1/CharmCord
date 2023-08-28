from CharmCord.Functions.Events import options


async def newChannel(option, context, opt=options.options):
    return opt["newChannel"][option.lower()]
