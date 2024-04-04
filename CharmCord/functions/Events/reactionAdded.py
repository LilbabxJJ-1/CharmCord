from CharmCord.functions.Events import _options_


async def reactionAdded(option, context, opt=_options_.options):
    return opt["reactionAdded"][option.lower()]
