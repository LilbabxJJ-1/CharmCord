from CharmCord.CharmErrorHandling import CharmCordErrors


async def channelMention(ID, Context):
    """
    Ex. $channelMention[ChannelID]
    returns a channel mention from the given args
    """
    if len(ID) < 1:
        CharmCordErrors("No parameter provided for '$channelMention'")
    from CharmCord.Classes.CharmCord import bots

    try:
        channel = await bots.fetch_channel(ID.replace("<#", "").replace(">", ""))
        return channel.mention
    except ValueError:
        CharmCordErrors(f"$channelMention: {ID} not valid channel id\nCommand: {Context.command.name}")
