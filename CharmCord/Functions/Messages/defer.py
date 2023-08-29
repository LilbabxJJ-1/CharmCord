import discord
from CharmCord.CharmErrorHandling import CharmCordErrors


async def defer(emp, context):
    if isinstance(context, discord.Interaction):
       await context.response.defer()
       return
    else:
        CharmCordErrors(f"$defer: Defer cannot be used outside slash commands\nCommand: {context.command.name}")