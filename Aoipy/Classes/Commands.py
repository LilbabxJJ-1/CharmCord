from Aoipy.tools import findBracketPairs

########################################
#              COMMANDS                #
########################################


class Commands:
    # Global variables

    def command(self, Name, Code):
        # Define command function dynamically
        from Aoipy.Classes.AoiPyClient import bots
        @bots.command(name=Name)
        async def go(ctx, *args, Code=Code):
            from Aoipy.Classes.AoiPyClient import TotalFuncs
            Context = ctx
            if '$args' in Code:
                while "$args" in str(Code):
                    count = 0
                    end = None
                    balance = 0
                    start = Code.index("$args") + 5
                    look = Code[start:len(Code)]
                    for i in look:
                        if i == "[":
                            start = count
                            count += 1
                            balance += 1
                            continue
                        if i == "]":
                            end = count
                            balance -= 1
                        count += 1
                        if balance == 0 and start is not None and end is not None:
                            try:
                                # Replace $args with arguments
                                Code = str(Code).replace(f"$args[{look[start + 1:end]}]", args[int(look[start + 1:end]) - 1])
                                break
                            except IndexError:
                                raise SyntaxError(F"$args[{int(look[start + 1:end])}] Not Provided")

            if "$argCheck" in Code:
                if Code.count("$argCheck") > 1:
                    raise Exception("Too many $argCheck in a single command | Max is 1!")
                start = Code.index("$argCheck[") + 10
                area = Code[start:]
                try:
                    argTotal = area[:area.index(";")]
                    warning = area[area.index(";") + 1:area.index("]")]
                    if len(args) != int(argTotal):
                        await Context.channel.send(warning)
                        return
                    Code = Code.replace(f"$argCheck[{argTotal}{area[area.index(';'):area.index(']')]}]\n", "")
                except:
                    raise SyntaxError("Not enough arguments in $argCheck!")

            await findBracketPairs(Code, TotalFuncs, Context)