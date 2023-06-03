import Aoipy.AoiErrorHandling as ErrorHandling

EH = ErrorHandling.AoipyErrorHandling()


async def channelID(empty, Context):
    try:
        int(Context.channel.id)
    except ValueError:
        EH.Errors(1, "None")
    return Context.channel.id
