import CharmCord.CharmErrorHandling as ErrorHandling

EH = ErrorHandling.CharmErrorHandling()


async def guildID(empty, context):
    """Get guild id of the guild where command was invoked"""
    return context.guild.id
