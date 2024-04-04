from CharmCord.globeHandler import get_globals


async def message(emp, context):
    bots = get_globals()[1]
    remove = ""
    if str(bots.command_prefix) in context.message.content:
        for i in context.message.content:
            if i == " ":
                break
            else:
                remove += i
    return str(context.message.content).replace(remove, "")
