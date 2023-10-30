from CharmCord.CharmErrorHandling import CharmCordErrors


async def channelChangedRoles(args, context):
    """
    Ex. $channelChangedRoles[ChannelID;Index]
    """
    if len(args) < 1:
        CharmCordErrors("No parameter provided for '$channelChangedRoles'")
        return
    from CharmCord.utils.CharmCord import bots

    if ";" in args:
        args = args.split(";")
        args = args[0]
        index = args[1]
        try:
            int(args)
            channel = await bots.fetch_channel(args)
            return channel.changed_roles[int(index) - 1]
        except ValueError:
            CharmCordErrors("No parameter provided for '$channelCategoryRoles'")
    else:
        try:
            int(args)
            channel = await bots.fetch_channel(args)
            return channel.changed_roles
        except ValueError:
            CharmCordErrors("No parameter provided for '$channelCategoryRoles'")
