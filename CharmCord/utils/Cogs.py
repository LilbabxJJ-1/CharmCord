from CharmCord.utils.CharmCord import bots, TotalFuncs
from CharmCord.tools import checkArgCheck, checkArgs, findBracketPairs, noArguments, isValid

AC = {}


class CharmCogs:

    @staticmethod
    def command_cogs(name, code):
        from .CharmCord import bots

        @bots.command(name=name)
        async def go(ctx, *args, codes=code):
            context = ctx
            new_code = await checkArgCheck(args, codes, context)
            if new_code == "Failed":
                return
            code1 = await noArguments(new_code, TotalFuncs, context)
            code2 = checkArgs(args, code1)
            final_code = await isValid(code2, TotalFuncs)
            await findBracketPairs(final_code, TotalFuncs, context)

    @staticmethod
    def slashcommand_cogs(name, code, args: list[dict], description):
        def slash_command():
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
            needs = {"arguments": args, "codes": code, "bot": bots, "name": name}
            func = f"""
            @bot.tree.command(name=name)
            async def go(ctx, {', '.join(new_args)}):
                            '''{description}

                            Args:
                                {nl.join(arg_descripts)}
                            '''
                            from CharmCord.utils.CharmCord import TotalFuncs
                            from CharmCord.tools import noArguments, slashArgs, findBracketPairs, lets
                            context = ctx
                            new = []
                            for i in arguments:
                                new.append(eval(i['name']))
                            finalCode = await noArguments(codes, TotalFuncs, context)
                            finalCode = slashArgs(new, finalCode)
                            await findBracketPairs(finalCode, TotalFuncs, context)
                            if len(lets) >= 1:
                                lets.clear()
                    """
            exec(func, needs)

        slash_command()
