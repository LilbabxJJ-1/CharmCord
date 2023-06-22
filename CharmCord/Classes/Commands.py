from CharmCord.tools import checkArgCheck, checkArgs, findBracketPairs, noArguments, lets, isValid

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
            finalCode = await noArguments(newCode, TotalFuncs, Context)
            finalCode = checkArgs(args, finalCode)
            finalCode = await isValid(finalCode, TotalFuncs)
            await findBracketPairs(finalCode, TotalFuncs, Context)
            if len(lets) >= 1:
                lets.clear()

