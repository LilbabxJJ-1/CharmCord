from CharmCord.CharmErrorHandling import CharmCordErrors
from CharmCord.globeHandler import get_globals

async def userID(user: str, context):
    bots = get_globals()[1]

    try:
        user = int(user.replace("<@", "").replace(">", ""))
        new_user = await bots.fetch_user(user)
    except ValueError:
        CharmCordErrors(f"mention ({user}) in $userID not valid")
        return
    return new_user.id
