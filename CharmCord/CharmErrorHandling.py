from colorama import Fore


class CharmErrorHandling:
    pass


def deprecated(reason: str):
    print(Fore.RED + reason)
    return


class CharmCordErrors(Exception):
    def __init__(self, error: str):
        raise SyntaxError(error)
