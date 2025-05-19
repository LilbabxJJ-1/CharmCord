# 🧠 CharmCord Architecture

This document outlines how CharmCord interprets and executes string-based commands under the hood. If you’re curious about how `$if`, `$sendMessage`, and the entire logic tree works, this is your map.

---

## 🔁 Core Execution Flow

1. **Command Triggered**

   A user sends a message like:
   ```
   !hello
   ```

2. **CharmCord Matches Command**

   The message triggers a registered command block in:
   ```python
   bot.command(name="hello", code="...")
   ```

3. **String Parsing Begins**

   CharmCord starts evaluating your string-based `code`, looking for functions like:
   ```
   $sendMessage[$channelID; Hello!]
   ```

4. **Bracket Matching & Nesting**

   `find_bracket_pairs()` is used to:
   - Track nesting (`$if[...] $endIf`)
   - Handle embedded functions (`$sendMessage[$channelID; $args[1]]`)
   - Prevent syntax misuse or broken nesting

---

## 🧩 Parsing Chain (Per Function)

Each function goes through the following chain:

1. **`check_args_check()`**
   - Verifies required argument count
   - Sends error if not met

2. **`no_arguments()`**
   - Replaces default markers like `$channelID` or `$authorID`
   - Resolves basic context-only variables

3. **`check_args()`**
   - Substitutes nested values inside arguments
   - Example: `$args[1]` becomes `"hello"`

4. **`is_valid()`**
   - Confirms the function name exists in the loaded function registry

5. **`find_bracket_pairs()`**
   - Recursively parses any embedded commands or logic blocks
   - Example: `$if[1==1] $sendMessage[...] $endIf`

---

## ⚙️ Component Overview

- **`charmclient`**
  The core bot constructor, subclassed from `discord.py` commands.Bot

- **`FunctionHandler`**
  Loads and maps all functions (like `$sendMessage`) dynamically from `functions/`

- **`CharmCordError`**
  Custom error class for context-rich traceback messages

- **`globeHandler`**
  Handles global context like shared bot instance, user/session memory, and variable scope

---

## 🧠 Example Walkthrough

Let’s say the user types:

```txt
$if[1==1]
  $sendMessage[$channelID; Hello World]
$endIf
```

CharmCord will:

1. Match the `$if[...]` and see it returns `True`
2. Enter the logic block
3. See `$sendMessage[...]` inside, parse it
4. Replace `$channelID` with the actual ID
5. Run the function, sending a message

---

## 📚 Internal File Structure

- `CharmCord/functions/` — each `.py` file is a function like `$sendMessage` or `$waitMessage`
- `CharmCord/utils/CharmCord.py` — contains `find_bracket_pairs()` and parser internals
- `CharmCord/globeHandler.py` — stores the shared context (`get_globals`)
- `CharmCord/tools.py` — utility functions used across parsing logic
- `CharmCord/CharmErrorHandling.py` — manages custom errors with context

---

## 🚀 Expansion Friendly

You can add your own functions easily:

1. Create a file in `functions/MyCategory/myFunction.py`
2. Define an `async def myFunction(args, context)` handler
3. Register it via the loader (or let CharmCord detect it dynamically)
4. Use `$myFunction[...]` in your commands!

---

CharmCord is built to be readable, flexible, and fast to extend. Whether you’re a power user or new to bots, it gives you tools to make your commands feel like magic ✨
