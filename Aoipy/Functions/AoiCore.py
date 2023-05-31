import discord
from discord.ext import commands
from Aoipy.tools import findBracketPairs, FunctionHandler
from Aoipy.Functions import *
import os

# Global variables
global bots
global Context
global TotalFuncs


class Start(discord.Client):
    # Global variables
    global bots
    global Context

    def __init__(self, prefix: str, case_insensitive: bool = False, intents: tuple = ("default",), activity=None, help_command=None):
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
        super().__init__(intents=self.intent)

    @property
    def clients(self):
        return self._clients

    ########################################
    #              COMMANDS                #
    ########################################


class Commands:
    # Global variables
    global bots
    global Context

    def command(self, Name, Code):
        # Define command function dynamically

        @bots.command(name=Name)
        async def go(ctx, *args, Code=Code):
            global Context
            Context = ctx
            if '$args' in Code:
                while "$args" in str(Code):
                    count = 0
                    end = None
                    balance = 0
                    start = Code.index("$args") + 5
                    look = Code[start:len(Code)]
                    for i in look:
                        if i == "[":
                            start = count
                            count += 1
                            balance += 1
                            continue
                        if i == "]":
                            end = count
                            balance -= 1
                        count += 1
                        if balance == 0 and start is not None and end is not None:
                            try:
                                # Replace $args with arguments
                                Code = str(Code).replace(f"$args[{look[start + 1:end]}]", args[int(look[start + 1:end]) - 1])
                                break
                            except IndexError:
                                raise SyntaxError(F"$args[{int(look[start + 1:end])}] Not Provided")

            if "$argCheck" in Code:
                if Code.count("$argCheck") > 1:
                    raise Exception("Too many $argCheck in a single command | Max is 1!")
                start = Code.index("$argCheck[") + 10
                area = Code[start:]
                try:
                    argTotal = area[:area.index(";")]
                    warning = area[area.index(";") + 1:area.index("]")]
                    if len(args) != int(argTotal):
                        await Context.channel.send(warning)
                        return
                    Code = Code.replace(f"$argCheck[{argTotal}{area[area.index(';'):area.index(']')]}]\n", "")
                except:
                    raise SyntaxError("Not enough arguments in $argCheck!")

            await findBracketPairs(Code, TotalFuncs, Context)

    ########################################
    #              EVENTS                  #
    ########################################


class AoiEvents:
    def onReady(self, code):
        # Define on_ready event function
        @bots.event
        async def on_ready():
            await findBracketPairs(code, TotalFuncs, None)


def Bot(prefix: str, case_insensitive: bool = False, intents: tuple = ("default",), activity=None, help_command=None):
    # Global variables
    global bots
    global TotalFuncs

    # Initialize FunctionHandler and register functions
    Functions = FunctionHandler()
    TotalFuncs = Functions
    Functions.register_functions()

    # Create Start instance and return working bot
    _final = Start(prefix, case_insensitive, intents, activity, help_command)
    working = _final.clients
    return working
