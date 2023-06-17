from CharmCord.all_functions import all_Funcs

for i in all_Funcs:
    try:
        # AGAIN, THIS IS EXTREMELY DANGEROUSSSSS!!!!!!!!!!!
        # THIS IS LIKE WRITING CODE THAT IS PUSHED TO PROD
        # WITH NO SQL INJECTION OR XSS PROTECTION!
        # Again please fix this
        # From your dearest, Noelle
        exec(f'from .{i.replace("$", "").strip()} import *')
    except ModuleNotFoundError:
        continue
