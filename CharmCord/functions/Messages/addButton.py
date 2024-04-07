from discord.ui import View, Button
from ._btnOpts_ import interactions, views
from CharmCord.globeHandler import get_globals


async def addButton(args, ctx):
    from CharmCord.tools import checkArgCheck, checkArgs, findBracketPairs, noArguments, lets, isValid
    try:
        label, custom_id = args.split(";")
    except:
        raise SyntaxError("$addButton needs a label and custom_id")

    if sum(1 for val in interactions.values() if val == custom_id) > 1:
        raise Exception(f"Multiple interactions with '{custom_id}' ID found! Please make sure all IDs are unique")

    class MyView(View):
        def __init__(self):
            super().__init__()
            self.all_buttons = {}

        def add_button(self, button_name, button_instance):
            self.all_buttons[button_name] = button_instance
            return

        def get_button(self, button_name):
            if button_name in self.all_buttons:
                return self.all_buttons[button_name]
            return None

    if len(views) == 0:
        async def button_go(button_interaction):
            funcs = get_globals()[0]
            views.clear()
            try:
                codes = interactions[custom_id]
            except KeyError:
                raise Exception(f"There's no code for button: {custom_id}")
            new_code = await checkArgCheck(args, codes, button_interaction)
            if new_code == "Failed":
                return
            code1 = await noArguments(new_code, funcs, button_interaction)
            code2 = checkArgs(args, code1)
            final_code = await isValid(code2, funcs)
            await findBracketPairs(final_code, funcs, button_interaction)
            if len(lets) >= 1:
                lets.clear()

        data = Button(label=label, custom_id=custom_id)
        mine = MyView()
        mine.add_button(label, data)
        views.append(mine)
        data.callback = button_go
        views[0].add_item(data)
    else:
        async def button_go(button_interaction):
            funcs = get_globals()[0]
            views.clear()
            codes = interactions[custom_id]
            new_code = await checkArgCheck(args, codes, button_interaction)
            if new_code == "Failed":
                return
            code1 = await noArguments(new_code, funcs, button_interaction)
            code2 = checkArgs(args, code1)
            final_code = await isValid(code2, funcs)
            await findBracketPairs(final_code, funcs, button_interaction)
            if len(lets) >= 1:
                lets.clear()

        data = Button(label=label, custom_id=custom_id)
        data.callback = button_go
        views[0].add_item(data)
    return
