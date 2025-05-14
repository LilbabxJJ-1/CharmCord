from random import choice
from CharmCord.CharmErrorHandling import CharmCordError
async def random(args: str, context):
    """
    Use. $random[value;value;value;...]
    Ex. $random[cool;dog;city]

    :param args:
    :param context:
    :return: Random value from given list
    """
    data = args.split(';')
    if len(data) < 2:
        raise CharmCordError(
            error_msg="Not enough arguments in $random",
            code_sample=args,
            command_name=context.command.name
        )
    return choice(data)
