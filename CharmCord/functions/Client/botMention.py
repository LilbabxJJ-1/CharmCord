from CharmCord.globeHandler import get_globals

async def botMention(args, context):
    bots = get_globals()[1]

    return bots.user.mention
