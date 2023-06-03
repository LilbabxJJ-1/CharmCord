import Aoipy.AoiErrorHandling as ErrorHandling
import discord
EH = ErrorHandling.AoipyErrorHandling()


async def guildChannels(ID, Context):
    from Aoipy.Classes.AoiPyClient import bots
    try:
        ID = int(ID)
        guild = await bots.fetch_guild(ID)
        return guild.channels
    except ValueError:
        EH.Errors(1, "None")
