from ._btnOpts_ import currently_selected
from ...CharmErrorHandling import CharmCordError


async def selectedDropdown(args, ctx):
    if args == '':
        for item in currently_selected:
            if f"{ctx.guild.id}" in item:
                return item.get(f"{ctx.guild.id}")

    else:
        try:
            for item in currently_selected:
                if f"{ctx.guild.id}" in item:
                    return item.get(f"{ctx.guild.id}")[int(args) - 1]

        except ValueError:
            raise CharmCordError(
                error_msg="Not a valid dropdown option",
                code_sample=args,
                command_name=ctx.command.name
            )
