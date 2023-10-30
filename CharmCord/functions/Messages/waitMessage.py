import asyncio

from CharmCord.CharmErrorHandling import CharmCordErrors


async def waitMessage(args, context):
    """
    Ex. $waitMessage[ChannelID;User;timeout;timeoutErrMsg]
    """
    from CharmCord.utils.CharmCord import bots
    split = args.split(";")
    if len(split) < 3:
        raise SyntaxError("args, User, or timeout not provided to $waitMessage")
    try:
        channel_id = split[0]
        user = split[1]
        timeout = int(split[2])

        def check(msg):
            if int(channel_id) == msg.channel.id:
                if user == "everyone":
                    return True
                elif int(user) == msg.author.id:
                    return True

        error = None
        if len(split[3]) > 1:
            error = split[3]
        if error is None:
            try:
                message = await bots.wait_for("message", timeout=timeout, check=check)
                return message.content
            except asyncio.TimeoutError:
                return
        else:
            try:
                message = await bots.wait_for("message", timeout=timeout, check=check)
                return message.content
            except asyncio.TimeoutError:
                await context.channel.send(error)
    except ValueError:
        CharmCordErrors(f"args Error in {context.command.name}")
        return
