import CharmCord.AoiErrorHandling as ErrorHandling

EH = ErrorHandling.AoipyErrorHandling()


async def authorID(emp, Context):
    try:
        int(Context.author.id)
    except ValueError:
        EH.Errors(1, "None")
    return Context.author.id
