from CharmCord.functions.Events import options


async def reactionAdded(option, context, opt=options.options):
    return opt["reactionAdded"][option.lower()]
