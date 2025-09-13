from CharmCord import charmclient, set_activity

act = set_activity(typing="watching", message="All my servers")
bot = charmclient(prefix="!", case_insensitive=True, intents=["all"], activity=act)

# Bot code here...


bot.run("******************************")
