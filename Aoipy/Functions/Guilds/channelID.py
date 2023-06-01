import Aoipy.AoiErrorHandling as ErrorHandling

EH = ErrorHandling.AoipyErrorHandling()


async def channelID(Name, Context):
    if len(Name) < 1:
        raise EH.Errors(4, "No parameter provided for '$channelID'")
    from Aoipy.Classes.AoiPyClient import bots
    try:
        channel = await bots.fetch_user(Name)
        return channel.name
    except ValueError:
        EH.Errors(2, Name)