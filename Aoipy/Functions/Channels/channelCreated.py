import Aoipy.AoiErrorHandling as ErrorHandling
EH = ErrorHandling.AoipyErrorHandling()

async def channelCreated(args: str, Context, timezones, format_datetime):
    if len(args) < 1:
        raise EH.Errors(4, "No parameter provided for '$channelCreated'")
    est, utc, pst = timezones
    try:
        ID, TIME, FORM = tuple(args.split(","))
        TIME = locals()[TIME.strip()]
        FORM = FORM.lower()
    except ValueError:
        FORM="full"
        try:
            ID, TIME = tuple(args.split(","))
            TIME = locals()[TIME.strip()]
        except:
            ID   = args
            TIME = utc
    


    
    from Aoipy.Classes.AoiPyClient import bots
    try:
        int(ID)
        channel = await bots.fetch_channel(ID)

        desiredDateForm = format_datetime(channel.created_at, FORM, TIME)
        if desiredDateForm != "ERROR":
            return desiredDateForm
        else:
            raise SyntaxError("Invalid Format option in $channelCreated!")

    except ValueError:
        EH.Errors(2, ID)