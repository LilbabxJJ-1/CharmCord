from CharmCord.CharmErrorHandling import CharmCordErrors


async def channelCreated(args: str, context, timezones, format_datetime):
    """
    Ex. $channelCreated[ChannelID]
    """
    if len(args) < 1:
        raise CharmCordErrors("No parameter provided for '$channelCreated'")
    est, utc, pst = timezones
    try:
        ids, time, form = tuple(args.split(";"))
        time = locals()[time.strip()]
        form = form.lower()
    except ValueError:
        form = "full"
        try:
            ids, time = tuple(args.split(","))
            time = locals()[time.strip()]
        except:
            ids = args
            time = utc

    from CharmCord.utils.CharmCord import bots

    try:
        channel = await bots.fetch_channel(ids.replace("<#", "").replace(">", ""))

        desiredDateForm = format_datetime(channel.created_at, form, time)
        if desiredDateForm != "ERROR":
            return desiredDateForm
        else:
            raise SyntaxError("Invalid Format option in $channelCreated!")

    except ValueError:
        CharmCordErrors(f"$channelCreated: {ids} not valid channel id\nCommand: {context.command.name}")
