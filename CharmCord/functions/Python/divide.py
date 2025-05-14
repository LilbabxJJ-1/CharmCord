from CharmCord.CharmErrorHandling import CharmCordError


async def divide(args, context):
    """
    Use. $divide[digit1;digit2]
    Ex. $divide[10;5]

    :param args:
    :param context:
    :return:
    """
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
            CharmCordError("$divide parameters can only be numbers",
                                   f"{args}",
                                   context.command.name).command_error()
        except IndexError:
            raise SyntaxError("$divide requires 2 parameters")
    else:
        raise SyntaxError("$divide requires 2 parameters")
