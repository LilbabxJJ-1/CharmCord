import CharmCord.CharmErrorHandling as ErrorHandling

EH = ErrorHandling.CharmErrorHandling()


async def username(user, context):
    from CharmCord.Classes.CharmCord import bots

    try:
        int(user)
        new_user = await bots.fetch_user(user)
    except ValueError:
        EH.Errors(1, user)
        return
    return new_user
