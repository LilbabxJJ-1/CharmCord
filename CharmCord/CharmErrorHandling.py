from colorama import Fore, Style


class CharmErrorHandling:
    pass


class CharmCordErrorHandling:
    def __init__(self, error_msg: str, code_sample: str, command_name: str = None):
        self.error = error_msg
        self.command = command_name
        self.code = code_sample

    def command_error(self):
        print(Fore.RED + f"[CHARMCORD ERR] Error: {self.error} --> Command '{self.command}' "
                         f"--> '{self.code}'\n")
        print(Style.RESET_ALL)

    def internal_error(self):
        print(Fore.RED + f"[CHARMCORD ERR] Error: {self.error} --> '{self.code}'\n")
        print(Style.RESET_ALL)


def deprecated(reason: str):
    print(Fore.RED + reason)
    return


class CharmCordErrors(Exception):
    def __init__(self, error: str):
        raise SyntaxError(error)
