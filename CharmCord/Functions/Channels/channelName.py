from CharmCord.CharmErrorHandling import CharmCordErrors


async def channelName(ID, Context):
    """
    Ex. $channelName[ChannelID]
    returns channel name of the given args
    """
    if len(ID) < 1:
        CharmCordErrors("No parameter provided for '$channelName'")
    from CharmCord.Classes.CharmCord import bots

    try:
        channel = await bots.fetch_channel(ID.replace("<#", "").replace(">", ""))
        return channel.name
    except ValueError:
        CharmCordErrors(f"$channelName: {ID} not valid channel id\nCommand: {Context.command.name}")
