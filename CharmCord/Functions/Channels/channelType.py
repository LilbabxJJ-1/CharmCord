from CharmCord.CharmErrorHandling import CharmCordErrors


async def channelType(ID, Context):
    """
    Ex. $channelType[ChannelID]
    returns the channel type of the given ID
    """
    if len(ID) < 1:
        CharmCordErrors("No parameter provided for '$channelType'")
    from CharmCord.Classes.CharmCord import bots

    try:
        channel = await bots.fetch_channel(ID.replace("<#", "").replace(">", ""))
        return channel.type
    except ValueError:
        CharmCordErrors(f"$channelType: {ID} not valid channel id\nCommand: {Context.command.name}")
