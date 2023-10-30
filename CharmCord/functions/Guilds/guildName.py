import CharmCord.CharmErrorHandling as ErrorHandling

EH = ErrorHandling.CharmErrorHandling()


async def guildName(id, context):
    if len(id) < 1:
        raise EH.Errors(4, "No parameter provided for '$guildName'")
    from CharmCord.utils.CharmCord import bots

    try:
        int(id)
        guild = await bots.fetch_guild(id)
        return guild.name
    except ValueError:
        EH.Errors(2, id)
