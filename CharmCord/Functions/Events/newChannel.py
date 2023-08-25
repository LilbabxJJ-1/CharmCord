from CharmCord.Functions.Events import options


async def newChannel(option, context, options=options.options):
    return options["newChannel"][option.lower()]
