class SlashCommands:

    @staticmethod
    def slash_command(name, code, args: list[dict], description=None, bot=None):
        types = {1: "str", 2: "int"}
        new_args = []
        arg_descripts = []
        for i in args:
            if len(i) != 0:
                try:
                    i['description']
                except KeyError:
                    i['description'] = "No Description"
                new_args.append(f"{i['name']}: {types[i['type']]}")
                arg_descripts.append(f"{i['name']} ({types[i['type']]}): {i['description']}")
        nl = "\n\t\t\t"
        needs = {"arguments": args, "codes": code, "bot": bot, "name": name}
        func = f"""
@bot.tree.command(name=name)
async def go(ctx, {', '.join(new_args)}):
                '''{description}
                
                Args:
                    {nl.join(arg_descripts)}
                '''
                from CharmCord.Classes.CharmCord import TotalFuncs
                from CharmCord.tools import noArguments, slashArgs, findBracketPairs
                Context = ctx
                new = []
                for i in arguments:
                    new.append(eval(i['name']))
                finalCode = await noArguments(codes, TotalFuncs, Context)
                finalCode = slashArgs(new, finalCode)
                await findBracketPairs(finalCode, TotalFuncs, Context)
        """
        exec(func, needs)
