from Aoipy.tools import findBracketPairs, checkArgs, checkArgCheck, noArguments


########################################
#              COMMANDS                #
########################################

class Commands:
    # Global variables

    def command(self, Name, Code, Aliases=[]):
        # Define command function dynamically
        from Aoipy.Classes.AoiPyClient import bots

        @bots.command(name=Name, aliases=Aliases)
        async def go(ctx, *args, Code=Code):
            from Aoipy.Classes.AoiPyClient import TotalFuncs
            Context = ctx
            newCode = await checkArgCheck(args, Code, Context)
            if newCode == "Failed":
                return
            finalCode = checkArgs(args, newCode)
            finalCode = await noArguments(finalCode, TotalFuncs, Context)
            await findBracketPairs(finalCode, TotalFuncs, Context)
