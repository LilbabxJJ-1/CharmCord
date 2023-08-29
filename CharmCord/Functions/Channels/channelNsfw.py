from CharmCord.CharmErrorHandling import CharmCordErrors


async def channelNsfw(ID, Context):
    """
    Ex. $channelNsfw[ChannelID]
    returns a boolean about a channel nsfw setting
    """
    if len(ID) < 1:
        CharmCordErrors("No parameter provided for '$channelNsfw'")
    from CharmCord.Classes.CharmCord import bots

    try:
        channel = await bots.fetch_channel(ID.replace("<#", "").replace(">", ""))
        if channel.is_nsfw():
            return True
        else:
            return False
    except ValueError:
        CharmCordErrors(f"ID ({ID}) is an invalid Channel ID")
