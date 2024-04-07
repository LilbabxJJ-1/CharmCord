import discord
from ._btnOpts_ import dropdown_options, interactions, views, dropdown_values, currently_selected
from CharmCord.globeHandler import get_globals


async def addDropdown(args, ctx):
    from CharmCord.tools import checkArgCheck, checkArgs, findBracketPairs, noArguments, lets, isValid
    try:
        placeHolder, custom_id = args.split(";")

    except:
        raise SyntaxError("$addDropdown needs a placeholder and custom_id")

    if sum(1 for val in interactions.values() if val == custom_id) > 1:
        raise Exception(f"Multiple interactions with '{custom_id}' ID found! Please make sure all IDs are unique")

    if len(dropdown_values) == 0:
        raise Exception("No Dropdown options created")

    for option in dropdown_values:
        dropdown_options.append(discord.SelectOption(label=option['label'], value=option['value']))

    async def drop_go(drop_interaction):
        if len(currently_selected) == 0:
            currently_selected.append(drop_interaction.data['values'][0])
        else:
            currently_selected[0] = drop_interaction.data['values'][0]

        funcs = get_globals()[0]
        views.clear()
        codes = interactions[custom_id]
        new_code = await checkArgCheck(args, codes, drop_interaction)

        if new_code == "Failed":
            return

        code1 = await noArguments(new_code, funcs, drop_interaction)
        code2 = checkArgs(args, code1)
        final_code = await isValid(code2, funcs)
        await findBracketPairs(final_code, funcs, drop_interaction)

        if len(lets) >= 1:
            lets.clear()

    select = discord.ui.Select(placeholder=placeHolder, options=dropdown_options, custom_id=custom_id)
    select.callback = drop_go

    if len(views) == 0:
        views.append(discord.ui.View().add_item(select))
    else:
        views[0].add_item(select)

    return
