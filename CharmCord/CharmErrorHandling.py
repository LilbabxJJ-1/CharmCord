


class CharmErrorHandling:
    @staticmethod
    def Errors(self, error, code):
        """
        ERRORS:

        1: user     args
        2: channel  args
        3: category args

        4: WILDCARD
        """

        if error == 1:
            raise SyntaxError(f"args '{code}' is not a user args")
        if error == 2:
            raise SyntaxError(f"args '{code}' is not a channel args")
        if error == 3:
            raise SyntaxError(f"args '{code}' is not a category args")

        if error == 4:
            raise SyntaxError(code)


class CharmCordErrors(Exception):
    def __init__(self, error: str):
        raise SyntaxError(error)
