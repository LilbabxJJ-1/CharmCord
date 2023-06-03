import asyncio


async def wait(seconds, context):
    return await asyncio.sleep(int(seconds))
