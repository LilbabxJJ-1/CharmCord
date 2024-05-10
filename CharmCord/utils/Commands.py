from CharmCord.tools import check_args_check, check_args, find_bracket_pairs, no_arguments, lets, is_valid
from CharmCord.globeHandler import get_globals


class Commands:

    @staticmethod
    def command(name: str, code: str, aliases: list, bot=None):
        # Define command function dynamically

        @bot.command(name=name, aliases=aliases)
        async def go(ctx, *args, codes=code):
            funcs = get_globals()[0]
            new_code = await check_args_check(args, codes, ctx)
            if new_code == "Failed":
                return
            code1 = await no_arguments(new_code, funcs, ctx)
            code2 = check_args(args, code1)
            final_code = await is_valid(code2, funcs)
            await find_bracket_pairs(final_code, funcs, ctx)
            if len(lets) >= 1:
                lets.clear()
