from CharmCord.CharmErrorHandling import CharmCordErrors


async def userID(user: str, context):
    from CharmCord.Classes.CharmCord import bots

    try:
        user = int(user.replace("<@", "").replace(">", ""))
        new_user = await bots.fetch_user(user)
    except ValueError:
        CharmCordErrors(f"mention ({user}) in $userID not valid")
        return
    return new_user.id