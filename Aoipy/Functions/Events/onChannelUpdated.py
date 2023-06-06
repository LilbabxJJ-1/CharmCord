options = {
    'before': {
        'name': '',
    },
    'after': {
        'name': '',
    },
    'id': ''
}


async def onChannelUpdated(option, context):
    if option.lower().strip() == "id":
        return options['id']
    try:
        option, option2 = tuple(option.split())
    except ValueError:
        return "ERROR"
    else:
        try:
            return options[option.lower().strip()][option2.lower().strip()]
        except ValueError:
            return "ERROR2"