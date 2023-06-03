import Aoipy.AoiErrorHandling as ErrorHandling

EH = ErrorHandling.AoipyErrorHandling()


async def guildID(empty, Context):
    """Get guild id of the guild where command was invoked"""
    return Context.guild.id