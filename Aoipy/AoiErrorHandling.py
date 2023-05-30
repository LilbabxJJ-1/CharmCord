class AoipyErrorHandling:

    def Errors(self, error, code):
        if error == 1:
            raise SyntaxError(f"ID '{code}' is not a user ID")
        if error == 2:
            raise SyntaxError(f"ID '{code}' is not a channel ID")

        if error == 4:
            raise SyntaxError(code)
