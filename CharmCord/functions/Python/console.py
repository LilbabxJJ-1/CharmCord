from CharmCord.CharmErrorHandling import CharmCordError


async def console(args, context):
    """
    Use. $console[text]
    Ex. $console[Hello world!]

    :param args:
    :param context:
    :return:
    """
    if args == "":
        CharmCordError("$Console was given no argument", "", context).command_error()
        return
    print(args)
    return
