from CharmCord.CharmErrorHandling import CharmCordErrors
from CharmCord.globeHandler import get_globals


async def userName(user: str, context):
    bots = get_globals()[1]

    try:
        user = int(user.replace("<@", "").replace(">", ""))
        new_user = await bots.fetch_user(user)
    except ValueError:
        CharmCordErrors(f"ID ({user}) in $userMention not valid")
        return
    return new_user.name
