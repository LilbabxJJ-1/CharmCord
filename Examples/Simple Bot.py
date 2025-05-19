from CharmCord import charmclient

bot = charmclient(prefix="!", case_insensitive=True, intents='all')

bot.on_ready(
    code="$console[$botName is online!]"
)

bot.command(
    name="Ping",
    code="""
    $sendMessage[$channelID;Pong!! $ping]
    """,
)

bot.run("TOKEN HERE")
