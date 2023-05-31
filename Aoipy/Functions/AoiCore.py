from Aoipy.tools import findBracketPairs, FunctionHandler
from Aoipy.Functions import *
import os

# Global variables
global bots




    ########################################
    #              EVENTS                  #
    ########################################


class AoiEvents:
    def onReady(self, code):
        # Define on_ready event function
        @bots.event
        async def on_ready():
            await findBracketPairs(code, TotalFuncs, None)

