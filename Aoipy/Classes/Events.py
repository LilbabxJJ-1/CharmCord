from Aoipy.tools import findBracketPairs

#######################################
#              EVENTS                 #
#######################################

#
#class AoiEvents:
#    def onReady(self, code):
#        from Aoipy.Classes.AoiPyClient import bots, TotalFuncs
#        # Define on_ready event function
#        @bots.event
#        async def on_ready():
#            await findBracketPairs(code, TotalFuncs, None)
#
#    def onGuildChannelDelete(self):
#        from Aoipy.Classes.AoiPyClient import bots
#        from Aoipy.Functions.Events.onChannelDelete import options
#        @bots.event
#        async def on_guild_channel_delete(channel):
#            options["name"] = channel.name
#            options['id'] = channel.id
#
#
#