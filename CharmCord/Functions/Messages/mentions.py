from CharmCord.CharmErrorHandling import CharmCordErrors
async def mentions(IDs, Context):
    try:
        return Context.message.mentions[int(IDs)-1].id
    except ValueError:
        CharmCordErrors("Invalid ID in $mentions | Command..")
    except IndexError:
        return None
