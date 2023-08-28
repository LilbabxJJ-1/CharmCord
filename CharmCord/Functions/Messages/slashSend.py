from CharmCord.all_functions import newline_char


async def slashSend(args: str, Context):
    try:
        message = args
        message = message.replace(newline_char, "\n")
        await Context.response.send_message(message)
    except Exception as e:
        print(e)
        raise SyntaxError("Can't send empty message!")
    return
