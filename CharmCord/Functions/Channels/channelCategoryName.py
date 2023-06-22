import CharmCord.CharmErrorHandling as ErrorHandling

EH = ErrorHandling.CharmErrorHandling()


async def channelCategoryName(ID, Context):
    """
    Ex. $channelCategoryName[ChannelID]
    returns the name of the category name of the given ID
    """
    if len(ID) < 1:
        raise EH.Errors(4, "No parameter provided for '$channelCategoryName'")
    from CharmCord.Classes.CharmCord import bots

    try:
        int(ID)
        channel = await bots.fetch_channel(ID)
        return channel.category.name
    except ValueError:
        EH.Errors(3, ID)
