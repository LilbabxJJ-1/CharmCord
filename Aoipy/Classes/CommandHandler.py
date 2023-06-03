import os


def load_commands(dir):
    for filename in os.listdir(dir):
        if filename.endswith('.py'):
            exec(f"from {dir}.{filename[:-3]} import *")
