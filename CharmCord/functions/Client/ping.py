async def ping(emp, context):
    from CharmCord.utils.CharmCord import bots

    return round(bots.latency * 1000, 2)
