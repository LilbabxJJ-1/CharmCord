from CharmCord.Functions.Events import options


async def oldChannel(option, context, options=options.options):
    return options["oldChannel"][option.lower()]
