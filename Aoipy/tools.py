from Aoipy.Users.funcs import *

funcs = {"$username": username, "$authorid": authorID, "$send": send, "$pyeval": pyeval}


async def findBracketPairs(entry: str):
    all = entry.split("\n")
    for code in all:
        if len(code) < 3:
            continue
        code = code.strip()
        first = None
        last = None
        argument = ""
        keyword = ""
        count = 0
        for i in code:
            if i == "[" and first is None:
                first = count
                count += 1
                continue
            if i == "]":
                last = count
                count += 1
                continue
            count += 1
        argument = code[first + 1:last]
        keyword = code[0:first]
        find = [first, last, keyword, argument]
        while "[" in str(argument) and "]" in str(argument) and "$" in str(argument):
            count = 0
            start = None
            end = None
            balance = 0
            for i in argument:
                if i == "$" and start is None:
                    start = count
                    count += 1
                    continue
                if i == "[":
                    balance += 1
                if i == "]":
                    end = count
                    count += 1
                    balance -= 1
                    continue
                count += 1
                if balance == 0 and start is not None and end is not None:
                    break
            if start != 0:
                argument = str(argument[0:start]) + str(await findBracketPairs(argument[start:end + 1])) + argument[end + 1: len(argument)]
            else:
                argument = await findBracketPairs(argument)
            find = [first, last, keyword, argument]
        if find[2].lower() in funcs:
            name = await funcs[find[2].lower()](find[3])
    try:
        return name
    except:
        return "Error"
