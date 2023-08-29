from CharmCord.CharmErrorHandling import CharmCordErrors


async def channelPosition(ID, Context):
    """
    Ex. $channelPosition[ChannelID]
    returns the position of a given channel ID
    """
    if len(ID) < 1:
        CharmCordErrors("No parameter provided for '$channelPosition'")
    from CharmCord.Classes.CharmCord import bots

    try:
        channel = await bots.fetch_channel(ID.replace("<#", "").replace(">", ""))
        return channel.position
    except ValueError:
        CharmCordErrors(f"$channelPosition: {ID} not valid channel id\nCommand: {Context.command.name}")
