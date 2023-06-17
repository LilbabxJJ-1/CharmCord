from ast import literal_eval

import CharmCord


class SlashCommands:
    def slashCommand(self, name, code, args, description=""):
        from .CharmCord import bots
        global codes
        global argss
        global parem
        codes = code
        argss = args

        function_definition = f"""@bots.slash_command(name=name, description=description)
async def go(ctx, {', '.join(args)}):
                global codes
                global argss
                from CharmCord.Classes.CharmClient import TotalFuncs
                Context = ctx
                new = []
                for i in args:
                    new.append(eval(i))
                finalCode = await noArguments(code, TotalFuncs, Context)
                finalCode = slashArgs(new, finalCode)
                await findBracketPairs(finalCode, TotalFuncs, Context)
                
        """
        exec_globals = {
            'bots': bots,
            'name': name,
            'description': description,
            'codes': codes,
            'argss': argss,
            'TotalFuncs': __import__("CharmCord.Classes.CharmCord", fromlist=["TotalFuncs"]).TotalFuncs,
            'from': __builtins__.get('from'),
            'await': __builtins__.get('await'),
            'slashArgs': __import__('CharmCord.tools', fromlist=['slashArgs']).slashArgs,
            'findBracketPairs': __import__('CharmCord.tools', fromlist=['findBracketPairs']).findBracketPairs,
            'noArguments': __import__('CharmCord.tools', fromlist=['noArguments']).noArguments
        }

        # Import required module
        from CharmCord.Classes.CharmCord import TotalFuncs
        exec(function_definition, exec_globals)
