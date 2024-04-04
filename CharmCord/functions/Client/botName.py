from CharmCord.globeHandler import get_globals

async def botName(args, context):
    bots = get_globals()[1]

    return bots.user.name
