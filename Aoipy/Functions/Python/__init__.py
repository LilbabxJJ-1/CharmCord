from Aoipy.all_functions import funcs

for i in funcs:
    try:
        exec(f'from .{i.replace("$", "").strip()} import *')
    except ModuleNotFoundError:
        continue
