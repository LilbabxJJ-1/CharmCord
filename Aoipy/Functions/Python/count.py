async def count(code, Context):
    try:
        return len(eval(code))
    except:
        return len(code)