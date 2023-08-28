from datetime import datetime as d_t
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


async def noArguments(entry: str, functions, context):
    from .all_functions import no_arg_Funcs

    for func in no_arg_Funcs:
        if func in entry:
            entry = entry.replace(
                func,
                str(await functions.execute_functions(func.lower(), None, context)),
            )

    return entry


def slashArgs(args, code):
    if "$slashArgs" in code:
        while "$slashArgs" in str(code):
            count = 0
            end = None
            balance = 0
            start = code.index("$slashArgs") + 10
            look = code[start: len(code)]
            for char in look:
                if char == "[":
                    start = count
                    count += 1
                    balance += 1
                    continue
                if char == "]":
                    end = count
                    balance -= 1
                count += 1
                if balance == 0 and start is not None and end is not None:
                    try:
                        # Replace $args with arguments
                        code = str(code).replace(
                            f"$slashArgs[{look[start + 1:end]}]",
                            args[int(look[start + 1: end]) - 1],
                        )
                        break
                    except IndexError:
                        raise SyntaxError(
                            f"$slashArgs[{int(look[start + 1:end])}] Not Provided"
                        )
    return code


EndIf = True


async def findBracketPairs(entry: str, functions, context):
    global EndIf
    test = [line.strip() for line in entry.split("\n") if len(line.strip()) >= 1]
    starts = 0
    for char in test:
        if char.strip().startswith("$") and char[-1] != "]" and "[" in char.strip():
            try:
                test[starts] = (test[starts].strip() + " " + test[starts + 1].strip()).strip()
                test.remove(test[starts + 1])
                starts += 1
            except IndexError:
                starts -= 1
                test[starts] = (test[starts].strip() + " " + test[starts + 1].strip()).strip()
                test.remove(test[starts + 1])
                starts += 1
        elif char.endswith("]") and char[0].strip() != "$":
            test[starts] = (test[starts - 1].strip() + " " + test[starts].strip()).strip()
            test.remove(test[starts - 1])
            starts += 1
        elif char[-1].strip() != "]" and char[0].strip() != "$":
            test[starts] = test[starts - 1] + " " + test[starts].strip()
            test.remove(test[starts - 1])
        elif char.strip().startswith("]"):
            test[starts] = test[starts - 1] + " " + test[starts].strip()
            test.remove(test[starts - 1])
        else:
            starts += 1
            continue

    count = 0
    for cleanup in test:
        if cleanup.strip() == "]":
            test[count - 1] = test[count - 1] + test[count]
            test.remove(test[count])
        elif cleanup.endswith("]") and cleanup[0] != "$":
            test[count - 1] = test[count - 1] + test[count]
            test.remove(test[count])
        else:
            count += 1

    if len(test) == 0:
        test = [line.strip() for line in entry.split("\n") if len(line.strip()) >= 3]
    line = 0
    for code in test:
        line += 1
        if EndIf:
            if code.strip().startswith("$end"):
                return
            if code.strip().lower().startswith("$endif"):
                continue
            elif code.strip().lower().startswith("$elif"):
                if not any("$if" in Char.lower() for Char in test):
                    raise SyntaxError("No $If found in command before $ElIf")
                EndIf = False
                continue
            else:
                pass
        else:
            if code.strip().lower().startswith("$elif"):
                EndIf = True
            elif code.strip().lower().startswith("$endif"):
                EndIf = True
                continue
            else:
                continue
        code = code.strip()
        first = None
        last = None
        count = 0
        balance1 = 0
        for char in code:
            if char == "[" and first is None:
                first = count
                balance1 += 1
                count += 1
                continue
            if char == "[":
                balance1 += 1
            elif char == "]":
                last = count
                balance1 -= 1
            if first is not None and last is not None and balance1 == 0:
                break
            count += 1
        argument = str(code[first + 1: last])
        keyword = code[0:first]
        find = [first, last, keyword, argument, context]
        func_job = False
        while "[" in str(argument) and "]" in str(argument) and "$" in str(argument) and func_job is False:
            if "$charmai" in argument.lower():
                func_job = True
            count = 0
            start = None
            end = None
            balance = 0
            for char in argument:
                digits = ["1", "2", "3", "4", "5", "6", '7', '8', "9", "0"]  # A keyword will never start or have a
                # digit in it
                if char == "$" and start is None and argument[count + 1] != "$" and argument[
                        count + 1] not in digits:  # $$keyword will discount the first $ as part of the text
                    start = count
                elif char == "[":
                    balance += 1
                elif char == "]":
                    end = count
                    balance -= 1
                count += 1
                if balance == 0 and start is not None and end is not None:
                    break
            if start != 0:
                argument = (
                        argument[:start]
                        + str(
                            await findBracketPairs(argument[start: end + 1], functions, context)
                        )
                        + argument[end + 1:]
                )
            else:
                argument = (
                        str(await findBracketPairs(argument, functions, context))
                        + argument[end + 1:]
                )
            find = [first, last, keyword, argument, context]
        if find[2].lower() in functions.funcs:
            response = await functions.execute_functions(find[2].lower(), find[3], find[4])
            if find[2].lower() == "$onlyif" and response is False:
                return
            if find[2].lower() == "$if" and response is False:
                EndIf = False
                if not any("$endif" in Char.lower() for Char in test):
                    raise SyntaxError("No $EndIf found in command after $If")
            elif find[2].lower() == "$if":
                if not any("$endif" in Char.lower() for Char in test):
                    raise SyntaxError("No $EndIf found in command after $If")

                continue
            if find[2].lower() == "$elif" and EndIf is False:
                if not any("$if" in Char.lower() for Char in test):
                    raise SyntaxError("No $If found in command before $ElIf")

                if not any("$endif" in Char.lower() for Char in test):
                    raise SyntaxError("No $EndIf found in command after $Elif")

            if find[2].lower() == "$elif":
                if not any("$if" in Char.lower() for Char in test):
                    raise SyntaxError("No $If found in command before $ElIf")

                if not any("$endif" in Char.lower() for Char in test):
                    raise SyntaxError("No $EndIf found in command after $Elif")

            EndIf = response is not False

        else:
            response = find[2]

    try:
        return response
    except Exception as e:
        raise Exception(f"Error at: {e}")


