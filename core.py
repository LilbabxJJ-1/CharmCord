import discord
from discord.ext import commands
from tools import findBracketPairs
global bots
global Context


class Start(discord.Client):
    global bots
    global Context

    def __init__(self, prefix: str, case_insensitive: bool = False, intents: tuple = ("default",), activity=None, help_command=None):
        global bots
        self.prefix = prefix
        self.case_insensitive = case_insensitive
        self.intented = intents
        self._help_command = help_command
        self._clients = ''
        self.intent = ''
        self._activity = activity
        if "all" in self.intented:
            self.intent = discord.Intents.all()
        elif "default" in self.intented:
            self.intent = discord.Intents.default()
        else:
            self.intent = discord.Intents.default()
        if "message" in self.intented:
            self.intent.message_content = True
        if "members" in self.intented:
            self.intent.members = True
        if "presences" in self.intented:
            self.intent.presences = True

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


class Commands:
    global bots
    global Context

    def command(self, Name, Code):
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
                                Code = str(Code).replace(f"$args[{look[start + 1:end]}]", args[int(look[start + 1:end]) - 1])
                                break
                            except IndexError:
                                raise SyntaxError(F"$args[{int(look[start + 1:end])}] Not Provided")
            await findBracketPairs(Code)


def Bot(prefix: str, case_insensitive: bool = False, intents: tuple = ("default",), activity=None, help_command=None):
    global bots
    _final = Start(prefix, case_insensitive, intents, activity, help_command)
    working = _final.clients
    return working
