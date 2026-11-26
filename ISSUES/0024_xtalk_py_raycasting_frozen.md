# 0024 xtalk_py: Raycasting_101 answered one key, then froze

**Status:** fixed (branch `fast-translate` in xtalk_py, waits for the owner's "merge")

## What we saw
The owner's window: Raycasting_101 "responded once to a keypress and locked up, the mouse never affected anything",
CPU climbing.

## Cause
Two together:
1. Speed: the interpreter needed 85-125 ms for one GameLoop while walking (LiveCode's budget is 50 ms).
2. The window ran every due `send ... in` message before drawing. GameLoop re-sends itself in
   `max(1, 50 - timeTaken)` ms, so after a slow step it was due again at once, and one frame ran dozens of steps
   back to back: no drawing, no keys read.

## Fix
- The window runs at most 20 ms of messages a frame; the rest wait for the next frame.
- Stack scripts are translated to Python before they run (xtalk/fastgen.py): handler variables as Python
  variables, numbers as floats. GameLoop: 12 ms. 100 scripted steps give the same results as the interpreter.
  `XTALK_INTERP=1` brings back the interpreted path.

## Discoveries (measured in LiveCode 9.6.3)
- Numbers compare at their full value with a tolerance of ~10 steps of a double: `(1/3) = 0.333333` is false
  (we said true: we compared the 6-decimal text), `0.1 + 0.2 = 0.3` true.
- numberFormat applies when a number becomes text, not when it is computed.

## Log
- 25 Nov 2026: profiled, fixed, measured; still to see on his screen (and whether WSL passes the grabbed mouse).
