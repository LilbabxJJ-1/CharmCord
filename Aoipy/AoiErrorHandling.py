class AoipyErrorHandling:

    def Errors(self, error, code):
        if error == 1:
            raise SyntaxError(f"ID {code} is not a user ID")