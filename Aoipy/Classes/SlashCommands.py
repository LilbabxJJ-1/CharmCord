from Aoipy.tools import findBracketPairs, checkArgs, checkArgCheck, noArguments, slashArgs
import inspect

class SlashCommands:

    def slashCommand(self, Name, Code, Args, Description=''):
        global code
        global args
        global parem
        code = Code
        args = Args
        from .AoiPyClient import bots
        function_definition = f"""@bots.slash_command(name=Name, description=Description)
async def go(ctx, {', '.join(Args)}):
                global code
                global args
                from Aoipy.Classes.AoiPyClient import TotalFuncs
                Context = ctx
                new = []
                for i in args:
                    new.append(eval(i))
                finalCode = await noArguments(code, TotalFuncs, Context)
                finalCode = slashArgs(new, finalCode)
                await findBracketPairs(finalCode, TotalFuncs, Context)
                
        """

        exec(function_definition)
