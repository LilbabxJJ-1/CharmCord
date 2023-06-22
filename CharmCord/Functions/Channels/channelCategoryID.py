import CharmCord.CharmErrorHandling as ErrorHandling

EH = ErrorHandling.CharmErrorHandling()


async def channelCategoryID(empty, Context):
    """
    Ex. $channelCategoryID
    Returns the ID of the current category ID
    """
    pass

    try:
        int(Context.channel.category.id)
    except ValueError:
        EH.Errors(3, "None")
    return Context.channel.category.id
