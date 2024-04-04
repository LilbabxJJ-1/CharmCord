import discord
import CharmCord.CharmErrorHandling as ErrorHandling
from CharmCord.globeHandler import get_globals

EH = ErrorHandling.CharmErrorHandling()


async def guildTextChannels(id, context):
    bots = get_globals()[1]

    try:
        id = int(id)
        text = []
        guild = await bots.fetch_guild(id)
        channels = list(await guild.fetch_channels())
        for channel in channels:
            if isinstance(channel, discord.TextChannel):
                text.append(channel.name)
        return text
    except ValueError:
        EH.Errors(2, "None")
