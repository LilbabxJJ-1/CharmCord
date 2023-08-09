import asyncio

import discord
from discord.ext import commands
from CharmCord.tools import FunctionHandler
from .CommandHandler import load_commands

global TotalFuncs
global bots
global all_vars


class CharmCord:
    # Global variables
    global bots
    global all_vars

    def __init__(
            self,
            prefix,
            case_insensitive,
            intents: tuple,
            activity,
            help_command,
            load_command_dir,
    ):
        # Global variables
        global bots

        # Initialize Start class
        self.prefix = prefix
        self.case_insensitive = case_insensitive
        self.intented = intents
        self._help_command = help_command
        self._clients = ""
        self.intent = ""
        self._activity = activity
        self.all_variables = {}

        # Determine intents
        if "all" in self.intented:
            self.intent = discord.Intents.all()
        elif "default" in self.intented:
            self.intent = discord.Intents.default()
        else:
            self.intent = discord.Intents.default()

        # Enable specific intents
        if "message" in self.intented:
            self.intent.message_content = True
        if "members" in self.intented:
            self.intent.members = True
        if "presences" in self.intented:
            self.intent.presences = True

        # Create bot instances
        if self._activity is None:
            self._clients = commands.Bot(
                command_prefix=self.prefix,
                case_insensitive=self.case_insensitive,
                intents=self.intent,
                help_command=self._help_command,
            )
            bots = self._clients

        else:
            self._clients = commands.Bot(
                command_prefix=self.prefix,
                case_insensitive=self.case_insensitive,
                intents=self.intent,
                activity=self._activity,
                help_command=self._help_command,
            )
            bots = self._clients

        try:
            load_commands(load_command_dir)
        except FileNotFoundError:
            pass

        import json

        try:
            with open("variables.json", "r") as var:
                pass
        except FileNotFoundError:
            with open("variables.json", "w") as var:
                go = {"STRD": True}
                json.dump(go, var)


    def run(self, token: str):
        bots.run(token)

    def variables(self, vars: dict):
        global all_vars
        for key, value in vars.items():
            self.all_variables[key] = value
        all_vars = self.all_variables

    def slashCommand(self, name: str, code: str, args: list = [], description: str = ""):
        from .SlashCommands import SlashCommands

        sl = SlashCommands().slashCommand
        sl(name=name, code=code, args=args, description=description.lower())

    def command(self, Name: str, Code: str, Aliases=[]):
        from .Commands import Commands

        co = Commands().command
        co(Name=Name, Code=Code, Aliases=Aliases)

    def onChannelUpdated(self, Code):
        @bots.event
        async def on_guild_channel_update(before, after):
            from CharmCord.Functions.Events.oldChannel import options as old

            for i in old.keys():
                old[i] = before.i

            if Code is not None:
                from CharmCord.tools import findBracketPairs

                await findBracketPairs(Code, TotalFuncs, None)

    def onChannelDeleted(self, Code=None):
        @bots.event
        async def on_guild_channel_delete(channel):
            from CharmCord.Functions.Events.deletedChannel import options

            options["name"] = channel.name
            options["id"] = channel.id
            # more options coming
            if Code is not None:
                from CharmCord.tools import findBracketPairs

                await findBracketPairs(Code, TotalFuncs, None)

    def onReady(self, Code):
        @bots.event
        async def on_ready():
            from CharmCord.tools import findBracketPairs, noArguments
            from CharmCord.CharmErrorHandling import CharmCord_Errors
            finalCode = await noArguments(Code, TotalFuncs, None)
            await findBracketPairs(finalCode, TotalFuncs, None)
            c = 1
            try:
                await bots.tree.sync()
            except:
                CharmCord_Errors("All slash commands need a description")
def CharmClient(
        prefix: str,
        case_insensitive: bool = False,
        intents: tuple = ("default",),
        activity=None,
        help_command=None,
        load_command_dir="commands",
):
    """
    CharmCord Discord Client
    """
    # Global variables
    global bots
    global TotalFuncs

    # Initialize FunctionHandler and register functions
    Functions = FunctionHandler()
    TotalFuncs = Functions
    Functions.register_functions()

    # Create Start instance and return working bot
    _final = CharmCord(
        prefix, case_insensitive, intents, activity, help_command, load_command_dir
    )
    working = _final
    return working
