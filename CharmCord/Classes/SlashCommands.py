class SlashCommands:

    def slash_command(self, name, code, args: list, description=None, bot=None):
        new_args = []
        for i in args:
            new_args.append(f"{i}: str")
        needs = {"arguments": args, "codes": code, "bot": bot, "name": name, "description": description}
        func = f"""
@bot.tree.command(name=name, description=description)
async def go(ctx, {', '.join(new_args)}):
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
