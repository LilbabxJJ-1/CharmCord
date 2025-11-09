import discord
from discord import app_commands

class SlashCommands:

    @staticmethod
    def interaction_command(name, code, args=None, description=None, bot=None):
        from CharmCord.globeHandler import get_globals
        from CharmCord.tools import no_arguments, slash_args, find_bracket_pairs, lets

        # If no args, simple handler
        if not args:
            @bot.tree.command(name=name, description=description or "No description.")
            async def go(interaction: discord.Interaction):
                funcs = get_globals()[0]
                context = interaction
                final_code = await no_arguments(code, funcs, context)
                await find_bracket_pairs(final_code, funcs, context)
                if lets:
                    lets.clear()
            return

        # If args exist, build a new command dynamically
        # Start with a dict of supported types
        type_map = {1: str, 2: int}

        # Dynamically create parameters
        annotations = {"interaction": discord.Interaction}
        defaults = {}

        for a in args:
            arg_type = type_map[a["type"]]
            annotations[a["name"]] = arg_type
            defaults[a["name"]] = ...  # required parameter

        # Define the function
        async def go(interaction: discord.Interaction, **kwargs):
            funcs = get_globals()[0]
            context = interaction

            final_code = await no_arguments(code, funcs, context)
            final_code = slash_args(list(kwargs.values()), final_code)
            await find_bracket_pairs(final_code, funcs, context)
            if lets:
                lets.clear()

        # Apply annotations
        go.__annotations__ = annotations
        go.__doc__ = description or "No description."

        # Register with tree
        bot.tree.command(name=name, description=description or "No description.")(go)
