from CharmCord.CharmErrorHandling import CharmCordErrors


async def mentions(ids, context):
    try:
        return context.message.mentions[int(ids) - 1].id
    except ValueError:
        CharmCordErrors("Invalid args in $mentions | Command..")
    except IndexError:
        return None
