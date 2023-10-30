async def message(emp, context):
    from CharmCord.utils.CharmCord import bots
    remove = ""
    if str(bots.command_prefix) in context.message.content:
        for i in context.message.content:
            if i == " ":
                break
            else:
                remove += i
    return str(context.message.content).replace(remove, "")
