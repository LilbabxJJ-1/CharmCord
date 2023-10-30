from CharmCord.CharmErrorHandling import CharmCordErrors


async def channelType(id, context):
    """
    Ex. $channelType[ChannelID]
    returns the channel type of the given args
    """
    if len(id) < 1:
        CharmCordErrors("No parameter provided for '$channelType'")
    from CharmCord.utils.CharmCord import bots

    try:
        channel = await bots.fetch_channel(id.replace("<#", "").replace(">", ""))
        return channel.type
    except ValueError:
        CharmCordErrors(f"$channelType: {id} not valid channel id\nCommand: {context.command.name}")
