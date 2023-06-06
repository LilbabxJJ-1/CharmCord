import Aoipy.AoiErrorHandling as ErrorHandling

EH = ErrorHandling.AoipyErrorHandling()
import discord

d = discord.Guild


async def guildTextChannels(ID, Context):
    from Aoipy.Classes.AoiPyClient import bots
    try:
        ID = int(ID)
        text = []
        guild = await bots.fetch_guild(ID)
        channels = list(await guild.fetch_channels())
        for channel in channels:
            if isinstance(channel, discord.TextChannel):
                text.append(channel.name)
        return text
    except ValueError:
        EH.Errors(2, "None")
