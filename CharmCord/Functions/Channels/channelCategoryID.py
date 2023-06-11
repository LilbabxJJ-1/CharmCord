import CharmCord.CharmErrorHandling as ErrorHandling

EH = ErrorHandling.CharmErrorHandling()


async def channelCategoryID(empty, Context):
    from CharmCord.Classes.CharmCord import bots
    try:
        int(Context.channel.category.id)
    except ValueError:
        EH.Errors(3, "None")
    return Context.channel.category.id