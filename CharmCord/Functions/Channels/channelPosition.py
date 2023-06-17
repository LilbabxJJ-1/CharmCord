import CharmCord.CharmErrorHandling as ErrorHandling

EH = ErrorHandling.CharmErrorHandling()


async def channelPosition(ID, Context):
    if len(ID) < 1:
        raise EH.Errors(4, "No parameter provided for '$channelPosition'")
    from CharmCord.Classes.CharmCord import bots

    try:
        int(ID)
        channel = await bots.fetch_channel(ID)
        return str(channel.position)
    except ValueError:
        EH.Errors(2, ID)
