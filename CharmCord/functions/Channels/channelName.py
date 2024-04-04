from CharmCord.CharmErrorHandling import CharmCordErrors
from CharmCord.globeHandler import get_globals

async def channelName(id, context):
    """
    Ex. $channelName[ChannelID]
    returns channel name of the given args
    """
    if len(id) < 1:
        CharmCordErrors("No parameter provided for '$channelName'")
    bots = get_globals()[1]

    try:
        channel = await bots.fetch_channel(id.replace("<#", "").replace(">", ""))
        return channel.name
    except ValueError:
        CharmCordErrors(f"$channelName: {id} not valid channel id\nCommand: {context.command.name}")
