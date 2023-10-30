from CharmCord.CharmErrorHandling import CharmCordErrors


async def channelCategoryName(args, context):
    """
    Ex. $channelCategoryName[ChannelID]
    returns the name of the category name of the given args
    """
    if len(args) < 1:
        CharmCordErrors("No parameter provided for '$channelCategoryName'")
    from CharmCord.utils.CharmCord import bots

    try:
        channel = await bots.fetch_channel(args.replace("<#", "").replace(">", ""))
        return channel.category.name
    except ValueError:
        CharmCordErrors(f"$channelCategoryName: {args} not valid channel id\nCommand: {context.command.name}")
