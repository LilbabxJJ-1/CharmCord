from CharmCord.tools import checkArgCheck, checkArgs, findBracketPairs, noArguments, isValid
from CharmCord.Classes.CharmCord import bots, TotalFuncs
AC = {}


class CharmCogs:

    @staticmethod
    def command_cogs(name, codes):
        from .CharmCord import bots

        @bots.command(name=name)
        async def go(ctx, *args, code=codes):

            context = ctx
            new_code = await checkArgCheck(args, code, context)
            if new_code == "Failed":
                return
            code1 = await noArguments(new_code, TotalFuncs, context)
            code2 = checkArgs(args, code1)
            final_code = await isValid(code2, TotalFuncs)
            await findBracketPairs(final_code, TotalFuncs, context)

    @staticmethod
    def slashcommand_cogs(name, code, args: list, description):
        def slash_command():
            new_args = []
            for i in args:
                new_args.append(f"{i}: str")
            needs = {"arguments": args, "codes": code, "bots": bots, "name": name, "description": description}
            func = f"""@bots.tree.command(name=name, description=description)
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
        slash_command()
