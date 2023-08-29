import discord


async def authorID(emp, Context):
    if isinstance(Context, discord.Interaction):
        return Context.user.id
    else:
        return Context.author.id
