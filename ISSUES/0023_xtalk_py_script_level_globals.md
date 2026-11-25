# 0023 xtalk_py: script-level `global` lines were ignored

**Status:** fixed (branch `phase2-thorough` in xtalk_py, waits for the owner's "merge")

## What we saw
The survey of the harvested stacks showed 900 "expression: bad operand" errors (GAD 3/77 clicks working,
3DShufflepuckaroo 0/3). Globals declared at the top of a script, outside any handler, were empty inside its handlers.

## Cause
The interpreter only knew globals declared inside a handler. A `global` line at script level set up the global
but did not make the handlers see it.

## Fix / workaround
The parser records, for each handler, the script-level globals declared ABOVE it; the interpreter and the
translator add them to the handler's frame. A parameter of the same name stays the parameter.

## Discoveries (measured in LiveCode 9.6.3)
- A script-level global reaches only the handlers below its line; above it the name is an unset variable.
- A parameter named like a script global is the parameter; `local g` below `global g` does not compile.
- Numbers keep their full value through arrays, parameters and returns (found on the same hunt: Raycasting_101's
  divide by zero).

## Log
- 25 Nov 2026: found by the survey, measured, fixed; GAD 65/77 and Shufflepuck 3/3 afterwards.
