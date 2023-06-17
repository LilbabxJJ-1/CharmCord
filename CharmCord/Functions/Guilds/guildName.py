import CharmCord.CharmErrorHandling as ErrorHandling

EH = ErrorHandling.CharmErrorHandling()


async def guildName(ID, Context):
    if len(ID) < 1:
        raise EH.Errors(4, "No parameter provided for '$guildName'")
    from CharmCord.Classes.CharmCord import bots

    try:
        int(ID)
        guild = await bots.fetch_guild(ID)
        return guild.name
    except ValueError:
        EH.Errors(2, ID)
