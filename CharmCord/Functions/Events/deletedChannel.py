from CharmCord.Functions.Events import options


async def deletedChannel(option, context, options=options.options):
    return options["deletedChannel"][option.lower()]
