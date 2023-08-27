import CharmCord.CharmErrorHandling as ErrorHandling

EH = ErrorHandling.CharmErrorHandling()


async def channelPosition(ID, Context):
    """
    Ex. $channelPosition[ChannelID]
    returns the position of a given channel ID
    """
    if len(ID) < 1:
        raise EH.Errors(4, "No parameter provided for '$channelPosition'")
    from CharmCord.Classes.CharmCord import bots

    try:
        int(ID)
        channel = await bots.fetch_channel(ID)
        return str(channel.position + 1)
    except ValueError:
        EH.Errors(2, ID)
