import discord
global Context


def getChannelContext(ctx):
    global Context
    Context = ctx


async def currentChannelID(empty):
    return Context.channel.id

async def currentChannel():
    pass
