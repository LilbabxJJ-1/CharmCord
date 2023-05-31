async def sendMessage(args: str, Context):
    from Aoipy.Functions.AoiCore import bots
    split = args.split(";")
    channel_id = split[0]
    message = split[1]
    channel = await bots.fetch_channel(int(channel_id))
    await channel.send(message)
    return