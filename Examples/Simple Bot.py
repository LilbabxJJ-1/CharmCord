from Aoipy import Bot, Commands, AoiEvents
bot = Bot(prefix="!", case_insensitive=True, intents=("all",))
commands = Commands().command
event = AoiEvents()

commands(
    Name='Send',
    Code="""
    $send[1112301680839643156;Hiya, $username[$authorID[]] and $args[1]]"""
)

commands(
    Name="Toast",
    Code="""
    $send[1112301680839643156; I AM TOAST!!]
    $pyeval[print('Hey')]"""
)


event.onReady(
    code="""$send[1112301680839643156; Bot is online!]"""
)


bot.run("************************")