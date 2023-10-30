from CharmCord.CharmErrorHandling import CharmCordErrors


async def channelNsfw(id, context):
    """
    Ex. $channelNsfw[ChannelID]
    returns a boolean about a channel nsfw setting
    """
    if len(id) < 1:
        CharmCordErrors("No parameter provided for '$channelNsfw'")
    from CharmCord.utils.CharmCord import bots

    try:
        channel = await bots.fetch_channel(id.replace("<#", "").replace(">", ""))
        if channel.is_nsfw():
            return True
        else:
            return False
    except ValueError:
        CharmCordErrors(f"id ({id}) is an invalid Channel ID")
