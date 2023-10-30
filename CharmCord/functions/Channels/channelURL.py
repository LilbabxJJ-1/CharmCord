from CharmCord.CharmErrorHandling import CharmCordErrors


async def channelURL(id, context):
    """
    Ex. $channelURL
    returns the channel url to the given args
    """
    if len(id) < 1:
        CharmCordErrors("No parameter provided for '$channelURL'")
    from CharmCord.utils.CharmCord import bots

    try:
        channel = await bots.fetch_channel(id.replace("<#", "").replace(">", ""))
        return channel.jump_url
    except ValueError:
        CharmCordErrors(f"$channelURL: {id} not valid channel id\nCommand: {context.command.name}")
