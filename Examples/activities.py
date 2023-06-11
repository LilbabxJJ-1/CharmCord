from CharmCord import Bot, setActivity
act = setActivity(type="watching", message="All my servers")
bot = Bot(prefix="!", case_insensitive=True, intents=("all",), activity=act)



bot.run("******************************")