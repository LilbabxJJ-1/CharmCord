from discord.ext import commands
from Aoipy.tools import findBracketPairs, checkArgs, checkArgCheck

class cogs:
    
    def Cogs(self, Cog_Group, Name, Code):
        from Aoipy.Classes.AoiPyClient import bots

        class main_bod:
            def __init__(self, bot):
                self.bot = bot

            @bots.command(name=Name)
            async def go(ctx, *args, Code=Code):
                from LuPYdisc.Classes.AoiPyClient import TotalFuncs
                Context   = ctx
                if type(Code) == type({"p": "s"}):
                    for main, secondary in Code.items():
                        if type(secondary) == type(([], "")):                        
                            main_args=""
                            for arg in secondary[0]: main_args+="$"+arg+"[]; "

                            Code      = f'{main+"["+main_args+secondary[1]+"]"}'.strip()
                        else:
                            Code      = f'{main+"["+secondary+"]"}'.strip()
                    
                        
                        newCode   = checkArgs(args, Code)
                        finalCode = await checkArgCheck(args, newCode, Context)

                        await findBracketPairs(finalCode, TotalFuncs, Context)

                else:
                    newCode   = checkArgs(args, Code)
                    finalCode = await checkArgCheck(args, newCode, Context)

                    await findBracketPairs(finalCode, TotalFuncs, Context)

        
            

        COGS = type(Cog_Group, (commands.Cog,), {'__init__': main_bod.__init__, 'go': main_bod.go})
        try:
            bots.add_cog(COGS(bots))
        except:
            pass
