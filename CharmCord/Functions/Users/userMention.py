from CharmCord.CharmErrorHandling import CharmCordErrors


async def userMention(user: str, context):
    from CharmCord.Classes.CharmCord import bots

    try:
        user = int(user.replace("<@", "").replace(">", ""))
        new_user = await bots.fetch_user(user)
    except ValueError:
        CharmCordErrors(f"ID ({user}) in $userMention not valid")
        return
    return new_user.mention
