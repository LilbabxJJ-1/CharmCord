from CharmCord.tools import check_args_check, check_args, find_bracket_pairs, no_arguments, is_valid
from CharmCord.globeHandler import get_globals

AC = {}


class CharmCogs:

    @staticmethod
    def command_cogs(name, code):
        funcs = get_globals()[0]
        bots = get_globals()[1]

        @bots.command(name=name)
        async def go(ctx, *args, codes=code):
            context = ctx
            new_code = await check_args_check(args, codes, context)
            if new_code == "Failed":
                return
            code1 = await no_arguments(new_code, funcs, context)
            code2 = check_args(args, code1)
            final_code = await is_valid(code2, funcs)
            await find_bracket_pairs(final_code, funcs, context)

    @staticmethod
    def slashcommand_cogs(name: str, code: str, args: list[dict], description: str):

        def slash_command():
            bots = get_globals()[1]
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
            nl = "\n\t\t\t\t\t\t\t\t"
            needs = {"arguments": args, "codes": code, "bot": bots, "name": name}
            func = f"""@bot.tree.command(name=name)
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
            exec(func, needs)

        slash_command()
