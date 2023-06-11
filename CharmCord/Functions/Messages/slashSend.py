from CharmCord.all_functions import newline_char


async def slashSend(args: str, Context):
    try:
        message = args
        message = message.replace(newline_char, "\n")
        await Context.respond(message)
    except:
        raise SyntaxError("Can't send empty message!")
    return
