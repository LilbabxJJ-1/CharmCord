options = {
    "name": "",
    "id": "",
}


async def newChannel(option, context):
    return options[option.lower()]
