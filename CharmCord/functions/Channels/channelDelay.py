from CharmCord.CharmErrorHandling import CharmCordErrors
from CharmCord.globeHandler import get_globals

async def channelDelay(id, context):
    """
    Ex. $channelDelay[ChannelID]
    Returns the channel delay for the given channel args
    """
    if len(id) < 1:
        raise CharmCordErrors("No parameter provided for '$channelDelay'")
    bots = get_globals()[1]

    try:
        channel = await bots.fetch_channel(id.replace("<#", "").replace(">", ""))
        return channel.delay
    except ValueError:
        CharmCordErrors(f"$channelDelay: {id} not valid channel id\nCommand: {context.command.name}")
