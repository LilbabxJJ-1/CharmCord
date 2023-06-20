from CharmCord.all_functions import newline_char


async def sendMessage(args: str, Context):
    from CharmCord.Classes.CharmCord import bots

    split = args.split(";")
    if len(split) < 2:
        raise SyntaxError("ID or message not provided to $sendMessage")
    try:
        channel_id = split[0]
        message = split[1]
        channel = await bots.fetch_channel(int(channel_id))
        message = message.replace(newline_char, "\n")
        sent = await channel.send(message)
    except:
        raise SyntaxError("Can't send empty message!")
    return sent.id
