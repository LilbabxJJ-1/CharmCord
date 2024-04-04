from CharmCord.functions.Events import _options_


async def memberJoined(option, context, opt=_options_.options):
    return opt["memberJoined"][option.lower()]
