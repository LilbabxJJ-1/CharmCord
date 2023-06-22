import CharmCord.CharmErrorHandling as ErrorHandling

EH = ErrorHandling.CharmErrorHandling()


async def channelName(ID, Context):
    """
    Ex. $channelName[ChannelID]
    returns channel name of the given ID
    """
    if len(ID) < 1:
        raise EH.Errors(4, "No parameter provided for '$channelName'")
    from CharmCord.Classes.CharmCord import bots

    try:
        int(ID)
        channel = await bots.fetch_channel(ID)
        return channel.name
    except ValueError:
        EH.Errors(2, ID)
