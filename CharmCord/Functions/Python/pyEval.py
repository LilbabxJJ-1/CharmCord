import ast


async def pyEval(code, Context):
    answer = ast.literal_eval(code)
    return answer
