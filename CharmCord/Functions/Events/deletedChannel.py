from CharmCord.Functions.Events import options


async def deletedChannel(option, context, opt=options.options):
    return opt["deletedChannel"][option.lower()]
