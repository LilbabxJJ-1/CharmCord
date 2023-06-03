import Aoipy.AoiErrorHandling as ErrorHandling

EH = ErrorHandling.AoipyErrorHandling()


async def channelChangedRoles(ID, Context):
    if len(ID) < 1:
        raise EH.Errors(4, "No parameter provided for '$channelChangedRoles'")
    from Aoipy.Classes.AoiPyClient import bots
    if ";" in ID:
        args = ID.split(";")
        ID = args[0]
        Index = args[1]
        try:
            int(ID)
            channel = await bots.fetch_channel(ID)
            return channel.changed_roles[int(Index) - 1]
        except ValueError:
            EH.Errors(2, ID)
    else:
        try:
            int(ID)
            channel = await bots.fetch_channel(ID)
            return channel.changed_roles
        except ValueError:
            EH.Errors(2, ID)