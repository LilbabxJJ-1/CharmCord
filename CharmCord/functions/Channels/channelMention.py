from CharmCord.CharmErrorHandling import CharmCordErrors
from CharmCord.globeHandler import get_globals


async def channelMention(id, context):
    """
    Ex. $channelMention[ChannelID]
    returns a channel mention from the given args
    """
    if len(id) < 1:
        CharmCordErrors("No parameter provided for '$channelMention'")
    bots = get_globals()[1]

    try:
        channel = await bots.fetch_channel(id.replace("<#", "").replace(">", ""))
        return channel.mention
    except ValueError:
        CharmCordErrors(f"$channelMention: {id} not valid channel id\nCommand: {context.command.name}")
