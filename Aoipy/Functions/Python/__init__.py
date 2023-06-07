from Aoipy.all_functions import all_Funcs

for i in all_Funcs:
    try:
        exec(f'from .{i.replace("$", "").strip()} import *')
    except ModuleNotFoundError:
        continue