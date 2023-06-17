from CharmCord.tools import checkArgCheck, checkArgs, findBracketPairs, noArguments

AC = {}


class Charmcogs:
    def Cogs(self, Name, Code):
        from .CharmCord import bots

        @bots.command(name=Name)
        async def go(ctx, *args, Code=Code):
            from CharmCord.Classes.CharmCord import TotalFuncs

            Context = ctx
            newCode = checkArgs(args, Code)
            if newCode == "Failed":
                return
            finalCode = await checkArgCheck(args, newCode, Context)
            finalCode = await noArguments(finalCode, TotalFuncs, Context)
            await findBracketPairs(finalCode, TotalFuncs, Context)
