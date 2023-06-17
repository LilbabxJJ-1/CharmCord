from ast import literal_eval

async def If(args, context):
    from CharmCord.tools import safe_eval
    choices = ["==", ">=", "<=", "!=", "<", ">"]
    for i in choices:
        if i in args:
            if i in ["==", "!="]:
                vals = args.split(i)
                val1 = vals[0]
                val2 = vals[1]
            else:
                vals = args.split(i)
                val1 = int(vals[0])
                val2 = int(vals[1])
            test = safe_eval(f"{val1} {i} {val2}")
            if test:
                return True
            else:
                return False
    return False
