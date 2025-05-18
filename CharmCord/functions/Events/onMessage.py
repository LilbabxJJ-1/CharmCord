from CharmCord.functions.Events import _options_

async def onMessage(option, context, opt=_options_.options):
    return opt["onMessage"][option.lower()]