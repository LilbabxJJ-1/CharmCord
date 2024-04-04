from CharmCord.globeHandler import get_globals

async def botAvatar(args, context):
    bots = get_globals()[1]

    return bots.user.avatar.url
