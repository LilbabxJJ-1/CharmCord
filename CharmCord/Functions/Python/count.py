from ast import literal_eval

async def count(code, Context):
    if isinstance(code, list):
        try:
            return len(code)
        except:
            return
    else:
        try:
            return len([i for i in code.split(" ") if len(i) > 0])
        except:
            return 0
