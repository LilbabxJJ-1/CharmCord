import CharmCord.CharmErrorHandling as ErrorHandling
from CharmCord.CharmErrorHandling import CharmCordErrors
EH = ErrorHandling.CharmErrorHandling()


async def channelMention(ID, Context):
    """
    Ex. $channelMention[ChannelID]
    returns a channel mention from the given ID
    """
    if len(ID) < 1:
        raise EH.Errors(4, "No parameter provided for '$channelMention'")
    from CharmCord.Classes.CharmCord import bots

    try:
        int(ID)
        channel = await bots.fetch_channel(ID)
        return channel.mention
    except ValueError:
        CharmCordErrors(f"$channelMention: {ID} not valid channel id\nCommand: {Context.command.name}")
