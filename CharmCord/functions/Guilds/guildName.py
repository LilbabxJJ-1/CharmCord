from CharmCord.CharmErrorHandling import CharmCordErrors
from CharmCord.globeHandler import get_globals



async def guildName(id, context):
    if len(id) < 1:
        raise CharmCordErrors("No parameter provided for '$guildName'")
    bots = get_globals()[1]

    try:
        int(id)
        guild = await bots.fetch_guild(id)
        return guild.name
    except ValueError:
        CharmCordErrors("Invalid ID for '$guildName'")
