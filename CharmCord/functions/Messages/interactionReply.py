import discord
from CharmCord.all_functions import newline_char
from CharmCord.functions.Messages._btnOpts_ import views


async def interactionReply(args, interaction: discord.Interaction):
    try:
        message = args
        message = message.replace(newline_char, "\n")
        if len(views) > 0:
            await interaction.response.send_message(message, view=views[0])
            return
        await interaction.response.send_message(message)
    except Exception as e:
        raise SyntaxError("Can't send empty message!")
    return