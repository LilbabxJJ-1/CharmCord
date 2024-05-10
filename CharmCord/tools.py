from datetime import datetime as d_t
import discord.ext.commands
from pytz import timezone
from CharmCord.all_functions import date_funcs, ifse, all_Funcs, no_arg_Funcs
from typing import Callable
from CharmCord.functions import *

timezones = (timezone("EST"), timezone("UTC"), timezone("US/Pacific"))
lets = {}


class FunctionHandler:
    def __init__(self):
        self.funcs = {}

    def register_functions(self) -> None:
        """
        Registers functions for execution.

        Notes:
            This method registers functions for execution by iterating through all_Funcs.
            Each function is added to the 'funcs' dictionary with its lowercase name as the key.

        :return: None
        """
        for line in all_Funcs:
            function = eval(line.replace("$", ""))  # nosec
            self.funcs[line.replace("\n", "").lower()] = function
            continue

    async def execute_functions(self, keyword: str,
                                args: str,
                                context: discord.ext.commands.Context) -> Callable:
        """
        Executes functions based on the provided keyword, arguments, and context.

        Notes:
            This method checks if the keyword exists in predefined function dictionaries.

            It then executes the function with the provided arguments and context.

        :param keyword: The function keyword to execute.
        :param args: The arguments for the function.
        :param context: Discord context.
        :return: The result of executing the function.
        """
        if keyword in ifse:
            return await self.funcs[keyword](args, context)
        if keyword in date_funcs:
            return await self.funcs[keyword](args, context, timezones, format_datetime)

        return await self.funcs[keyword](args, context)


async def no_arguments(entry: str,
                       functions: FunctionHandler,
                       context: discord.ext.commands.Context) -> str:
    """
    Executes functions without arguments.

    Notes:
        This asynchronous function iterates through no_arg_Funcs and replaces each function
        occurrence in the entry string with its execution result.

    :param entry: String of CharmCord Code
    :param functions: Function Handler
    :param context: Discord Context
    :return:
    """
    for func in no_arg_Funcs:
        if func.lower() in entry:
            entry = entry.replace(
                func.lower(),
                str(await functions.execute_functions(func.lower(), '', context))
            ).replace(
                func,
                str(await functions.execute_functions(func.lower(), '', context))
            )

    return entry


def slash_args(args: list, code: str) -> str:
    """
    Replaces $slashArgs with provided arguments in the code string.

    Raises:
        SyntaxError: If the index provided in $slashArgs is out of bounds.

    :param args: The list of arguments in a slash command
    :param code: The string of CharmCord code
    :return: The modified code string with $slashArgs replaced by arguments.
    """
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
                        # Replace $slashArgs with arguments
                        code = str(code).replace(
                            f"$slashArgs[{look[start + 1:end]}]",
                            str(args[int(look[start + 1: end]) - 1]),
                        )
                        break
                    except IndexError:
                        raise SyntaxError(
                            f"$slashArgs[{int(look[start + 1:end])}] Not Provided"
                        )
    return code


