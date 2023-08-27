from CharmCord.CharmErrorHandling import CharmCordErrors


async def purge(args, context):
    from CharmCord.Classes.CharmCord import bots
    vals = args.split(";")
    channel = vals[0]
    amount = vals[1]

    try:
        channel = await bots.fetch_channel(channel)
    except:
        CharmCordErrors(f"{channel} not a channel ID or Name")
    try:
        await channel.purge(limit=int(amount))
    except ValueError:
        CharmCordErrors(f"{amount} is not a digit! Needs to be digit")
