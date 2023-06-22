async def channelID(empty, Context):
    """
    Ex. $channelID
    return channel ID for the current channel
    """
    return Context.channel.id
