import Aoipy.AoiErrorHandling as ErrorHandling

EH = ErrorHandling.AoipyErrorHandling()


async def guildName(ID, Context):
    if len(ID) < 1:
        raise EH.Errors(4, "No parameter provided for '$guildName'")
    from Aoipy.Classes.AoiPyClient import bots
    try:
        int(ID)
        guild = await bots.fetch_guild(ID)
        return guild.name
    except ValueError:
        EH.Errors(2, ID)