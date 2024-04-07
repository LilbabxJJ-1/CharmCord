import json
import discord
from CharmCord.all_functions import title
from discord.ext import commands
from CharmCord.functions.Events._options_ import options
from CharmCord.functions.Messages._btnOpts_ import interactions
from CharmCord.tools import FunctionHandler, findBracketPairs, noArguments
from .CommandHandler import load_commands
from .Commands import Commands
from .SlashCommands import SlashCommands
from ..globeHandler import update_globals, get_globals

global bots


class CharmCord:

    def __init__(
            self,
            prefix,
            case_insensitive,
            intents,
            activity,
            load_command_dir,
    ):
        """
        This function initializes a bot with specified prefix, case sensitivity, intents, activity, and loads command files.
        It determines intents based on user input and creates bot instances with the specified parameters.
        Additionally, it loads command files and sets up a JSON file for storing variables if it doesn't exist.
        :param prefix:
        :param case_insensitive:
        :param intents:
        :param activity:
        :param load_command_dir:
        """
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
        update_globals("bots", self.bot)

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
        print(title)


    @staticmethod
    def run(token: str):
        bots.run(token)

    def variables(self, variables: dict):
        for key, value in variables.items():
            self.all_variables[key] = value
        all_vars = self.all_variables
        update_globals("all", all_vars)

    @staticmethod
    def interaction_code(id_name, code):
        if id_name in interactions:
            raise Exception(f"Multiple interactions with '{id_name}' ID found! Please make sure all IDs are unique")
        interactions[id_name] = code
        return

    @staticmethod
    def slash_command(name: str, code: str, args: list[dict] = None, description: str = "") -> None:
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

    def on_reaction_add(self, code=None):
        @self.bot.event
        async def on_reaction_add(reaction: discord.Reaction, user: discord.User):
            try:
                options["reactionAdded"]["name"] = reaction.emoji.name
                options["reactionAdded"]["id"] = reaction.emoji.id
            except AttributeError:
                options["reactionAdded"]["name"] = reaction.emoji  # May Remove
                options["reactionAdded"]["id"] = 0
            options["reactionAdded"]["bot_reacted"] = reaction.me
            options["reactionAdded"]["users_reacted"] = [user async for user in reaction.users()]
            options["reactionAdded"]["count"] = reaction.count
            options["reactionAdded"]["username"] = user.name
            options["reactionAdded"]["userid"] = user.id
            options["reactionAdded"]["msgid"] = reaction.message.id
            options["reactionAdded"]["msgauthorid"] = reaction.message.author.id
            options["reactionAdded"]["msgauthorname"] = reaction.message.author.name

            if code is not None:
                final_code = await noArguments(code, TotalFuncs, None)
                await findBracketPairs(final_code, TotalFuncs, None)
            return

    def on_reaction_remove(self, code=None):
        @self.bot.event
        async def on_reaction_remove(reaction: discord.Reaction, user: discord.User):
            try:
                options["reactionRemoved"]["name"] = reaction.emoji.name
                options["reactionRemoved"]["id"] = reaction.emoji.id
            except AttributeError:
                options["reactionRemoved"]["name"] = reaction.emoji  # May Remove
                options["reactionRemoved"]["id"] = 0
            options["reactionRemoved"]["bot_reacted"] = reaction.me
            options["reactionRemoved"]["users_reacted"] = [user async for user in reaction.users()]
            options["reactionRemoved"]["count"] = reaction.count
            options["reactionRemoved"]["username"] = user.name
            options["reactionRemoved"]["userid"] = user.id
            options["reactionRemoved"]["msgid"] = reaction.message.id
            options["reactionRemoved"]["msgauthorid"] = reaction.message.author.id
            options["reactionRemoved"]["msgauthorname"] = reaction.message.author.name

            if code is not None:
                final_code = await noArguments(code, TotalFuncs, None)
                await findBracketPairs(final_code, TotalFuncs, None)
            return

    def on_message(self, code=None):
        @self.bot.event
        async def on_message(msg: discord.Message):
            pass  # For now

    def on_member_join(self, code=None):
        @self.bot.event
        async def on_member_join(member: discord.Member):
            options["memberJoined"]["id"] = member.id
            options["memberJoined"]["guildid"] = member.guild.id

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
    update_globals("total", functions)
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
