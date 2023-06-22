async def deleteMessage(args, Context):
    try:
        msg_id = args
        msg = await Context.channel.fetch_message(int(msg_id))
        if msg is None:
            raise SyntaxError(f"$deleteMessage Message not found with ID: {msg_id}\nCommand: '{Context.command.name}'")
        await msg.delete()
        return
    except ValueError:
        raise SyntaxError(f"$deleteMessage Invalid ID provided in command: '{Context.command.name}'")
