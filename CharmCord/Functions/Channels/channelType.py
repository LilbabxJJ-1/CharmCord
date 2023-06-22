import CharmCord.CharmErrorHandling as ErrorHandling

EH = ErrorHandling.CharmErrorHandling()


async def channelType(ID, Context):
    """
    Ex. $channelType[ChannelID]
    returns the channel type of the given ID
    """
    if len(ID) < 1:
        raise EH.Errors(4, "No parameter provided for '$channelType'")
    from CharmCord.Classes.CharmCord import bots

    try:
        int(ID)
        channel = await bots.fetch_channel(ID)
        return channel.type
    except ValueError:
        EH.Errors(2, ID)
