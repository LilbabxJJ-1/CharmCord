import CharmCord.AoiErrorHandling as ErrorHandling

EH = ErrorHandling.AoipyErrorHandling()


async def authorName(emp, Context):
    return Context.author.name
