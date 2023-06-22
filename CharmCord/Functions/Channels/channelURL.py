import CharmCord.CharmErrorHandling as ErrorHandling

EH = ErrorHandling.CharmErrorHandling()


async def channelURL(ID, Context):
    """
    Ex. $channelURL
    returns the channel url to the given ID
    """
    if len(ID) < 1:
        raise EH.Errors(4, "No parameter provided for '$channelURL'")
    from CharmCord.Classes.CharmCord import bots

    try:
        int(ID)
        channel = await bots.fetch_channel(ID)
        return channel.jump_url
    except ValueError:
        EH.Errors(2, ID)
