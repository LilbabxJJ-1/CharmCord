import CharmCord.CharmErrorHandling as ErrorHandling

EH = ErrorHandling.CharmErrorHandling()


async def channelChangedRoles(ID, Context):
    """
    Ex. $channelChangedRoles[ChannelID]
    """
    if len(ID) < 1:
        raise EH.Errors(4, "No parameter provided for '$channelChangedRoles'")
    from CharmCord.Classes.CharmCord import bots

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
