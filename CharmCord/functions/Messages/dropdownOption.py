from ._btnOpts_ import dropdown_values


async def dropdownOption(args: str, ctx):
    try:
        label, value = args.split(";")
    except Exception:
        raise SyntaxError("$dropdownOption needs a label and value")

    dropdown_values.append({
        "label": label,
        "value": value
    })
    return
