from CharmCord.globeHandler import get_globals

async def botGuilds(args, context):
    bots = get_globals()[1]

    return bots.guilds
