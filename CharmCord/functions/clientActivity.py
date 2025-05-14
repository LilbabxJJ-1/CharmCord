import random
import discord
from discord.ext import tasks
from CharmCord.globeHandler import get_globals, update_globals
from CharmCord.CharmErrorHandling import CharmCordErrors, CharmCordError


def set_activity(message: str, typing: str = "watching") -> discord.Activity:
    if typing.lower() not in ["watching", "playing", "listening"]:
        CharmCordError(error_msg="Unknown Status type used for bot activity",
                               code_sample=f"{typing}").internal_error()
        return None
    if typing.lower() == "watching":
        act = discord.Activity(type=discord.ActivityType.watching, name=message)
    elif typing.lower() == "playing":
        act = discord.Activity(type=discord.ActivityType.playing, name=message)
    else:
        act = discord.Activity(type=discord.ActivityType.listening, name=message)
    return act


def loop_activity(time: int, messages: [str], types: str = "watching"):
    @tasks.loop(seconds=time)
    async def updateActivity(message=messages, typing=types):
        bots = get_globals()[1]
        act = discord.Activity(type=discord.ActivityType.watching, name=random.choice(message))
        return act

    return updateActivity


# Still having a lot of errors with this, will return when I have the time to set it up

async def update_activity(activity):
    return await activity.start()
