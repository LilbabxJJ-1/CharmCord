async def divide(args, context):
    if ";" in args:
        values = args.split(";")
        try:
            val1 = float(values[0])
            val2 = float(values[1])
            new = str(val1 / val2)
            if new.endswith(".0"):
                new = new.replace(".0", "")
            return new
        except ValueError:
            raise SyntaxError("$divide parameters can only can numbers")
        except IndexError:
            raise SyntaxError("$divide requires 2 parameters")
    else:
        raise SyntaxError("$divide requires 2 parameters")