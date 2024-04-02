import discord
from discord.ui import button, view
from btnOpts import buttons


async def addButton(args, ctx):

    class View(view):

        @button(label="testing", custom_id="test2")
        async def button_go(self):
            print("Button Worked")

    buttons.append(view)