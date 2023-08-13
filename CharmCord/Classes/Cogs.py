from CharmCord.tools import checkArgCheck, checkArgs, findBracketPairs, noArguments, isValid

AC = {}


class Charmcogs:
    def commandcogs(self, name, code):
        from .CharmCord import bots

        @bots.command(name=name)
        async def go(ctx, *args, code=code):
            from CharmCord.Classes.CharmCord import TotalFuncs

            Context = ctx
            newcode = await checkArgCheck(args, code, Context)
            if newcode == "Failed":
                return
            finalcode = await noArguments(newcode, TotalFuncs, Context)
            finalcode = checkArgs(args, finalcode)
            finalcode = await isValid(finalcode, TotalFuncs)
            await findBracketPairs(finalcode, TotalFuncs, Context)

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