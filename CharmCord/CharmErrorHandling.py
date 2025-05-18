from colorama import Fore, Style

class CharmCordError(Exception):
    def __init__(self, error_msg: str, code_sample: str, command_name: str = None):
        self.error = error_msg
        self.command = command_name
        self.code = code_sample
        super().__init__(self.__str__())

    def command_error(self):
        return (Fore.RED +
                f"[CHARMCORD COMMAND ERR]: {self.error} --> Command '{self.command}' "
                f"--> '{self.code}'\n" +
                Style.RESET_ALL)

    def internal_error(self):
        return (Fore.RED +
                f"[CHARMCORD INTERNAL ERR]: {self.error} --> '{self.code}'\n" +
                Style.RESET_ALL)

    def __str__(self):
        if self.command:
            return self.command_error()
        return self.internal_error()


def deprecated(reason: str):
    print(Fore.RED + reason)
    return

def CharmCordErrors(ss):
    pass