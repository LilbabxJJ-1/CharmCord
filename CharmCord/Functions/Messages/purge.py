from CharmCord.CharmErrorHandling import CharmCordErrors


async def purge(args, context):
    def check(msg):
        if context.message.id != msg.id:
            return True
    from CharmCord.Classes.CharmCord import bots
    vals = args.split(";")
    channel = vals[0]
    amount = vals[1]
    try:
        checking = vals[2].lower()
    except IndexError:
        checking = "false"
    try:
        channel = await bots.fetch_channel(channel)
    except:
        CharmCordErrors(f"{channel} not a channel ID or Name")

    if checking == "true":
        try:
            await channel.purge(limit=int(amount), check=check)
        except ValueError:
            CharmCordErrors(f"{amount} is not a digit! Needs to be digit")
    elif checking == "false":
        try:
            await channel.purge(limit=int(amount))
        except ValueError:
            CharmCordErrors(f"{amount} is not a digit! Needs to be digit")