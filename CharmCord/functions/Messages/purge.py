import discord

from CharmCord.CharmErrorHandling import CharmCordErrors

count = 0


async def purge(args, context):
    global count

    def check(msg):
        global count
        from CharmCord.utils.CharmCord import bots
        if isinstance(context, discord.Interaction):
            count += 1
            if msg.author.id != bots.user.id or count > 1:
                return True
        else:
            if context.message.id != msg.id:
                return True

    from CharmCord.utils.CharmCord import bots
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
            if isinstance(context, discord.Interaction):
                await context.response.defer()
                await channel.purge(limit=int(amount) + 1, check=check)
                count = 0
                return
            await channel.purge(limit=int(amount), check=check)
            count = 0
            return
        except ValueError:
            CharmCordErrors(f"{amount} is not a digit! Needs to be digit")
    elif checking == "false":
        try:
            await channel.purge(limit=int(amount))
        except ValueError:
            CharmCordErrors(f"{amount} is not a digit! Needs to be digit")
