import Aoipy.AoiErrorHandling as ErrorHandling

EH = ErrorHandling.AoipyErrorHandling()


async def currentChannelID(empty, Context):
    try:
        int(Context.guild.id)
    except ValueError:
        EH.Errors(1, "None")
    return Context.guild.id