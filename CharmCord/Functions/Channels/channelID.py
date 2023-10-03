async def channelID(empty, Context):
    """
    Ex. $channelID
    return channel args for the current channel
    """
    return Context.channel.id
