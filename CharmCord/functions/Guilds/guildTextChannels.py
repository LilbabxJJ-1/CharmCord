import discord

import CharmCord.CharmErrorHandling as ErrorHandling

EH = ErrorHandling.CharmErrorHandling()


async def guildTextChannels(id, context):
    from CharmCord.utils.CharmCord import bots

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
