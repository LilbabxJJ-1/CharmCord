from CharmCord.functions.Events import options


async def reactionRemove(option, context, opt=options.options):
    return opt["reactionRemove"][option.lower()]