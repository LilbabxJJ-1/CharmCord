import CharmCord.CharmErrorHandling as ErrorHandling

EH = ErrorHandling.CharmErrorHandling()


async def guildID(empty, Context):
    """Get guild id of the guild where command was invoked"""
    return Context.guild.id
