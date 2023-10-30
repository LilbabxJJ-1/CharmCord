async def hasPerm(args, context):
    vals = args.split(";")
    user = vals[0].replace("<@", "").replace(">", "")
    perm = vals[1].lower()
    guild = await context.guild.fetch_member(int(user))
    perms = [i for i in guild.guild_permissions]
    for i in perms:
        if perm in i:
            return True
    else:
        return False
