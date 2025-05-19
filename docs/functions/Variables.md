# 🧮 Variable Functions

CharmCord supports local and persistent variables to store and reuse data across commands. Variables can be:
- **Temporary** (in-command only)
- **User-specific**
- **Server-wide**
- **Global** (shared everywhere)

This section covers how to define, access, and modify all variable types in CharmCord.

---

## 🧭 Function Index

| Function | Summary |
|----------|---------|
| [`$let`](#letname-value) | Sets a temporary variable |
| [`$get`](#getname) | Gets a temporary variable |
| [`$setVar`](#setvarname-value) | Sets a global static variable |
| [`$getVar`](#getvarname) | Gets a global static variable |
| [`$setUserVar`](#setuservarname-value-userid) | Sets a variable scoped to a specific user |
| [`$getUserVar`](#getuservarname-userid) | Gets a variable scoped to a user |
| [`$setServerVar`](#setservervarname-value-guildid) | Sets a variable scoped to a server |
| [`$getServerVar`](#getservervarname-guildid) | Gets a server-scoped variable |
| [`$setGlobalUserVar`](#setglobaluservarname-value-userid) | Sets a variable shared globally per user |
| [`$getGlobalUserVar`](#getglobaluservarname-userid) | Gets a globally-shared user variable |
