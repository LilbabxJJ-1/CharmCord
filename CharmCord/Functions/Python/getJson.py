from CharmCord.CharmErrorHandling import CharmCordErrors
import aiohttp

async def getJson(args, context):
    """
    Ex. $getJson[url;keyValue]
    :param args:
    :param context:
    :return:
    """
    if ";" not in args:
        CharmCordErrors(f"Not enough args in $getJson: {context.command.name} command")
    vals =args.split(";")
    url = vals[0]
    key = vals[1]

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                try:
                    return data[key]
                except KeyError:
                    CharmCordErrors(f"Unknown key in $getJson: {context.command.name} command")