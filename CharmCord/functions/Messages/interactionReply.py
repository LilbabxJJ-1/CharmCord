import discord
from ._btnOpts_ import newline_char
from CharmCord.functions.Messages._btnOpts_ import views


async def interactionReply(args, interaction: discord.Interaction):
    arguments = args.split(";")
    try:
        message = arguments[0]
        message = message.replace(newline_char, "\n")
        ephemeral = False
        try:
            if arguments[1].lower() == 'true':
                ephemeral = True
        except IndexError:
            pass
        if len(views) > 0:
            await interaction.response.send_message(message, view=views[0], ephemeral=ephemeral)
            return
        await interaction.response.send_message(message, ephemeral=ephemeral)
    except Exception as e:
        raise SyntaxError("Can't send empty message!")
    return