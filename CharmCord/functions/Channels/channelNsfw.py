from CharmCord.CharmErrorHandling import CharmCordErrors
from CharmCord.globeHandler import get_globals

async def channelNsfw(id, context):
    """
    Ex. $channelNsfw[ChannelID]
    returns a boolean about a channel nsfw setting
    """
    if len(id) < 1:
        CharmCordErrors("No parameter provided for '$channelNsfw'")
    bots = get_globals()[1]

    try:
        channel = await bots.fetch_channel(id.replace("<#", "").replace(">", ""))
        if channel.is_nsfw():
            return True
        else:
            return False
    except ValueError:
        CharmCordErrors(f"id ({id}) is an invalid Channel ID")
