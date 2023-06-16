from CharmCord import CharmClient
bot = CharmClient(prefix="!", case_insensitive=True, intents=("all",))

bot.commands(
    Name='Send',
    Code="""
    $sendMessage[$channelID;Hiya, $username[$authorID] and $args[1]]"""
)

bot.commands(
    Name="Toast",
    Code="""
    $sendMessage[1112301680839643156; I AM TOAST!!]
    $pyeval[print('Hey')]"""
)


bot.onReady(
    code="""$console[$botName is online!]"""
)


bot.run("************************")