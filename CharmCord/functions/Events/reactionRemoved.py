from CharmCord.functions.Events import options


async def reactionRemoved(option, context, opt=options.options):
    return opt["reactionRemoved"][option.lower()]