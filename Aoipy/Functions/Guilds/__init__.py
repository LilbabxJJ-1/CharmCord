with open("Aoipy/all_Functions.txt") as funcs:
    alls = funcs.readlines()
    for i in alls:
        try:
            exec(f'from .{i.replace("$", "").strip()} import *')
        except ModuleNotFoundError:
            continue
