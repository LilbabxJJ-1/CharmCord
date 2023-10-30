from CharmCord.functions.Events import options


async def deletedChannel(option, context, opt=options.options):
    return opt["deletedChannel"][option.lower()]
