from CharmCord.all_functions import all_Funcs

for i in all_Funcs:
    try:
        exec(f'from .{i.replace("$", "").strip()} import *')  # nosec
    except ModuleNotFoundError:
        continue
