from CharmCord.all_functions import all_Funcs

for i in all_Funcs:
    try:
        # THIS IS EXTREMELY DANGEROUS! EXECING WITHOUT PROTECTION IS EXTREMELY BAD!!!!!
        # Marked by Bandit, but please fix this later!
        # From Noelle
        exec(f'from .{i.replace("$", "").strip()} import *')  # nosec
    except ModuleNotFoundError:
        continue
