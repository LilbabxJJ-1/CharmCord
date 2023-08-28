from CharmCord.Functions.Events import options


async def oldChannel(option, context, opt=options.options):
    return opt["oldChannel"][option.lower()]
