import CharmCord.CharmErrorHandling as ErrorHandling

EH = ErrorHandling.CharmErrorHandling()


async def channelNsfw(ID, Context):
    if len(ID) < 1:
        raise EH.Errors(4, "No parameter provided for '$channelNsfw'")
    from CharmCord.Classes.CharmCord import bots

    try:
        int(ID)
        channel = await bots.fetch_channel(ID)
        if channel.is_nsfw():
            return "nsfw"
        else:
            return "not nsfw"
    except ValueError:
        EH.Errors(2, ID)
