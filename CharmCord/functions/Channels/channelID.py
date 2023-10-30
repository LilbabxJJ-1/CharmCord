async def channelID(empty, context):
    """
    Ex. $channelID
    return channel args for the current channel
    """
    return context.channel.id
