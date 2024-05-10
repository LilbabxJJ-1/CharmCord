async def contains(args: str, context):
    data = args.split(';')
    text = data[0]
    del data[0]
    if text in data:
        return True
    return False
