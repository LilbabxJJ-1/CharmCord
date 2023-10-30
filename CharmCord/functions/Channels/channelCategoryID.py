from CharmCord.CharmErrorHandling import CharmCordErrors


async def channelCategoryID(args: str, context):
    """
    Ex. $channelCategoryID[ChannelID]
    Returns the args of the current category args
    """
    from CharmCord.utils.CharmCord import bots

    try:
        channel = await bots.fetch_channel(args.replace("<#", "").replace(">", ""))
        return channel.category.id
    except ValueError:
        CharmCordErrors(f"$channelCategoryID: {args} not valid channel id\nCommand: {context.command.name}")
