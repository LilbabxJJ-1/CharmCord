from CharmCord import CharmClient

bot = CharmClient(prefix="!", case_insensitive=True, intents=("all",))

bot.command(
    name="Hey",
    code="""
    $argCheck[1;You need at least 1 argument!]
    $sendMessage[$channelID;Hiya, $username[$authorID] and $args[1]]
    """,
)

bot.slashCommand(
    name="toast",
    code="""
    $sendMessage[1112301680839643156; I AM TOAST!!]
    $console[Hiya]
    """,
    description="Toast command"
)


bot.onReady(
    code="$console[$botName is online!]"
)


bot.run("TOKEN HERE")
