from discord.ext import commands
from Aoipy.tools import findBracketPairs, checkArgs, checkArgCheck
import asyncio


class cogs:
    def Cogs(self, Cog_Group, Name, Code):
        from Aoipy.Classes.AoiPyClient import bots

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

        COGS = type(Cog_Group, (commands.Cog,), {'__init__': main_bod.__init__, 'go': main_bod.go})
        asyncio.run(bots.add_cog(COGS(bots)))
