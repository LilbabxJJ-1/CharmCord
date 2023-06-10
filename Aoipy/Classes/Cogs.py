import discord
from discord.ext import commands
from Aoipy.tools import findBracketPairs, checkArgs, checkArgCheck, noArguments
import asyncio

AC = {}


class Aoicogs:
    def Cogs(self, Name, Code):
        from .AoiPyClient import bots

        @bots.command(name=Name)
        async def go(ctx, *args, Code=Code):
            from Aoipy.Classes.AoiPyClient import TotalFuncs
            Context = ctx
            newCode = checkArgs(args, Code)
            if newCode == "Failed":
                return
            finalCode = await checkArgCheck(args, newCode, Context)
            finalCode = await noArguments(finalCode, TotalFuncs, Context)
            await findBracketPairs(finalCode, TotalFuncs, Context)

