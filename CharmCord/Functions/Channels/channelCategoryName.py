from CharmCord.CharmErrorHandling import CharmCordErrors


async def channelCategoryName(ID, Context):
    """
    Ex. $channelCategoryName[ChannelID]
    returns the name of the category name of the given ID
    """
    if len(ID) < 1:
        CharmCordErrors("No parameter provided for '$channelCategoryName'")
    from CharmCord.Classes.CharmCord import bots

    try:
        channel = await bots.fetch_channel(ID.replace("<#", "").replace(">", ""))
        return channel.category.name
    except ValueError:
        CharmCordErrors(f"$channelCategoryName: {ID} not valid channel id\nCommand: {Context.command.name}")
