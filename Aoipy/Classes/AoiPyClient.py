import discord
from discord.ext import commands
from Aoipy.tools import FunctionHandler
from .CommandHandler import load_commands
import asyncio

global TotalFuncs
global bots
global all_commands


class Aoipy:
    # Global variables
    global bots
    global all_commands

    def __init__(self, prefix, case_insensitive, intents: tuple, activity, help_command, load_command_dir):
        # Global variables
        global bots
        global all_commands

        # Initialize Start class
        self.prefix = prefix
        self.case_insensitive = case_insensitive
        self.intented = intents
        self._help_command = help_command
        self._clients = ''
        self.intent = ''
        self._activity = activity
        all_commands = {}

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
            self._clients = commands.Bot(command_prefix=self.prefix, case_insensitive=self.case_insensitive, intents=self.intent,
                                         help_command=self._help_command)
            bots = self._clients

        else:
            self._clients = commands.Bot(command_prefix=self.prefix, case_insensitive=self.case_insensitive, intents=self.intent,
                                         activity=self._activity,
                                         help_command=self._help_command)
            bots = self._clients
        try:
            load_commands(load_command_dir)
        except FileNotFoundError:
            pass
        # super().__init__(intents=self.intent)

    def run(self, token: str):
        bots.run(token)

    def command(self, Name, Code, Aliases=[]):
        from .Commands import Commands
        co = Commands().command
        co(
            Name=Name,
            Code=Code,
            Aliases=Aliases
        )


    def onChannelUpdated(self, Code):
        @bots.event
        async def on_guild_channel_update(before, after):
            from Aoipy.Functions.Events.oldChannel import options as old
            from Aoipy.Functions.Events.newChannel import options as new
            for i in old.keys():
                old[i] = eval(f"before.{i}")

            if Code is not None:
                from Aoipy.tools import findBracketPairs
                await findBracketPairs(Code, TotalFuncs, None)

    def onChannelDeleted(self, Code=None):
        @bots.event
        async def on_guild_channel_delete(channel):
            from Aoipy.Functions.Events.deletedChannel import options
            options["name"] = channel.name
            options['id'] = channel.id
            # more options coming
            if Code is not None:
                from Aoipy.tools import findBracketPairs
                await findBracketPairs(Code, TotalFuncs, None)

    def onReady(self, Code):
        @bots.event
        async def on_ready():
            from Aoipy.tools import findBracketPairs
            await findBracketPairs(Code, TotalFuncs, None)


def AoipyClient(prefix: str, case_insensitive: bool = False, intents: tuple = ("default",), activity=None, help_command=None,
                load_command_dir="commands"):
    # Global variables
    global bots
    global TotalFuncs
    global all_commands

    # Initialize FunctionHandler and register functions
    Functions = FunctionHandler()
    TotalFuncs = Functions
    Functions.register_functions()

    # Create Start instance and return working bot
    _final = Aoipy(prefix, case_insensitive, intents, activity, help_command, load_command_dir)
    working = _final
    return working
