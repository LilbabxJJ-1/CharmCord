from CharmCord.globeHandler import get_globals

async def ping(emp, context):
    bots = get_globals()[1]

    return round(bots.latency * 1000, 2)
