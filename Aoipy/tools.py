from Aoipy.Functions import *
from Aoipy.all_functions import all_Funcs, date_funcs
from datetime import datetime as D_T
from pytz import timezone

timezones = (
    timezone('EST'),
    timezone('UTC'),
    timezone('US/Pacific')
)


class FunctionHandler:

    def __init__(self):
        self.funcs = {}

    def register_functions(self):
        for line in all_Funcs:
            function = eval(line.replace("$", ""))
            self.funcs[line.replace("\n", "").lower()] = function

    async def execute_functions(self, keyword, args, context):
        if keyword in date_funcs:
            return await self.funcs[keyword](args, context, timezones, format_datetime)
        return await self.funcs[keyword](args, context)


async def noArguments(entry: str, Functions, context):
    from .all_functions import no_arg_Funcs
    for func in no_arg_Funcs:
        if func in entry:
            entry = entry.replace(func, str(await Functions.execute_functions(func.lower(), None, context)))

    return entry


async def findBracketPairs(entry: str, Functions, context):
    test = [line.strip() for line in entry.split("\n") if len(line.strip()) >= 3]
    starts = 0
    for i in test:
        if i.strip().startswith("$") and i[-1] != "]":
            try:
                test[starts] = (test[starts].strip() + " " + test[starts + 1].strip()).strip()
                test.remove(test[starts + 1])
                starts += 1
            except IndexError:
                starts -= 1
                test[starts] = (test[starts].strip() + " " + test[starts + 1].strip()).strip()
                test.remove(test[starts + 1])
                starts += 1
        elif i.endswith("]") and i[0].strip() != "$":
            test[starts] = (test[starts - 1].strip() + " " + test[starts].strip()).strip()
            test.remove(test[starts - 1])
            starts += 1
        elif i[-1].strip() != "]" and i[0].strip() != "$":
            test[starts] = (test[starts - 1] + " " + test[starts].strip())
            test.remove(test[starts - 1])
        else:
            continue
    try:
        if test[-1].endswith("]") and test[-2][-1] != "]":
            test[-2] = test[-2] + " " + test[-1].strip()
            test.remove(test[-1])
    except:
        pass

    if len(test) == 0:
        test = [line.strip() for line in entry.split("\n") if len(line.strip()) >= 3]
    for code in test:
        code = code.strip()
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


def format_datetime(datetime: D_T, FORM: str, TIMEZONE):
    UnformatedDatetime = datetime.astimezone(TIMEZONE)
    UnformatedDatetimeTuple = (
        UnformatedDatetime.year, UnformatedDatetime.month, UnformatedDatetime.day, UnformatedDatetime.hour, UnformatedDatetime.minute,
        UnformatedDatetime.second, UnformatedDatetime.microsecond)
    year, month, day, hour, minute, second, microsecond = UnformatedDatetimeTuple

    AM_PM = "AM" if hour < 12 else "PM"
    hour = hour if hour < 12 else hour - 12

    FORM = FORM.lower().strip()

    if FORM == "full":
        desiredDateForm = f"USA: {month}/{day}/{year} at {hour} :{minute} :{second} :{microsecond} {AM_PM}"
    elif FORM == "year":
        desiredDateForm = str(year)
    elif FORM == "month":
        desiredDateForm = str(month)
    elif FORM == "day":
        desiredDateForm = str(day)
    elif FORM == "hour":
        desiredDateForm = str(hour)
    elif FORM == "minute":
        desiredDateForm = str(minute)
    elif FORM == "second":
        desiredDateForm = str(second)
    elif FORM == "microsecond":
        desiredDateForm = str(microsecond)
    elif FORM == "ampm":
        desiredDateForm = AM_PM
    else:
        desiredDateForm = "ERROR"
    return desiredDateForm
