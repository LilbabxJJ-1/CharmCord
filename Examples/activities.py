from CharmCord import CharmClient, setActivity

act = setActivity(typing="watching", message="All my servers")
bot = CharmClient(prefix="!", case_insensitive=True, intents=("all",), activity=act)

# Bot code here...


bot.run("******************************")
