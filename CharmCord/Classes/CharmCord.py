import json
import discord
from discord.ext import commands
from CharmCord.tools import FunctionHandler, findBracketPairs, noArguments
# from CharmCord.Functions.Events.deletedChannel import options
# from CharmCord.Functions.Events.oldChannel import options as old
from CharmCord.Functions.Events.options import options
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
        self.bot = None

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
        bots, self.bot = self._clients, self._clients

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

    @staticmethod
    def run(token: str):
        bots.run(token)

    def variables(self, variables: dict):
        global all_vars
        for key, value in variables.items():
            self.all_variables[key] = value
        all_vars = self.all_variables

    @staticmethod
    def slash_command(name: str, code: str, args: list[dict] = [{}], description: str = "") -> None:
        sl = SlashCommands().slash_command
        sl(name=name, code=code, args=args, description=description.lower(), bot=bots)

    @staticmethod
    def command(name: str, code: str, aliases: list = None):
        co = Commands().command
        if aliases is None:
            co(name=name, code=code, bot=bots)
        else:
            co(name=name, code=code, aliases=aliases, bot=bots)

    # EVENTS BELOW

    def on_member_join(self, code=None):
        @self.bot.event
        async def on_member_join(member):
            options["memberJoined"]["id"] = member.id

            if code is not None:
                final_code = await noArguments(code, TotalFuncs, None)
                await findBracketPairs(final_code, TotalFuncs, None)
            return

    def on_channel_updated(self, code=None):
        @self.bot.event
        async def on_guild_channel_update(before, after):
            for i in options["oldChannel"].keys():
                options["oldChannel"][i] = before.i
            for i in options["newChannel"].keys():
                options["newChannel"][i] = after.i
            if code is not None:
                final_code = await noArguments(code, TotalFuncs, None)
                await findBracketPairs(final_code, TotalFuncs, None)

    def on_channel_deleted(self, code=None):
        @self.bot.event
        async def on_guild_channel_delete(channel):
            options["deletedChannel"]["name"] = channel.name
            options["deletedChannel"]["id"] = channel.id
            options["deletedChannel"]["type"] = channel.type
            options["deletedChannel"]["category"] = channel.category
            options["deletedChannel"]["categoryid"] = channel.category_id
            options["deletedChannel"]["guild"] = channel.guild
            options["deletedChannel"]["nsfw"] = channel.nsfw
            options["deletedChannel"]["delay"] = channel.slowmode_delay
            options["deletedChannel"]["created"] = channel.created_at
            # more options coming
            if code is not None:
                final_code = await noArguments(code, TotalFuncs, None)
                await findBracketPairs(final_code, TotalFuncs, None)

    def on_ready(self, code):
        @self.bot.event
        async def on_ready():
            from CharmCord.CharmErrorHandling import CharmCordErrors
            final_code = await noArguments(code, TotalFuncs, None)
            await findBracketPairs(final_code, TotalFuncs, None)
            try:
                await self.bot.tree.sync()
            except Exception as e:
                print(e)
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
