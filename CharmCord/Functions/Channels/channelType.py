import CharmCord.CharmErrorHandling as ErrorHandling

EH = ErrorHandling.CharmErrorHandling()


async def channelType(ID, Context):
    if len(ID) < 1:
        raise EH.Errors(4, "No parameter provided for '$channelType'")
    from CharmCord.Classes.CharmCord import bots

    try:
        int(ID)
        channel = await bots.fetch_channel(ID)
        return channel.type
    except ValueError:
        EH.Errors(2, ID)
