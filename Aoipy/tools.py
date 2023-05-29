from Aoipy.Functions.Users.funcs import *

funcs = {"$username": username, "$authorid": authorID, "$send": send, "$pyeval": pyeval}


async def findBracketPairs(entry: str):
    lines = [line.strip() for line in entry.split("\n") if len(line.strip()) >= 3]
    for code in lines:
        first = None
        last = None
        argument = ""
        keyword = ""
        count = 0
        for i in code:
            if i == "[" and first is None:
                first = count
            elif i == "]":
                last = count
            count += 1
        argument = code[first + 1:last]
        keyword = code[0:first]
        find = [first, last, keyword, argument]
        while "[" in argument and "]" in argument and "$" in argument:
            count = 0
            start = None
            end = None
            balance = 0
            for i in argument:
                if i == "$" and start is None:
                    start = count
                elif i == "[":
                    balance += 1
                elif i == "]":
                    end = count
                    balance -= 1
                count += 1
                if balance == 0 and start is not None and end is not None:
                    break

            if start != 0:
                argument = argument[:start] + await findBracketPairs(argument[start:end + 1]) + argument[end + 1:]
            else:
                argument = await findBracketPairs(argument)
            find = [first, last, keyword, argument]
        if find[2].lower() in funcs:
            name = await funcs[find[2].lower()](find[3])

    try:
        return name
    except:
        raise SyntaxError(f"Missing '$' in {code}")

