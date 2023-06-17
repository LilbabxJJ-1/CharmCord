async def messageAuthor(IDs, Context):
    from CharmCord.Classes.CharmCord import bots

    try:
        args = IDs.split(";")
        channel = await bots.fetch_channel(args[0])
        mes = int(args[1])
        message = await channel.fetch_message(mes)
        return message.author
    except:
        raise SyntaxError("Not a message ID")
