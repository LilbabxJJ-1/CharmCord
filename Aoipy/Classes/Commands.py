from Aoipy.tools import findBracketPairs, checkArgs, checkArgCheck


########################################
#              COMMANDS                #
########################################

class Commands:
    # Global variables

    def command(self, Name, Code):
        # Define command function dynamically
        from Aoipy.Classes.AoiPyClient import bots
        @bots.command(name=Name)
        async def go(ctx, *args, Code=Code):
            from Aoipy.Classes.AoiPyClient import TotalFuncs
            Context = ctx
            newCode = checkArgs(args, Code)
            finalCode = await checkArgCheck(args, newCode, Context)

            await findBracketPairs(finalCode, TotalFuncs, Context)
