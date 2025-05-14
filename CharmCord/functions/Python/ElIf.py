async def ElIf(args, context):
    """
    Use. $elif[expression]



    :param args:
    :param context:
    :return:
    """
    # todo: Come back to finish making sure operators do the order of operation correctly
    choices = ["==", ">=", "<=", "!=", "<", ">"]
    ands = []
    ors = []
    operator_mapping = {
        "==": lambda x, y: x == y,
        "!=": lambda x, y: x != y,
        ">": lambda x, y: x > y,
        ">=": lambda x, y: x >= y,
        "<": lambda x, y: x < y,
        "<=": lambda x, y: x <= y,
    }
    if "&" in args:
        compare = args.split("&")
        for count, exp in enumerate(compare):
            if "|" in exp:
                continue
            for operator in choices:
                if operator in exp:
                    if operator in ["==", "!="]:
                        vals = exp.split(operator)
                        val1 = vals[0].strip()
                        val2 = vals[1].strip()
                    else:
                        vals = args.split(operator)
                        val1 = int(vals[0])
                        val2 = int(vals[1])
                    ands.append(operator_mapping.get(operator, lambda x, y: None)(val1, val2))

    if "|" in args:
        compare = args.split("|")
        for count, exp in enumerate(compare):
            if "&" in exp:
                continue
            for operator in choices:
                if operator in exp:
                    if operator in ["==", "!="]:
                        vals = exp.split(operator)
                        val1 = vals[0].strip()
                        val2 = vals[1].strip()
                    else:
                        vals = args.split(operator)
                        val1 = int(vals[0])
                        val2 = int(vals[1])
                    ors.append(operator_mapping.get(operator, lambda x, y: None)(val1, val2))

    if ands and ors:
        return any(ors) and all(ands)
    elif ands:
        return all(ands)
    elif ors:
        return any(ors)
    else:
        pass

    for i in choices:
        if i in args:
            if i in ["==", "!="]:
                vals = args.split(i)
                val1 = vals[0].strip()
                val2 = vals[1].strip()
            else:
                vals = args.split(i)
                val1 = int(vals[0])
                val2 = int(vals[1])
            result = operator_mapping.get(i, lambda x, y: None)(val1, val2)
            return result

    return False
