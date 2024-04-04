from CharmCord.CharmErrorHandling import CharmCordErrors
from CharmCord.globeHandler import get_globals

async def sendDM(args, context):
    bots = get_globals()[1]
    if ";" not in args:
        CharmCordErrors(f"Not enough arguments in $sendDM: {context.command.name} command")

    values = args.split(";")
    user = values[0].replace("<@", "").replace(">", "")
    message = values[1]
    dm = await bots.fetch_user(user)
    await dm.send(message)
    return
