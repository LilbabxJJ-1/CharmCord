async def sum(args, context):
    if ";" in args:
        values = args.split(";")
        try:
            val1 = float(values[0])
            val2 = float(values[1])
            new = str(val2 + val1)
            if new.endswith(".0"):
                new = new.replace(".0", "")
            return new
        except ValueError:
            raise SyntaxError("$sum parameters can only can numbers")
        except IndexError:
            raise SyntaxError("$sum requires 2 parameters")
    else:
        raise SyntaxError("$sum requires 2 parameters")
