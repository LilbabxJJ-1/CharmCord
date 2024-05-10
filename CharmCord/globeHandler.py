
TotalFuncs = None
bots = None
all_vars = None
lets = {}

def update_globals(key: str, value):
    global TotalFuncs
    global bots
    global all_vars
    global lets
    global activity
    if key.lower().startswith("t"):
        TotalFuncs = value
    elif key.lower().startswith("b"):
        bots = value
    elif key.lower().startswith("l"):
        lets = value
    elif key.lower().startswith("a"):
        activity = value
    else:
        all_vars = value


def get_globals():
    return [TotalFuncs, bots, all_vars, lets]
