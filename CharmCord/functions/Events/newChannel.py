from CharmCord.functions.Events import _options_


async def newChannel(option, context, opt=_options_.options):
    return opt["newChannel"][option.lower()]
