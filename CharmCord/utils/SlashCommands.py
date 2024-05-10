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
                from CharmCord.tools import no_arguments, slash_args, find_bracket_pairs, lets
                funcs = get_globals()[0]
                context = ctx
                new = []
                for i in arguments:
                    new.append(eval(i['name']))
                finalCode = await no_arguments(codes, funcs, context)
                finalCode = slash_args(new, finalCode)
                await find_bracket_pairs(finalCode, funcs, context)
                if len(lets) >= 1:
                    lets.clear()
        """
        func2 = f"""
@bot.tree.command(name=name)
async def go(ctx, {', '.join(new_args)}):
                '''{description}
                '''
                from CharmCord.globeHandler import get_globals
                from CharmCord.tools import no_arguments, slash_args, find_bracket_pairs, lets
                funcs = get_globals()[0]
                context = ctx
                new = []
                finalCode = await no_arguments(codes, funcs, context)
                await find_bracket_pairs(finalCode, funcs, context)
                if len(lets) >= 1:
                    lets.clear()
        """
        if args is None:
            exec(func2, needs)
        else:
            exec(func, needs)
