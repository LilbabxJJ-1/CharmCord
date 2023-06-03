class AoipyErrorHandling:

    def Errors(self, error, code):
        """
ERRORS:

1: user     ID
2: channel  ID
3: category ID

4: WILDCARD


        """



        if error == 1:
            raise SyntaxError(f"ID '{code}' is not a user ID")
        if error == 2:
            raise SyntaxError(f"ID '{code}' is not a channel ID")
        if error == 3:
            raise SyntaxError(f"ID '{code}' is not a category ID")

        if error == 4:
            raise SyntaxError(code)
