import random

import discord
from discord.ext import tasks

from CharmCord.CharmErrorHandling import CharmCordErrors


def setActivity(message: str, typing: str = "watching"):
    if typing.lower() not in ["watching", "playing", "listening"]:
        CharmCordErrors("Unknown Status type used for bot activity")
    if typing.lower() == "watching":
        act = discord.Activity(type=discord.ActivityType.watching, name=message)
    elif typing.lower() == "playing":
        act = discord.Activity(type=discord.ActivityType.playing, name=message)
    else:
        act = discord.Activity(type=discord.ActivityType.listening, name=message)

    return act


def loopActivity(time: int, messages: [str], types: str = "watching"):
    @tasks.loop(seconds=time)
    async def updateActivity(message=messages, typing=types):
        from CharmCord.utils.CharmCord import bots
        await bots.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching, name=random.choice(message)
            )
        )

    loopAct = updateActivity
    return loopAct
# Still having a lot of errors with this, will return when I have the time to set it up