async def find_bracket_pairs(entry: str, functions: FunctionHandler, context) -> None:
    """
    Async function to find and execute bracketed pairs within a command.

    Raises:
        SyntaxError: If there are syntax errors in the command structure.
        Exception: If an error occurs during execution.

    Notes:
        This function identifies and executes commands encapsulated within square brackets.
        It handles nested brackets and supports various control flow commands like $if, $elif, $else, and $end_if.
        The executed commands are based on the provided functions and context.

    :param entry: The string text of the command
    :param functions: List of all possible functions to use
    :param context: Discord context
    :return: Awaited Async functions
    """
    end_if = True
    response = None

    test = [line.strip() for line in entry.split("\n") if len(line.strip()) > 0]
    starts, pairs, index = 0, 0, 0
    new = []
    for char in test:
        pairs += char.count("[")
        pairs -= char.count("]")
        if starts >= len(test):
            starts -= 1
        if char.strip().startswith("$") and pairs > 0 and len(new) == 0:
            new.append(test[test.index(char)] + " " + test[test.index(char) + 1])
            starts += 1
            continue
        if starts == 1:
            starts += 1
            continue
        if char.strip().startswith("$") and pairs == 0 and len(new) == 0:
            new.append(test[test.index(char)])
            index += 1
        elif char.strip().startswith("$") and pairs == 0 and len(new) > 0:
            new.append(test[test.index(char)])
            index += 1
        elif char.strip().startswith("$") and pairs > 0 and len(new) > 0:
            new.append(test[test.index(char)])
            index += 1
        elif char.strip()[0] != "$" and pairs == 0 and len(new) > 0:
            new[index] = new[index] + " " + test[test.index(char)]
        elif char.strip()[0] != "$" and pairs > 0 and len(new) > 0:
            new[index] = new[index] + " " + test[test.index(char)]

    if len(new) == 0:
        test = [line.strip() for line in entry.split("\n") if len(line.strip()) >= 3]
    line = 0
    for code in new:
        line += 1
        if end_if:
            if code.strip().startswith("$end"):
                return
            if code.strip().lower().startswith("$onlyif") and line != 1:
                raise SyntaxError("$OnlyIf should only be at the beginning of a command")
            if code.strip().lower().startswith("$endif"):
                continue
            elif code.strip().lower().startswith("$elif"):
                if not any("$if" in Char.lower() for Char in test):
                    raise SyntaxError("No $If found in command before $ElIf")
                end_if = False
                continue
            else:
                pass
        else:
            if code.strip().lower().startswith("$elif"):
                end_if = True
            elif code.strip().lower().startswith("$endif"):
                end_if = True
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
        while "[" in str(argument) and "]" in str(argument) and "$" in str(argument):
            count = 0
            start = None
            end = None
            balance = 0
            for char in argument:
                digits = ["1", "2", "3", "4", "5", "6", '7', '8', "9", "0"]  # A keyword will never start or have a
                # digit in it
                if char == "$" and start is None and argument[count + 1] != "$" and argument[count + 1] not in digits:
                    # $$keyword will discount the first $ as part of the text
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
                        + str(await find_bracket_pairs(argument[start: end + 1], functions, context))
                        + argument[end + 1:]
                )
            else:
                argument = (
                        str(await find_bracket_pairs(argument, functions, context))
                        + argument[end + 1:]
                )
            find = [first, last, keyword, argument, context]
        if find[2].lower() in functions.funcs:
            response = await functions.execute_functions(find[2].lower(), find[3], find[4])
            if find[2].lower() == "$onlyif" and response is False:
                return
            if find[2].lower() == "$if" and response is False:
                end_if = False
                if not any("$endif" in Char.lower() for Char in test):
                    raise SyntaxError("No $EndIf found in command after $If")
            elif find[2].lower() == "$if":
                if not any("$endif" in Char.lower() for Char in test):
                    raise SyntaxError("No $EndIf found in command after $If")

                continue
            if find[2].lower() == "$elif" and end_if is False:
                if not any("$if" in Char.lower() for Char in test):
                    raise SyntaxError("No $If found in command before $ElIf")

                if not any("$endif" in Char.lower() for Char in test):
                    raise SyntaxError("No $EndIf found in command after $Elif")

            if find[2].lower() == "$elif":
                if not any("$if" in Char.lower() for Char in test):
                    raise SyntaxError("No $If found in command before $ElIf")

                if not any("$endif" in Char.lower() for Char in test):
                    raise SyntaxError("No $EndIf found in command after $Elif")

            end_if = response is not False

        else:
            response = find[2]

    try:
        return response
    except Exception as e:
        raise Exception(f"Error at: {e}")


def check_args(args: tuple, code: str) -> str:
    """
    Checks and replaces $args placeholders with provided arguments in the code string.

    Notes:
        This function iterates through the code string and replaces $args placeholders with provided arguments.
        It handles cases where $args is used with an index to replace specific arguments from the list.
        If no index is provided, it replaces $args with the entire list.

    :param args: Tuple of command Arguments
    :param code: String of CharmCord Code
    :return:
    """
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


async def is_valid(code: str, functions: FunctionHandler) -> str:
    if "$isValidFunc" in code:
        while "$isValidFunc" in code:
            start = code.index("$is_validFunc[") + 13
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


async def check_args_check(args: tuple,
                           code: str,
                           context: discord.ext.commands.Context) -> str:
    """
    Checks and processes $argcheck statements in the code string.

    Raises:
        Exception: If there are too many $argcheck statements in a single command.
        SyntaxError: If there are not enough arguments provided in $argcheck statements.

    Notes:
        This asynchronous function checks for $argcheck statements in the code string and processes them.
        It ensures that the number of arguments provided meets the specified criteria in $argcheck statements.
        If the conditions are not met, it may send a warning message to the channel and return "Failed".

    :param args: List of arguments
    :param code: The code string containing $argcheck statements
    :param context: Discord context
    :return: String
    """
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
    unformatted_datetime = datetime.astimezone(tz)
    unformulated_datetime_tuple = (
        unformatted_datetime.year,
        unformatted_datetime.month,
        unformatted_datetime.day,
        unformatted_datetime.hour,
        unformatted_datetime.minute,
        unformatted_datetime.second,
        unformatted_datetime.microsecond,
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
