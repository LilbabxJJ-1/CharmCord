import discord


async def authorName(emp, context):
    if isinstance(context, discord.Interaction):
        return context.user.name
    else:
        return context.author.name
