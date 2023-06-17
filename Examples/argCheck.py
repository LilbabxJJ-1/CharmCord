from CharmCord import CharmClient

bot = CharmClient(prefix="!", case_insensitive=True, intents=("all",))


# argCheck should always go on top! Reads from top to bottom

# First slot is the amount of required arguments
# The second slot is the warning message that will send if too many or few args are given

bot.command(
    Name="Send",
    Code="""
    $argCheck[1;You need 1 arg!] 
    $sendMessage[1112301680839643156;Hiya, $username[$authorID[]] and $args[1]]""",
)
