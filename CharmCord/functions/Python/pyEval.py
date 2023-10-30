import ast


async def pyEval(code, context):
    answer = ast.literal_eval(code)
    return answer
