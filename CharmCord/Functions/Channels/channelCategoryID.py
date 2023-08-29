from CharmCord.CharmErrorHandling import CharmCordErrors


async def channelCategoryID(ID: str, Context):
    """
    Ex. $channelCategoryID[ChannelID]
    Returns the ID of the current category ID
    """
    from CharmCord.Classes.CharmCord import bots

    try:
        channel = await bots.fetch_channel(ID.replace("<#", "").replace(">", ""))
        return channel.category.id
    except ValueError:
        CharmCordErrors(f"$channelCategoryID: {ID} not valid channel id\nCommand: {Context.command.name}")
