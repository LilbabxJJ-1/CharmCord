import asyncio
from ast import literal_eval


class SlashCommands:
    def slashCommand(self, name, code, args, description=""):
        from CharmCord.Classes.CharmCord import bots
        newArgs = []
        for i in args:
            newArgs.append(f"{i}: str")
        function_definition = f"""@bots.tree.command(name=name, description=description)
async def go(ctx, {', '.join(newArgs)}):
                from CharmCord.Classes.CharmCord import TotalFuncs
                Context = ctx
                new = []
                for i in args:
                    new.append(eval(i))
                finalCode = await noArguments(codes, TotalFuncs, Context)
                finalCode = slashArgs(new, finalCode)
                await findBracketPairs(finalCode, TotalFuncs, Context)
                
        """

        # Import required module
        from CharmCord.Classes.CharmCord import TotalFuncs
        exec(function_definition)
