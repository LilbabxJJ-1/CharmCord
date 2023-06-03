import discord
from discord.ext import commands
from Aoipy.tools import findBracketPairs, checkArgs, checkArgCheck
import asyncio
AC = {}

class Aoicogs:
    def Cogs(self, Cog_Group, Name, Code):
        from Aoipy.Classes.AoiPyClient import bots, all_commands

        class main_bod:
            def __init__(self, bot):
                self.bot = bot

            @commands.command(name=Name)
            async def go(self, ctx, *args, Code=Code):
                from Aoipy.Classes.AoiPyClient import TotalFuncs
                Context = ctx
                newCode = checkArgs(args, Code)
                finalCode = await checkArgCheck(args, newCode, Context)

                await findBracketPairs(finalCode, TotalFuncs, Context)

        # if Cog_Group in AC:
        #    asyncio.run(bots.remove_cog(Cog_Group))
        #    AC[Cog_Group][f"go{len(AC[Cog_Group])}"] = main_bod.go
        # else:
        #    AC[Cog_Group] = {'__init__': main_bod.__init__, 'go': main_bod.go}
        try:
           COGS = type(Cog_Group, (commands.Cog,), {'__init__': main_bod.__init__, 'go': main_bod.go})
        except:
           COGS = type(Cog_Group, (commands.Cog,), AC[Name])
        bots.add_cog(COGS(bots))

