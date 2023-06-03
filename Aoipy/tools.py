from Aoipy.Functions import *
from Aoipy.all_functions import funcs


class FunctionHandler:

    def __init__(self):
        self.funcs = {}

    def register_functions(self):
        for line in funcs:
            function = eval(line.replace("$", ""))
            self.funcs[line.replace("\n", "").lower()] = function

    async def execute_functions(self, keyword, args, context):
        return await self.funcs[keyword](args, context)


async def findBracketPairs(entry: str, Functions, context):
    lines = [line.strip() for line in entry.split("\n") if len(line.strip()) >= 3]
    for code in lines:
        first = None
        last = None
        count = 0
        balance1 = 0
        for i in code:
            if i == "[" and first is None:
                first = count
                balance1 += 1
                count += 1
                continue
            if i == "[":
                balance1 += 1
            elif i == "]":
                last = count
                balance1 -= 1
            if first is not None and last is not None and balance1 == 0:
                break
            count += 1
        argument = str(code[first + 1:last])
        keyword = code[0:first]
        find = [first, last, keyword, argument, context]
        while "[" in str(argument) and "]" in str(argument) and "$" in str(argument):
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
                argument = argument[:start] + str(await findBracketPairs(argument[start:end + 1], Functions, context)) + argument[end + 1:]
            else:
                argument = str(await findBracketPairs(argument, Functions, context)) + argument[end + 1:]
            find = [first, last, keyword, argument, context]
        if find[2].lower() in Functions.funcs:
            name = await Functions.execute_functions(find[2].lower(), find[3], find[4])
        else:
            name = find[2]

    try:
        return name
    except Exception as e:
        raise Exception(f"Error at: {e}")


def checkArgs(args, Code):
    if '$args' in Code:
        while "$args" in str(Code):
            count = 0
            end = None
            balance = 0
            start = Code.index("$args") + 5
            look = Code[start:len(Code)]
            for i in look:
                if i == "[":
                    start = count
                    count += 1
                    balance += 1
                    continue
                if i == "]":
                    end = count
                    balance -= 1
                count += 1
                if balance == 0 and start is not None and end is not None:
                    try:
                        # Replace $args with arguments
                        Code = str(Code).replace(f"$args[{look[start + 1:end]}]", args[int(look[start + 1:end]) - 1])
                        break
                    except IndexError:
                        raise SyntaxError(F"$args[{int(look[start + 1:end])}] Not Provided")
    return Code


async def checkArgCheck(args, Code, Context):
    if "$argCheck" in Code:
        if Code.count("$argCheck") > 1:
            raise Exception("Too many $argCheck in a single command | Max is 1!")
        start = Code.index("$argCheck[") + 10
        area = Code[start:]
        try:
            if ";" in area[:area.index("]")]:
                argTotal = area[:area.index(";")]
                warning = area[area.index(";") + 1:area.index("]")]
                if len(args) < int(argTotal):
                    await Context.channel.send(warning)
                    return 'Failed'
                Code = Code.replace(f"$argCheck[{argTotal}{area[area.index(';'):area.index(']')]}]\n", "")
                return Code
            else:
                argTotal = area[:area.index("]")]
                if len(args) < int(argTotal):
                    return 'Failed'
                Code = Code.replace(f"$argCheck[{argTotal}]\n", "")
                return Code
        except Exception as e:
            print(e)
            raise SyntaxError("Not enough arguments in $argCheck!")
    return Code
