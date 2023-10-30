from CharmCord.CharmErrorHandling import CharmCordErrors


async def channelName(id, context):
    """
    Ex. $channelName[ChannelID]
    returns channel name of the given args
    """
    if len(id) < 1:
        CharmCordErrors("No parameter provided for '$channelName'")
    from CharmCord.utils.CharmCord import bots

    try:
        channel = await bots.fetch_channel(id.replace("<#", "").replace(">", ""))
        return channel.name
    except ValueError:
        CharmCordErrors(f"$channelName: {id} not valid channel id\nCommand: {context.command.name}")
