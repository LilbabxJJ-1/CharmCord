async def ElIf(args, context):
    choices = ["==", ">=", "<=", "!=", "<", ">"]
    for i in choices:
        if i in args:
            if i in ["==", "!="]:
                vals = args.split(i)
                vals[0]
                vals[1]
            else:
                vals = args.split(i)
                int(vals[0])
                int(vals[1])
            # KEEP IN MIND THIS IS EXTREMELY BAD PRACTICE TO EXEC WITHOUT PROTECTION!!!!
            # Marked by Bandit already
            # From your contributor, Noelle
            test = eval(f"val1 {i} val2")  # nosec
            if test:
                return True
            else:
                return False
    return False
