import os


def load_commands(directory: str):
    for filename in os.listdir(directory):
        if filename.endswith(".py"):
            exec(f"from {directory.replace('/', '.')}.{filename[:-3]} import *")
        elif os.path.isdir(f"{directory}/{filename}") and not filename.endswith("__"):
            load_commands(f"{directory}/{filename}")
