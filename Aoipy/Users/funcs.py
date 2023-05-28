async def username(user):
    from Aoipy.core import bots
    try:
        int(user)
        new_user = await bots.fetch_user(user)
    except:
        raise Exception(f"{user} isn't an ID")
    return new_user

async def authorName(emp):
    from Aoipy.core import Context
    return Context.author.name

async def authorID(emp):
    from Aoipy.core import Context
    return Context.author.id


async def send(args: str):
    from Aoipy.core import bots
    split = args.split(";")
    channel_id = split[0]
    message = split[1]
    channel = await bots.fetch_channel(int(channel_id))
    await channel.send(message)
    return


async def pyeval(code):
    answer = eval(code)
    return answer