def checkArgs(args, code):
    if "$args" in code:
        while "$args" in str(code):
            if "$args[" in code:
                count = 0
                end = None
                balance = 0
                start = code.index("$args") + 5
                look = code[start: len(code)]
                for Char in look:
                    if Char == "[":
                        start = count
                        count += 1
                        balance += 1
                        continue
                    if Char == "]":
                        end = count
                        balance -= 1
                    count += 1
                    if balance == 0 and start is not None and end is not None:
                        try:
                            # Replace $args with arguments
                            code = str(code).replace(
                                f"$args[{look[start + 1:end]}]",
                                args[int(look[start + 1: end]) - 1],
                            )
                            break
                        except IndexError:
                            raise SyntaxError(
                                f"$args[{int(look[start + 1:end])}] Not Provided"
                            )
            else:
                add = [char for char in args]
                code = str(code).replace(f"$args", str(add))
    return code


async def isValid(code, functions):
    if "$isValidFunc" in code:
        while "$isValidFunc" in code:
            start = code.index("$isValidFunc[") + 13
            area = code[start:]
            if "$" not in area[:area.index(']')]:
                valid = str(f"${area[:area.index(']')]}").lower() in functions.funcs
                code = code.replace(
                    f"$isValidFunc[{area[:area.index(']')]}]", str(valid)
                )
            else:
                valid = str(f"{area[:area.index(']')]}").lower() in functions.funcs
                code = code.replace(
                    f"$isValidFunc[{area[:area.index(']')]}]", str(valid)
                )
            return code
    return code


async def checkArgCheck(args, code, context):
    if "$argcheck" in code.lower():
        if code.lower().count("$argcheck") > 1:
            raise Exception("Too many $argCheck in a single command | Max is 1!")
        start = code.lower().index("$argcheck[") + 10
        area = code[start:]
        try:
            if ";" in area[: area.index("]")]:
                arg_total = area[: area.index(";")]
                warning = area[area.index(";") + 1: area.index("]")]
                if len(args) < int(arg_total):
                    await context.channel.send(warning)
                    return "Failed"
                code = code.replace(
                    f"$argCheck[{arg_total}{area[area.index(';'):area.index(']')]}]\n",
                    "",
                )
                return code
            else:
                arg_total = area[: area.index("]")]
                if len(args) < int(arg_total):
                    return "Failed"
                code = code.replace(f"$argCheck[{arg_total}]\n", "")
                return code
        except Exception:
            raise SyntaxError("Not enough arguments in $argCheck!")
    return code


def format_datetime(datetime: d_t, form: str, tz):
    unformated_datetime = datetime.astimezone(tz)
    unformulated_datetime_tuple = (
        unformated_datetime.year,
        unformated_datetime.month,
        unformated_datetime.day,
        unformated_datetime.hour,
        unformated_datetime.minute,
        unformated_datetime.second,
        unformated_datetime.microsecond,
    )
    year, month, day, hour, minute, second, microsecond = unformulated_datetime_tuple

    am_pm = "AM" if hour < 12 else "PM"
    hour = hour if hour < 12 else hour - 12

    form = form.lower().strip()

    if form == "full":
        desired_date_form = f"USA: {month}/{day}/{year} at {hour} :{minute} :{second} :{microsecond} {am_pm}"
    elif form == "year":
        desired_date_form = str(year)
    elif form == "month":
        desired_date_form = str(month)
    elif form == "day":
        desired_date_form = str(day)
    elif form == "hour":
        desired_date_form = str(hour)
    elif form == "minute":
        desired_date_form = str(minute)
    elif form == "second":
        desired_date_form = str(second)
    elif form == "microsecond":
        desired_date_form = str(microsecond)
    elif form == "ampm":
        desired_date_form = am_pm
    else:
        desired_date_form = "ERROR"
    return desired_date_form
