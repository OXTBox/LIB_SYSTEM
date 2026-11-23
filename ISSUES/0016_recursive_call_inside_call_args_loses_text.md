# 0016 A recursive function called inside another call's brackets lost the caller's text (fixed by a workaround, 22 Nov 2026)

**Found by:** Claude (Opus), testing LIB_EMITTERS in OXT-Beyond 0.2.7 through the MCP bridge.

## What happened
`emitJagLine` (a lightning bolt, LIB_EMITTERS/livecode/lib_emitters.livecodescript) adds its branches with

    put Emit.Join(tOut, emitJagLine(...branch...)) into tOut

where the inner `emitJagLine` call recurses again (branches of branches). With branches two deep the
**main bolt vanished**: 32 segments, depth 2 gave 23 lines with neither end of the bolt in them, so a
lightning strike started half way down the sky. Depth 1 was fine. xtalk_py's interpreter gave the
right answer, so its tests (58/58) did not see it.

| segments, depth | lines before | main bolt there? | lines after the fix |
|---|---|---|---|
| 8, 2 | 15 | no | 25 |
| 32, 2 | 23 | no | 213 |
| 32, 1 | 123 | yes | 123 |

## Workaround (in)
Call the recursive function on its own line, then join:

    put emitJagLine(...) into tBranch
    put Emit.Join(tOut, tBranch) into tOut

## Rule
In xTalk on OXT-Beyond, never call a **recursive** function inside the argument list of another call
that also takes the caller's local; put its result in a variable first. Not yet narrowed to the
smallest case (is it recursion, or any nested call of the same handler?): open.
