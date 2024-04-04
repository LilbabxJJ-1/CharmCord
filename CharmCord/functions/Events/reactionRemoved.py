from CharmCord.functions.Events import _options_


async def reactionRemoved(option, context, opt=_options_.options):
    return opt["reactionRemoved"][option.lower()]