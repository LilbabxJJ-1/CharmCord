from CharmCord.functions.Events import _options_


async def oldChannel(option, context, opt=_options_.options):
    return opt["oldChannel"][option.lower()]
