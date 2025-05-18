from datetime import datetime as d_t
import discord.ext.commands
from pytz import timezone
from virtualenv.seed.wheels.periodic_update import periodic_update

from CharmCord.all_functions import date_funcs, ifse, all_Funcs, no_arg_Funcs
from typing import Callable
from CharmCord.CharmErrorHandling import CharmCordError
from CharmCord.functions import *
import re

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

        pattern = re.compile(re.escape(func), re.IGNORECASE)
        matches = pattern.findall(entry)

        if bool(len(matches)):
            for match in matches:
                result = str(await functions.execute_functions(func.lower(), '', context))
                entry = entry.replace(match, result)

            entry = await no_arguments(entry, functions, context)
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
            arg_start, arg_end, bracket_balance = code.index("$slashArgs") + 10, None, 0
            if code[arg_start] != "[":
                 raise CharmCordError(
                    error_msg='No opening bracket for $slashArgs',
                    code_sample=code,

                )
            look = code[arg_start: len(code)]
            for position_num, char in enumerate(look):
                if char == "[":
                    arg_start = position_num
                    bracket_balance += 1
                    continue

                if char == "]":
                    arg_end = position_num
                    bracket_balance -= 1

                if bracket_balance == 0 and arg_start is not None and arg_end is not None:
                    try:
                        # Replace $slashArgs with arguments
                        code = str(code).replace(
                            f"$slashArgs[{look[arg_start + 1:arg_end]}]",
                            str(args[int(look[arg_start + 1: arg_end]) - 1]),
                        )
                        break
                    except IndexError:
                        raise CharmCordError(
                            error_msg=f"$slashArgs[{int(look[arg_start + 1:arg_end])}] Not Provided",
                            code_sample=code
                        )
    return code


def break_code_down(code: str) -> list:
    original_code = [line_of_code.strip() for line_of_code in code.split("\n") if len(line_of_code.strip()) > 0]
    pairs_of_brackets, index = 0, 0
    formatted_code = []
    for character in original_code:
        pairs_of_brackets += character.count("[")
        pairs_of_brackets -= character.count("]")

        if pairs_of_brackets > 0:
            if len(formatted_code) > 0:
                formatted_code[len(formatted_code) - 1] = formatted_code[len(formatted_code) - 1] + original_code[original_code.index(character) + 1]
            else:
                formatted_code.append(original_code[original_code.index(character)] + original_code[
                    original_code.index(character) + 1])
            continue

    if len(formatted_code) == 0:
        formatted_code = [line_of_code.strip() for line_of_code in code.split("\n") if len(line_of_code.strip()) > 3]

    return formatted_code


