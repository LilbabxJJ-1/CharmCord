import Aoipy.AoiErrorHandling as ErrorHandling

EH = ErrorHandling.AoipyErrorHandling()


async def username(user):
    from Aoipy.Functions.AoiCore import bots
    try:
        int(user)
        new_user = await bots.fetch_user(user)
    except ValueError:
        EH.Errors(1, user)
        return
    return new_user
