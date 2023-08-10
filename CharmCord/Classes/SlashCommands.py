import discord


class SlashCommands:

    def slashCommand(self, name, code, args: list, description=None):
        from CharmCord.Classes.CharmCord import bots
        newArgs = []
        for i in args:
            newArgs.append(f"{i}: str")
        needs = {"arguments": args, "codes": code, "bots": bots, "name": name, "description": description}
        func = f"""
@bots.tree.command(name=name, description=description)
async def go(ctx, {', '.join(newArgs)}):
                from CharmCord.Classes.CharmCord import TotalFuncs
                from CharmCord.tools import noArguments, slashArgs, findBracketPairs
                Context = ctx
                new = []
                for i in arguments:
                    new.append(eval(i))
                finalCode = await noArguments(codes, TotalFuncs, Context)
                finalCode = slashArgs(new, finalCode)
                await findBracketPairs(finalCode, TotalFuncs, Context)
        """
        exec(func, needs)
