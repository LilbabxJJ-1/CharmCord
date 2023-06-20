

async def editMessage(args, Context):
    if ";" in args:
        values = args.split(";")
        try:
            msg_id, new_msg = values[0], values[1]
            msg = await Context.channel.fetch_message(int(msg_id))
            if msg is None:
                raise SyntaxError(f"$editMessage Message not found with ID: {msg_id}\nCommand: '{Context.command.name}'")
            await msg.edit(content=new_msg)
            return
        except IndexError:
            raise SyntaxError(f"$editMessage requires 2 parameters in command: '{Context.command.name}'")
        except ValueError:
            raise SyntaxError(f"$editMessage Invalid ID provided in command: '{Context.command.name}'")