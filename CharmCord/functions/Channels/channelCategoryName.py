from CharmCord.CharmErrorHandling import CharmCordErrors
from CharmCord.globeHandler import get_globals

async def channelCategoryName(args, context):
    """
    Ex. $channelCategoryName[ChannelID]
    returns the name of the category name of the given args
    """
    if len(args) < 1:
        CharmCordErrors("No parameter provided for '$channelCategoryName'")
    bots = get_globals()[1]

    try:
        channel = await bots.fetch_channel(args.replace("<#", "").replace(">", ""))
        return channel.category.name
    except ValueError:
        CharmCordErrors(f"$channelCategoryName: {args} not valid channel id\nCommand: {context.command.name}")
