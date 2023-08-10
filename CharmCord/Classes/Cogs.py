from CharmCord.tools import checkArgCheck, checkArgs, findBracketPairs, noArguments

AC = {}


class Charmcogs:
    def commandcogs(self, name, code):
        from .CharmCord import bots

        @bots.command(name=name)
        async def go(ctx, *args, code=code):
            from CharmCord.Classes.CharmCord import TotalFuncs

            Context = ctx
            newCode = checkArgs(args, code)
            if newCode == "Failed":
                return
            finalCode = await checkArgCheck(args, newCode, Context)
            finalCode = await noArguments(finalCode, TotalFuncs, Context)
            await findBracketPairs(finalCode, TotalFuncs, Context)

    def slashcommandcogs(self, name, code, args: list, description):
        def slashcommand():
            from CharmCord.Classes.CharmCord import bots
            newArgs = []
            for i in args:
                newArgs.append(f"{i}: str")
            needs = {"arguments": args, "codes": code, "bots": bots, "name": name, "description": description}
            func = f"""@bots.tree.command(name=name, description=description)
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
        slashcommand()