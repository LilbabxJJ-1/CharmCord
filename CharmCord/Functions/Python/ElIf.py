async def ElIf(args, context):
    choices = ["==", ">=", "<=", "!=", "<", ">"]
    operator_mapping = {
        "==": lambda x, y: x == y,
        "!=": lambda x, y: x != y,
        ">": lambda x, y: x > y,
        ">=": lambda x, y: x >= y,
        "<": lambda x, y: x < y,
        "<=": lambda x, y: x <= y,
    }
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
            if result:
                return True
            else:
                return False
    return False
