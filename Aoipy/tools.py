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
    lines_of_function = [line.strip() for line in entry.split("\n") if len(line.strip()) >= 3]

    for code in lines_of_function:
        print(code)
        first    = None; last     = None
        count    = 0   ; balance1 = 0
        
        first_and_last = first is None and last is None
        
        #    count stuff
        for i in code:

            if i == "[" and first is None:
                first     = count
                balance1 += 1
                count    += 1
                continue

            if i == "[":
                balance1 += 1

            elif i == "]":
                last      = count
                balance1 -= 1

            if not first_and_last and balance1 == 0:   break

            count += 1
        #end count stuff

        argument = str(code[first + 1:last])
        keyword  =     code[0:first]
        find     = [first, last, keyword, argument, context]

        #    Magic
        while "[" in argument and "]" in argument and "$" in argument:
            start = None; end     = None
            count = 0   ; balance = 0
            
            start_and_end = start is None and end is None

            for i in argument:
                if i == "$" and start is None:
                    start = count
                elif i == "[":
                    balance += 1
                elif i == "]":
                    end = count
                    balance -= 1
                count += 1
                if not start_and_end and balance == 0: break

            
            
            if start != 0:
                argument = argument[:start] + str(await findBracketPairs(argument[start:end + 1], Functions, context)) + argument[end + 1:]
            else:
                argument =                    str(await findBracketPairs(argument,                Functions, context)) + argument[end + 1:]
            
            
            find = (first, last, keyword, argument, context)
        #END Magic

        first, last, keyword, argument, context                                                                                              = find


        if keyword.lower() in Functions.funcs:
            name = await Functions.execute_functions(keyword.lower(), argument, context)
        
        else:
            name = keyword

    try:
        return name

    except    Exception as e:
        raise Exception(f"Error at: {e}")


def checkArgs(args, Code):
    if '$args' in Code:
        while "$args" in str(Code):
            end = None; count = 0; balance = 0

            start = Code.index("$args") + 5
            look  = Code[start:len(Code)]


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
