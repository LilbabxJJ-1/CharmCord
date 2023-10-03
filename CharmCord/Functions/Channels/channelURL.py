from CharmCord.CharmErrorHandling import CharmCordErrors



async def channelURL(ID, Context):
    """
    Ex. $channelURL
    returns the channel url to the given args
    """
    if len(ID) < 1:
        CharmCordErrors("No parameter provided for '$channelURL'")
    from CharmCord.Classes.CharmCord import bots

    try:
        channel = await bots.fetch_channel(ID.replace("<#", "").replace(">", ""))
        return channel.jump_url
    except ValueError:
        CharmCordErrors(f"$channelURL: {ID} not valid channel id\nCommand: {Context.command.name}")
