import Aoipy.AoiErrorHandling as ErrorHandling

EH = ErrorHandling.AoipyErrorHandling()


async def channelName(ID, Context):
    if len(ID) < 1:
        raise EH.Errors(4, "No parameter provided for '$channelName'")
    from Aoipy.Classes.AoiPyClient import bots
    try:
        int(ID)
        channel = await bots.fetch_channel(ID)
        return channel.name
    except ValueError:
        EH.Errors(2, ID)