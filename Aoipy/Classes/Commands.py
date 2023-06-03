from Aoipy.tools import findBracketPairs, checkArgs, checkArgCheck


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
            if type(Code) == type({"p": "s"}) and bots._LUNA_DEV_ONLY:pass
            else:
                newCode    =        checkArgs    (args,    Code         )
                if newCode == "Failed": return
                finalCode  =  await checkArgCheck(args, newCode, Context)

                await            findBracketPairs(finalCode, TotalFuncs, Context)
