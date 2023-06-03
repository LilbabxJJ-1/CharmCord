import Aoipy.AoiErrorHandling as ErrorHandling

EH = ErrorHandling.AoipyErrorHandling()


async def channelCategoryName(ID, Context):
    if len(ID) < 1:
        raise EH.Errors(4, "No parameter provided for '$channelCategoryName'")
    from Aoipy.Classes.AoiPyClient import bots
    try:
        int(ID)
        channel = await bots.fetch_channel(ID)
        return channel.category.name
    except ValueError:
        EH.Errors(3, ID)