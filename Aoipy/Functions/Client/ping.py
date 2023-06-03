
async def ping(emp, Context):
    from Aoipy.Classes.AoiPyClient import bots
    return round(bots.latency * 1000, 2)