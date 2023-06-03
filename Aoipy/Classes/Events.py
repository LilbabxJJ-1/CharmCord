from Aoipy.tools import findBracketPairs

#######################################
#              EVENTS                 #
#######################################


class AoiEvents:
    def onReady(self, code):
        from Aoipy.Classes.AoiPyClient import bots, TotalFuncs
        # Define on_ready event function
        @bots.event
        async def on_ready():
            await findBracketPairs(code, TotalFuncs, None)