import Aoipy.AoiErrorHandling as ErrorHandling

EH = ErrorHandling.AoipyErrorHandling()


async def channelCategoryID(empty, Context):
    from Aoipy.Classes.AoiPyClient import bots
    try:
        int(Context.channel.category.id)
    except ValueError:
        EH.Errors(3, "None")
    return Context.channel.category.id