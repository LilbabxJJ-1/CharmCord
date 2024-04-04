from CharmCord.functions.Events import _options_


async def deletedChannel(option, context, opt=_options_.options):
    return opt["deletedChannel"][option.lower()]
