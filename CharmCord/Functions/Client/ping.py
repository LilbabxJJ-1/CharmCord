async def ping(emp, Context):
    from CharmCord.Classes.CharmCord import bots

    return round(bots.latency * 1000, 2)
