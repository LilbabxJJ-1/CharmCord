import discord


async def authorName(emp, Context):
    if isinstance(Context, discord.Interaction):
        return Context.user.name
    else:
        return Context.author.name