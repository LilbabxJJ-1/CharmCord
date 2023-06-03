import discord
import random
from discord.ext import tasks


def setActivity(message: str, type: str = "watching"):
    if type.lower() == "watching":
        act = discord.Activity(type=discord.ActivityType.watching, name=message)
    elif type.lower() == "playing":
        act = discord.Activity(type=discord.ActivityType.playing, name=message)
    else:
        act = discord.Activity(type=discord.ActivityType.listening, name=message)

    return act

#Come back to this
@tasks.loop(seconds=10)
async def updateActivity(messages: list, type: str = "watching"):
    from Aoipy.Functions.AoiCore import bots
    all = messages
    await bots.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=random.choice(all)))
