async def messageAuthor(ids, context):
    from CharmCord.utils.CharmCord import bots

    try:
        args = ids.split(";")
        channel = await bots.fetch_channel(args[0])
        mes = int(args[1])
        message = await channel.fetch_message(mes)
        return message.author
    except:
        raise SyntaxError("Not a message args")