async def find_bracket_pairs(raw_code: str, func_executor: FunctionHandler, context) -> None:
        """
        Async function to find and execute bracketed pairs within a command.

        Raises:
            SyntaxError: If there are syntax errors in the command structure.
            Exception: If an error occurs during execution.

        Notes:
            This function identifies and executes commands encapsulated within square brackets.
            It handles nested brackets and supports various control flow commands like $if, $elif, $else, and $end_if.
            The executed commands are based on the provided functions and context.

        :param raw_code: The string text of the command
        :param func_executor: List of all possible functions to use
        :param context: Discord context
        :return: Awaited Async functions
        """
        end_if: bool = True  # True when no "If" clause is currently in progress
        function_response = None
        line_number = 0
        formatted_code = break_code_down(raw_code)

        for line_of_code in formatted_code:
            line_number += 1
            lowercase_line_of_code: str = line_of_code.strip().lower()
            if end_if:

                if lowercase_line_of_code.startswith("$end"):
                    return

                if lowercase_line_of_code.startswith("$onlyif") and line_number != 1:
                    raise CharmCordError(error_msg="$OnlyIf should be at the beginning of a command",
                                                 code_sample=line_of_code,
                                                 command_name=context.command.name)

                if lowercase_line_of_code.startswith("$endif"):
                    continue

                elif lowercase_line_of_code.startswith("$elif"):
                    for check_line_number, code_line in enumerate(formatted_code):
                        if code_line.lower().startswith("$if"):
                            break

                        if check_line_number + 1 == line_number:
                            raise CharmCordError(error_msg="No $If found in command before $ElIf",
                                                         code_sample=line_of_code,
                                                         command_name=context.command.name)
                    end_if = False
                    continue

                else:
                    pass

            else:
                if lowercase_line_of_code.startswith("$elif"):
                    end_if = True

                elif lowercase_line_of_code.startswith("$endif"):
                    end_if = True
                    continue

                else:
                    continue

            first_bracket, last_bracket, keyword_start, bracket_balance = None, None, None, 0
            digits = ["1", "2", "3", "4", "5", "6", '7', '8', "9", "0"]
            for char_number, character in enumerate(lowercase_line_of_code):
                try:
                    if character == '$' and keyword_start is None and lowercase_line_of_code[char_number + 1] != "$" and lowercase_line_of_code[
                        char_number + 1] not in digits:
                        keyword_start = char_number
                except IndexError:
                    pass

                if character == '[' and not first_bracket:
                    first_bracket = char_number
                    bracket_balance += 1
                    continue

                if character == '[':
                    bracket_balance += 1

                elif character == "]":
                    last_bracket = char_number
                    bracket_balance -= 1

                if first_bracket is not None and last_bracket is not None and not bool(bracket_balance):
                    break

            argument = line_of_code[first_bracket + 1: last_bracket]
            keyword = line_of_code[keyword_start:first_bracket]
            digits = ["1", "2", "3", "4", "5", "6", '7', '8', "9", "0"]
            parsed_command = [keyword, argument, context, first_bracket, last_bracket]
            while all(searched in argument for searched in ["]", "["]) and any(searched in argument for searched in all_Funcs):
                arg_first_bracket, arg_last_bracket, arg_keyword_start, arg_bracket_balance = None, None, None, 0
                for char_number, character in enumerate(argument):
                    if character == '$' and arg_keyword_start is None and argument[char_number + 1] != "$" and argument[char_number + 1] not in digits:
                         arg_keyword_start = char_number

                    if character == '[' and arg_first_bracket is None and argument[char_number + 1] != "$" and argument[char_number + 1] not in digits:
                        arg_first_bracket = char_number
                        arg_bracket_balance += 1

                    elif character == '[':
                        arg_bracket_balance += 1

                    elif character == ']':
                        arg_last_bracket = char_number
                        arg_bracket_balance -= 1

                    if not bool(arg_bracket_balance) and arg_first_bracket is not None and arg_last_bracket is not None:
                        break

                if bool(arg_keyword_start):
                        argument = (argument[:arg_keyword_start]
                                    + str(await find_bracket_pairs(argument[arg_keyword_start: arg_last_bracket + 1],
                                                                   func_executor,
                                                                   context))
                                    + argument[arg_last_bracket + 1:]
                                    )

                elif bool(arg_first_bracket) and bool(arg_last_bracket):
                    argument = (argument[:arg_keyword_start]
                                + str(await find_bracket_pairs(argument[arg_keyword_start: arg_last_bracket + 1],
                                                               func_executor,
                                                               context))
                                + argument[arg_last_bracket + 1:]
                                )

                else:
                    argument = (str(await find_bracket_pairs(argument, func_executor, context))
                                + argument[arg_last_bracket + 1:])

                parsed_command = [keyword, argument, context, first_bracket, last_bracket]
            if parsed_command[0].lower() in func_executor.funcs:
                function_response = await func_executor.execute_functions(parsed_command[0].lower(),
                                                                          parsed_command[1],
                                                                          parsed_command[2])

                if parsed_command[0].lower() == '$onlyif' and not function_response:
                    return

                if parsed_command[0].lower() == '$if':
                    if not function_response:
                        end_if = False
                    for check_line_number, code_line in enumerate(formatted_code):
                        if code_line.lower() == "$endif":
                                break
                            
                        if check_line_number + 1 <= line_number:
                            continue


                    else:
                        raise CharmCordError(error_msg="No $EndIf found in command after $If",
                                                    code_sample=line_of_code,
                                                    command_name=context.command.name)

                    continue

                if parsed_command[0].lower() == '$elif':
                    for check_line_number, code_line in enumerate(formatted_code):
                        if check_line_number + 1 <= line_number:
                            continue

                        if code_line.lower() == "$endif":
                                break

                    else:
                        raise CharmCordError(error_msg="No $EndIf found in command after $ElIf",
                                                    code_sample=line_of_code,
                                                    command_name=context.command.name)

                    for check_line_number, code_line in enumerate(formatted_code):
                        if check_line_number + 1 == line_number:
                            raise CharmCordError(error_msg="No $If found in command before $ElIf",
                                                         code_sample=line_of_code,
                                                         command_name=context.command.name)

                        if code_line.lower().startswith("$if"):
                            break

                end_if = function_response is not False

            else:
                function_response = parsed_command[0]

        try:

            return function_response
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
