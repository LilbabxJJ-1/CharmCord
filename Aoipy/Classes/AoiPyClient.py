import discord
from discord.ext import commands
from Aoipy.tools import FunctionHandler
from .CommandHandler import load_commands
import asyncio
global TotalFuncs
global bots


class Aoipy(discord.Client):
    # Global variables
    global bots

    def __init__(self, prefix, case_insensitive, intents: tuple, activity, help_command, load_command_dir):
        # Global variables
        global bots

        # Initialize Start class
        self.prefix = prefix
        self.case_insensitive = case_insensitive
        self.intented = intents
        self._help_command = help_command
        self._clients = ''
        self.intent = ''
        self._activity = activity

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
        super().__init__(intents=self.intent)

    @property
    def clients(self):
        return self._clients


def AoipyClient(prefix: str, case_insensitive: bool = False, intents: tuple = ("default",), activity=None, help_command=None, load_command_dir = "commands"):
    # Global variables
    global bots
    global TotalFuncs

    # Initialize FunctionHandler and register functions
    Functions = FunctionHandler()
    TotalFuncs = Functions
    Functions.register_functions()

    # Create Start instance and return working bot
    _final = Aoipy(prefix, case_insensitive, intents, activity, help_command, load_command_dir)
    working = _final.clients
    return working
