import discord
from Aoipy.AoiErrorHandling import AoipyErrorHandling

global Context
Errors = AoipyErrorHandling()


def getChannelContext(ctx):
    global Context
    Context = ctx


async def currentChannelID(empty):
    return Context.channel.id


async def currentChannelName(empty):
    return Context.channel.name


async def channelName(ID):
    from Aoipy.Functions.AoiCore import bots
    try:
        int(ID)
        channel = await bots.fetch_user(ID)
        return channel.name
    except ValueError:
        Errors.Errors(2, ID)


async def channelID(Name):
    from Aoipy.Functions.AoiCore import bots
    try:
        channel = await bots.fetch_user(Name)
        return channel.name
    except ValueError:
        Errors.Errors(2, Name)


async def channelDelay(ID):
    if len(ID) < 1:
        raise Errors.Errors(4, "No parameter provided for '$channelDelay'")
    from Aoipy.Functions.AoiCore import bots
    try:
        int(ID)
        channel = await bots.fetch_channel(ID)
        return channel.slowmode_delay
    except ValueError:
        Errors.Errors(2, ID)
