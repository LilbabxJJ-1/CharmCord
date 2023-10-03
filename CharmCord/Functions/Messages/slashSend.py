import discord

from CharmCord.all_functions import newline_char


async def slashSend(args: str, context: discord.Interaction):
    try:
        message = args
        message = message.replace(newline_char, "\n")
        try:
            await context.response.send_message(message)
        except Exception:
            await context.followup.send(message)
    except Exception as e:
        raise SyntaxError("Can't send empty message!")
    return
