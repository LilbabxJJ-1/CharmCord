from datetime import datetime as D_T
from pytz import timezone
from CharmCord.all_functions import date_funcs, ifse
from .Functions import *

timezones = (timezone("EST"), timezone("UTC"), timezone("US/Pacific"))
lets = {}


class FunctionHandler:
    def __init__(self):
        self.funcs = {}

    def register_functions(self):
        for line in all_Funcs:
            function = eval(line.replace("$", ""))  # nosec
            self.funcs[line.replace("\n", "").lower()] = function

    async def execute_functions(self, keyword, args, context):
        if keyword in ifse:
            check = await self.funcs[keyword](args, context)
            return check
        if keyword in date_funcs:
            return await self.funcs[keyword](args, context, timezones, format_datetime)
        return await self.funcs[keyword](args, context)


async def noArguments(entry: str, Functions, context):
    from .all_functions import no_arg_Funcs

    for func in no_arg_Funcs:
        if func in entry:
            entry = entry.replace(
                func,
                str(await Functions.execute_functions(func.lower(), None, context)),
            )

    return entry


def slashArgs(args, Code):
    if "$slashArgs" in Code:
        while "$slashArgs" in str(Code):
            count = 0
            end = None
            balance = 0
            start = Code.index("$slashArgs") + 10
            look = Code[start: len(Code)]
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
                        Code = str(Code).replace(
                            f"$slashArgs[{look[start + 1:end]}]",
                            args[int(look[start + 1: end]) - 1],
                        )
                        break
                    except IndexError:
                        raise SyntaxError(
                            f"$slashArgs[{int(look[start + 1:end])}] Not Provided"
                        )
    return Code


EndIf = True


async def findBracketPairs(entry: str, Functions, context):
    global EndIf
    test = [line.strip() for line in entry.split("\n") if len(line.strip()) >= 3]
    starts = 0
    for i in test:
        if i.strip().startswith("$") and i[-1] != "]" and "[" in i.strip():
            try:
                test[starts] = (
                        test[starts].strip() + " " + test[starts + 1].strip()
                ).strip()
                test.remove(test[starts + 1])
                starts += 1
            except IndexError:
                starts -= 1
                test[starts] = (
                        test[starts].strip() + " " + test[starts + 1].strip()
                ).strip()
                test.remove(test[starts + 1])
                starts += 1
        elif i.endswith("]") and i[0].strip() != "$":
            test[starts] = (
                    test[starts - 1].strip() + " " + test[starts].strip()
            ).strip()
            test.remove(test[starts - 1])
            starts += 1
        elif i[-1].strip() != "]" and i[0].strip() != "$":
            test[starts] = test[starts - 1] + " " + test[starts].strip()
            test.remove(test[starts - 1])
        else:
            starts += 1
            continue

    if len(test) == 0:
        test = [line.strip() for line in entry.split("\n") if len(line.strip()) >= 3]
    line = 0
    for code in test:
        line += 1
        if EndIf:
            if code.strip().startswith("$EndIf"):
                continue
            elif code.strip().startswith("$ElIf"):
                if not any("$If" in i for i in test):
                    raise SyntaxError("No $If found in command before $ElIf")
                EndIf = False
                continue
            else:
                pass
        else:
            if code.strip().startswith("$ElIf"):
                EndIf = True
            elif code.strip().startswith("$EndIf"):
                EndIf = True
                continue
            else:
                continue
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
        argument = str(code[first + 1: last])
        keyword = code[0:first]
        find = [first, last, keyword, argument, context]
        while "[" in str(argument) and "]" in str(argument) and "$" in str(argument):
            count = 0
            start = None
            end = None
            balance = 0
            for i in argument:
                digits = ["1", "2", "3", "4", "5", "6", '7', '8', "9", "0"]  # A keyword will never start or have a digit in it
                if i == "$" and start is None and argument[count + 1] != "$" and argument[count + 1] not in digits:  # $$keyword will discount the first $ as part of the text
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
                argument = (
                        argument[:start]
                        + str(
                    await findBracketPairs(argument[start: end + 1], Functions, context)
                )
                        + argument[end + 1:]
                )
            else:
                argument = (
                        str(await findBracketPairs(argument, Functions, context))
                        + argument[end + 1:]
                )
            find = [first, last, keyword, argument, context]
        if find[2].lower() in Functions.funcs:
            name = await Functions.execute_functions(find[2].lower(), find[3], find[4])
            if find[2] == "$onlyIf" and name is False:
                return
            if find[2] == "$If" and name is False:
                EndIf = False
                if not any("$EndIf" in i for i in test):
                    raise SyntaxError("No $EndIf found in command after $If")
            elif find[2] == "$If":
                if not any("$EndIf" in i for i in test):
                    raise SyntaxError("No $EndIf found in command after $If")

                continue
            if find[2] == "$ElIf" and EndIf is False:
                if not any("$If" in i for i in test):
                    raise SyntaxError("No $If found in command before $ElIf")

                if not any("$EndIf" in i for i in test):
                    raise SyntaxError("No $EndIf found in command after $Elif")

            if find[2] == "$ElIf":
                if not any("$If" in i for i in test):
                    raise SyntaxError("No $If found in command before $ElIf")

                if not any("$EndIf" in i for i in test):
                    raise SyntaxError("No $EndIf found in command after $Elif")

            EndIf = name is not False

        else:
            name = find[2]

    try:
        return name
    except Exception as e:
        raise Exception(f"Error at: {e}")


def checkArgs(args, Code):
    if "$args" in Code:
        while "$args" in str(Code):
            if "$args[" in Code:
                count = 0
                end = None
                balance = 0
                start = Code.index("$args") + 5
                look = Code[start: len(Code)]
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
                            Code = str(Code).replace(
                                f"$args[{look[start + 1:end]}]",
                                args[int(look[start + 1: end]) - 1],
                            )
                            break
                        except IndexError:
                            raise SyntaxError(
                                f"$args[{int(look[start + 1:end])}] Not Provided"
                            )
            else:
                new = ""
                for i in args:
                    new += f"{i} "
                Code = str(Code).replace(f"$args", new)
    return Code


async def checkArgCheck(args, Code, Context):
    if "$argCheck" in Code:
        if Code.count("$argCheck") > 1:
            raise Exception("Too many $argCheck in a single command | Max is 1!")
        start = Code.index("$argCheck[") + 10
        area = Code[start:]
        try:
            if ";" in area[: area.index("]")]:
                argTotal = area[: area.index(";")]
                warning = area[area.index(";") + 1: area.index("]")]
                if len(args) < int(argTotal):
                    await Context.channel.send(warning)
                    return "Failed"
                Code = Code.replace(
                    f"$argCheck[{argTotal}{area[area.index(';'):area.index(']')]}]\n",
                    "",
                )
                return Code
            else:
                argTotal = area[: area.index("]")]
                if len(args) < int(argTotal):
                    return "Failed"
                Code = Code.replace(f"$argCheck[{argTotal}]\n", "")
                return Code
        except Exception:
            raise SyntaxError("Not enough arguments in $argCheck!")
    return Code


def format_datetime(datetime: D_T, FORM: str, TIMEZONE):
    UnformatedDatetime = datetime.astimezone(TIMEZONE)
    UnformatedDatetimeTuple = (
        UnformatedDatetime.year,
        UnformatedDatetime.month,
        UnformatedDatetime.day,
        UnformatedDatetime.hour,
        UnformatedDatetime.minute,
        UnformatedDatetime.second,
        UnformatedDatetime.microsecond,
    )
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
