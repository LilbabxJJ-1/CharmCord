from CharmCord.globeHandler import get_globals

async def botID(args, context):
    bots = get_globals()[1]
    return bots.user.id
