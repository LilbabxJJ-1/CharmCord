import CharmCord.CharmErrorHandling as ErrorHandling

EH = ErrorHandling.CharmErrorHandling()


async def channelMention(ID, Context):
    if len(ID) < 1:
        raise EH.Errors(4, "No parameter provided for '$channelMention'")
    from CharmCord.Classes.CharmCord import bots
    try:
        int(ID)
        channel = await bots.fetch_channel(ID)
        return channel.mention
    except ValueError:
        EH.Errors(2, ID)