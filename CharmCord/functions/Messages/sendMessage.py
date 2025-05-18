import discord

from CharmCord.all_functions import newline_char
from ._btnOpts_ import views
from CharmCord.globeHandler import get_globals
from ...CharmErrorHandling import CharmCordError


async def sendMessage(args: str, context):
    bots = get_globals()[1]
    split = args.split(";")
    ephemeral = False
    if len(split) < 2:
        raise CharmCordError("Channel, message not provided to $sendMessage",
                             args,
                             context.command.name)
    try:
        channel_id = split[0]
        channel = await bots.fetch_channel(int(channel_id))
        if len(split) > 1:
            message = split[1]
            message = message.replace(newline_char, "\n")
            if len(views) > 0:
                sent = await channel.send(message, view=views[0])
                return sent.id
            else:
                sent = await channel.send(message)
                return sent.id
        if len(views) > 0:
            sent = await channel.send(view=views)
            return sent.id
    except Exception as e:
        print(e)
        raise SyntaxError("Can't send empty message!")
