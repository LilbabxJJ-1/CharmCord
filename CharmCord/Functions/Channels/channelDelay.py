from CharmCord.CharmErrorHandling import CharmCordErrors


async def channelDelay(ID, Context):
    """
    Ex. $channelDelay[ChannelID]
    Returns the channel delay for the given channel args
    """
    if len(ID) < 1:
        raise CharmCordErrors("No parameter provided for '$channelDelay'")
    from CharmCord.Classes.CharmCord import bots

    try:
        channel = await bots.fetch_channel(ID.replace("<#", "").replace(">", ""))
        return channel.delay
    except ValueError:
        CharmCordErrors(f"$channelDelay: {ID} not valid channel id\nCommand: {Context.command.name}")
