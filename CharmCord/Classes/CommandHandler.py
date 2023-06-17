import os


def load_commands(dir):
    for filename in os.listdir(dir):
        if filename.endswith(".py"):
            exec(f"from {dir.replace('/', '.')}.{filename[:-3]} import *")
        elif os.path.isdir(f"{dir}/{filename}") and not filename.endswith("__"):
            load_commands(f"{dir}/{filename}")
