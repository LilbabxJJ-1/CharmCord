import discord
from ._btnOpts_ import dropdown_options, interactions, views, dropdown_values, currently_selected
from CharmCord.globeHandler import get_globals


async def addDropdown(args, ctx):
    from CharmCord.tools import check_args_check, check_args, find_bracket_pairs, no_arguments, lets, is_valid
    try:
        placeHolder, custom_id, minimum, maximum = args.split(";")

    except:
        raise SyntaxError("$addDropdown needs a placeholder and custom_id")

    if sum(1 for val in interactions.values() if val == custom_id) > 1:
        raise Exception(f"Multiple interactions with '{custom_id}' ID found! Please make sure all IDs are unique")

    if len(dropdown_values) == 0:
        raise Exception("No Dropdown options created")

    dropdown_options.clear()
    for option in dropdown_values:
        dropdown_options.append(discord.SelectOption(label=option['label'], value=option['value']))
    dropdown_values.clear()

    async def drop_go(drop_interaction):
        selects = []
        for selected in drop_interaction.data['values']:
            selects.append(selected)
        data = {f"{ctx.guild.id}": selects}
        for count, user_selections in enumerate(currently_selected):
            if f"{ctx.guild.id}" in user_selections:
                currently_selected[count] = data
                break
        else:
            currently_selected.append(data)


        funcs = get_globals()[0]
        views.clear()
        codes = interactions[custom_id]
        new_code = await check_args_check(args, codes, drop_interaction)

        if new_code == "Failed":
            return

        code1 = await no_arguments(new_code, funcs, drop_interaction)
        code2 = check_args(args, code1)
        final_code = await is_valid(code2, funcs)
        await find_bracket_pairs(final_code, funcs, drop_interaction)

        if len(lets) >= 1:
            lets.clear()

    select = discord.ui.Select(placeholder=placeHolder, options=dropdown_options, custom_id=custom_id, min_values=minimum, max_values=maximum)
    select.callback = drop_go

    if len(views) == 0:
        views.append(discord.ui.View().add_item(select))


    return
