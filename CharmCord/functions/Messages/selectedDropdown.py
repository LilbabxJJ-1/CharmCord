from ._btnOpts_ import currently_selected


async def selectedDropdown(args, ctx):
    return currently_selected[0]
