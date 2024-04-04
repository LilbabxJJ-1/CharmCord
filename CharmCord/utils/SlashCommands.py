class SlashCommands:

    @staticmethod
    def slash_command(name, code, args: list[dict] = None, description=None, bot=None):
        types = {1: "str", 2: "int"}
        new_args = []
        arg_descripts = []
        if args is not None:
            for i in args:
                if len(i) != 0:
                    try:
                        i['description']
                    except KeyError:
                        i['description'] = "No Description"
                    new_args.append(f"{i['name']}: {types[i['type']]}")
                    arg_descripts.append(f"{i['name']} ({types[i['type']]}): {i['description']}")
                    needs = {"arguments": args, "codes": code, "bot": bot, "name": name}
        else:
            needs = {"codes": code, "bot": bot, "name": name}
        nl = "\n\t\t\t"
        func = f"""
@bot.tree.command(name=name)
async def go(ctx, {', '.join(new_args)}):
                '''{description}
                
                Args:
                    {nl.join(arg_descripts)}
                '''
                from CharmCord.globeHandler import get_globals
                from CharmCord.tools import noArguments, slashArgs, findBracketPairs, lets
                funcs = get_globals()[0]
                context = ctx
                new = []
                for i in arguments:
                    new.append(eval(i['name']))
                finalCode = await noArguments(codes, funcs, context)
                finalCode = slashArgs(new, finalCode)
                await findBracketPairs(finalCode, funcs, context)
                if len(lets) >= 1:
                    lets.clear()
        """
        func2 = f"""
@bot.tree.command(name=name)
async def go(ctx, {', '.join(new_args)}):
                '''{description}
                '''
                from CharmCord.globeHandler import get_globals
                from CharmCord.tools import noArguments, slashArgs, findBracketPairs, lets
                funcs = get_globals()[0]
                context = ctx
                new = []
                finalCode = await noArguments(codes, funcs, context)
                await findBracketPairs(finalCode, funcs, context)
                if len(lets) >= 1:
                    lets.clear()
        """
        if args is None:
            exec(func2, needs)
        else:
            exec(func, needs)
