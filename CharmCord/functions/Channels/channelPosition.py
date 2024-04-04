from CharmCord.CharmErrorHandling import CharmCordErrors
from CharmCord.globeHandler import get_globals

async def channelPosition(id, context):
    """
    Ex. $channelPosition[ChannelID]
    returns the position of a given channel args
    """
    if len(id) < 1:
        CharmCordErrors("No parameter provided for '$channelPosition'")
    bots = get_globals()[1]

    try:
        channel = await bots.fetch_channel(id.replace("<#", "").replace(">", ""))
        return channel.position
    except ValueError:
        CharmCordErrors(f"$channelPosition: {id} not valid channel id\nCommand: {context.command.name}")
