from CharmCord.tools import checkArgCheck, checkArgs, findBracketPairs, noArguments, lets, isValid
from CharmCord.globeHandler import get_globals

########################################
#              COMMANDS                #
########################################


class Commands:
    # Global variables

    @staticmethod
    def command(name: str, code: str, aliases: list = [], bot=None):
        # Define command function dynamically

        @bot.command(name=name, aliases=aliases)
        async def go(ctx, *args, codes=code):
            funcs = get_globals()[0]
            new_code = await checkArgCheck(args, codes, ctx)
            if new_code == "Failed":
                return
            code1 = await noArguments(new_code, funcs, ctx)
            code2 = checkArgs(args, code1)
            final_code = await isValid(code2, funcs)
            await findBracketPairs(final_code, funcs, ctx)
            if len(lets) >= 1:
                lets.clear()
