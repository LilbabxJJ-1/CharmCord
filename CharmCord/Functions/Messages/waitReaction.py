import asyncio

from CharmCord.CharmErrorHandling import CharmCordErrors


async def waitReaction(args, context):
    """
    Ex. $waitMessage[ChannelID;User;emoji;timeout;timeoutErrMsg]
    """
    from CharmCord.Classes.CharmCord import bots
    split = args.split(";")
    if len(split) < 3:
        raise SyntaxError("args, User, or timeout not provided to $waitMessage")
    try:
        channel_id = split[0]
        users = split[1]
        emoji = split[2]
        timeout = int(split[3])

        def check(rct, usr):
            if int(channel_id) == context.channel.id:
                if users == "everyone":
                    if str(rct.emoji.name) == emoji:
                        return True
                elif int(users) == usr.id:
                    if str(rct.emoji.name) == emoji:
                        return True

        error = None
        if len(split[4]) > 1:
            error = split[4]
        if error is None:
            reaction, user = await bots.wait_for("reaction_add", timeout=timeout, check=check)
            try:
                return reaction.emoji.name
            except AttributeError:
                return reaction.emoji
        else:
            try:
                reaction, user = await bots.wait_for("reaction_add", timeout=timeout, check=check)
                try:
                    return reaction.emoji.name
                except AttributeError:
                    return reaction.emoji
            except asyncio.TimeoutError:
                await context.channel.send(error)
    except ValueError:
        CharmCordErrors(f"args Error in {context.command.name}")
        return
