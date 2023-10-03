import discord

import CharmCord.CharmErrorHandling as ErrorHandling

EH = ErrorHandling.CharmErrorHandling()


async def guildTextChannels(ID, Context):
    from CharmCord.Classes.CharmCord import bots

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
