from CharmCord.functions.Events import options


async def oldChannel(option, context, opt=options.options):
    return opt["oldChannel"][option.lower()]
