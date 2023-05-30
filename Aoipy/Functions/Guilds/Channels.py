import discord

global Context


def getChannelContext(ctx):
    global Context
    Context = ctx


async def currentChannelID(empty):
    return Context.channel.id


async def currentChannelName(empty):
    return Context.channel.name


async def getChannelDelay(ID):
    from Aoipy.Functions.AoiCore import bots
    try:
        int(ID)
        channel = await bots.fetch_user(ID)
        return channel.slowmode_delay
    except ValueError:
        raise Exception(f"{ID} isn't a Channel ID")
