from CharmCord.tools import findBracketPairs, checkArgs, checkArgCheck, noArguments, ifs


########################################
#              COMMANDS                #
########################################

class Commands:
    # Global variables

    def command(self, Name, Code, Aliases=[]):
        # Define command function dynamically
        from CharmCord.Classes.CharmCord import bots

        @bots.command(name=Name, aliases=Aliases)
        async def go(ctx, *args, Code=Code):
            from CharmCord.Classes.CharmCord import TotalFuncs
            Context = ctx
            newCode = await checkArgCheck(args, Code, Context)
            if newCode == "Failed":
                return
            finalCode = checkArgs(args, newCode)
            finalCode = await noArguments(finalCode, TotalFuncs, Context)
            finalCode = ifs(finalCode)
            if finalCode is False:
                return
            await findBracketPairs(finalCode, TotalFuncs, Context)
