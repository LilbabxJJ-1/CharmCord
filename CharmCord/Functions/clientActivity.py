import asyncio
import random
from enum import Enum

# class CharmActivity(Enum):
import discord
from discord.ext import tasks


def setActivity(message: str, type: str = "watching"):
    if type.lower() == "watching":
        act = discord.Activity(type=discord.ActivityType.watching, name=message)
    elif type.lower() == "playing":
        act = discord.Activity(type=discord.ActivityType.playing, name=message)
    else:
        act = discord.Activity(type=discord.ActivityType.listening, name=message)

    return act


def loopActivity(time: int, messages: [str], types: str = "watching"):
    @tasks.loop(seconds=time)
    async def updateActivity(message=messages, type=types):
        from CharmCord.Classes.CharmCord import bots
        await bots.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching, name=random.choice(message)
            )
        )

# Still having a lot of errors with this, will return when I have the time to set it up
