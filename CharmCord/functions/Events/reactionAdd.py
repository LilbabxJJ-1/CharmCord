from CharmCord.functions.Events import options


async def reactionAdd(option, context, opt=options.options):
    return opt["reactionAdd"][option.lower()]
