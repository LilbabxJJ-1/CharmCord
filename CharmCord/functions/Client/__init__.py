import os

current_directory = os.path.dirname(__file__)
files = os.listdir(current_directory)
python_files = [file for file in files if file.endswith('.py') and "_" not in file]
for file in python_files:
    try:
        module_name = file[:-3]  # Remove the '.py' extension
        exec(f'from .{module_name} import {module_name}')  # nosec
    except ModuleNotFoundError:
        continue

