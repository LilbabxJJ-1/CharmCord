from CharmCord.CharmErrorHandling import CharmCordError
from CharmCord.globeHandler import get_globals

async def channelCategoryID(args: str, context):
    """
    Ex. $channelCategoryID[ChannelID]
    Returns the args of the current category args
    """
    bots = get_globals()[1]

    try:
        channel = await bots.fetch_channel(args.replace("<#", "").replace(">", ""))
        return channel.category.id
    except ValueError:
        CharmCordError(f"Not valid channel id for $channelCategoryID",
                       args,
                       context.command.name)
