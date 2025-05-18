# 🧠 Logic, Math & Utility Functions

These functions let you handle common scripting needs within CharmCord — from basic math to logical conditionals, JSON parsing, text manipulation, and more.

They’re especially helpful for enhancing your `$if` conditions, performing operations, or managing dynamic values during command execution.

---

## 🧭 Function Index

| Function | Summary |
|----------|---------|
| [`$console`](#consoletext) | Prints text to the console (for debugging) |
| [`$contains`](#containstext-search) | Checks if a string contains another string |
| [`$count`](#counttext-char) | Counts how many times a character appears in a string |
| [`$divide`](#dividenum1-num2) | Divides two numbers |
| [`$multi`](#multinum1-num2) | Multiplies two numbers |
| [`$sum`](#sumnum1-num2) | Adds two numbers |
| [`$sub`](#subnum1-num2) | Subtracts two numbers |
| [`$random`](#randommin-max) | Returns a random number between min and max |
| [`$lower`](#lowertext) | Converts a string to lowercase |
| [`$getJson`](#getjsonurl-key) | Gets a value from a JSON response |
| [`$pyEval`](#pyevalcode) | Runs a Python one-liner (caution!) |
| [`$wait`](#waitseconds) | Delays command execution |
| [`$if`](#ifcondition) | Executes if the condition is true |
| [`$elif`](#elifcondition) | Executes if previous `$if` was false and this condition is true |
| [`$onlyIf`](#onlyifcondition-error) | Halts command if condition is false |