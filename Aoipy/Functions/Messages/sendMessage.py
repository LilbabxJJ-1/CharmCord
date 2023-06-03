async def sendMessage(args: str, Context):
    from Aoipy.Classes.AoiPyClient import bots
    split = args.split(";")
    try:
        channel_id = split[0]
        message = split[1]
        channel = await bots.fetch_channel(int(channel_id))
        await channel.send(message)
    except:
        raise SyntaxError("Can't send empty message!")
    return
