import discord


async def currentChannelID(args):
    from Aoipy.Functions.AoiCore import Context
    return Context.channel.id
