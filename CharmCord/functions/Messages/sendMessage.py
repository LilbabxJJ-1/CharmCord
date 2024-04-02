from CharmCord.all_functions import newline_char
from discord.ui import view
from btnOpts import buttons


async def sendMessage(args: str, context):
    from CharmCord.utils.CharmCord import bots

    split = args.split(";")
    if len(split) < 2:
        raise SyntaxError("args or message not provided to $sendMessage")
    try:
        channel_id = split[0]
        channel = await bots.fetch_channel(int(channel_id))
        if len(split) > 1:
            message = split[1]
            message = message.replace(newline_char, "\n")
            if len(buttons) > 0:
                sent = await channel.send(message, view=buttons[0])
            else:
                sent = await channel.send(message)
        if len(buttons) > 0:
            sent = await channel.send(view=buttons[0])
    except:
        raise SyntaxError("Can't send empty message!")
    return sent.id
