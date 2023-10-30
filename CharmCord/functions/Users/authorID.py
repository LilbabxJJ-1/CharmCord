import discord


async def authorID(emp, context):
    if isinstance(context, discord.Interaction):
        return context.user.id
    else:
        return context.author.id
