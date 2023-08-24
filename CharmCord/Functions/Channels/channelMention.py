import CharmCord.CharmErrorHandling as ErrorHandling

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
        CharmCord_Errors(f"$channelMention: {ID} not valid channel id\nCommand: {Context.command.name}")
