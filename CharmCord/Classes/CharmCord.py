import json
import discord
from discord.ext import commands
from CharmCord.tools import FunctionHandler, findBracketPairs, noArguments
from CharmCord.Functions.Events.deletedChannel import options
from CharmCord.Functions.Events.oldChannel import options as old
from .CommandHandler import load_commands
from .SlashCommands import SlashCommands
from .Commands import Commands

# Global Calls
TotalFuncs = None
bots = None
all_vars = None


class CharmCord:

    def __init__(
            self,
            prefix,
            case_insensitive,
            intents,
            activity,
            load_command_dir,
    ):
        # Global variables
        global bots

        # Initialize Start class
        self.prefix = prefix
        self.case_insensitive = case_insensitive
        self.intented = intents
        self._help_command = None
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

        try:
            with open("variables.json", "r") as var:
                pass
        except FileNotFoundError:
            with open("variables.json", "w") as var:
                go = {"STRD": True}
                json.dump(go, var)

    def run(self, token: str):
        bots.run(token)

    def variables(self, variables: dict):
        global all_vars
        for key, value in variables.items():
            self.all_variables[key] = value
        all_vars = self.all_variables

    def slash_command(self, name: str, code: str, args: list = [], description: str = "") -> None:
        sl = SlashCommands().slash_command
        sl(name=name, code=code, args=args, description=description.lower(), bot=bots)

    def command(self, name: str, code: str, aliases: list = None):
        co = Commands().command
        if aliases is None:
            co(name=name, code=code, bot=bots)
        else:
            co(name=name, code=code, aliases=aliases, bot=bots)

    def on_channel_updated(self, code):
        @bots.event
        async def on_guild_channel_update(before, after):
            for i in old.keys():
                old[i] = before.i
            if code is not None:
                await findBracketPairs(code, TotalFuncs, None)

    def on_channel_deleted(self, code=None):
        @bots.event
        async def on_guild_channel_delete(channel):
            options["name"] = channel.name
            options["id"] = channel.id
            # more options coming
            if code is not None:
                await findBracketPairs(code, TotalFuncs, None)

    def on_ready(self, code):
        @bots.event
        async def on_ready():
            from CharmCord.CharmErrorHandling import CharmCordErrors
            finalCode = await noArguments(code, TotalFuncs, None)
            await findBracketPairs(finalCode, TotalFuncs, None)
            try:
                await bots.tree.sync()
            except Exception:
                CharmCordErrors("All slash commands need a description")


def CharmClient(
        prefix: str,
        case_insensitive: bool = False,
        intents: tuple = ("default",),
        activity=None,
        load_command_dir="commands",
):
    """
    CharmCord Discord Client
    """
    # Global variables
    global bots
    global TotalFuncs

    # Initialize FunctionHandler and register functions
    functions = FunctionHandler()
    TotalFuncs = functions
    functions.register_functions()

    # Create Start instance and return working bot
    _final = CharmCord(
        prefix,
        case_insensitive,
        intents,
        activity,
        load_command_dir
    )
    return _final
