# 0025 xtalk_py: uDead through the xt3d host showed nothing, then hung in hiding mode 1

**Status:** fixed (branch `phase3-xt3d` in xtalk_py, waits for the owner's "merge")

## What we saw
uDead CullTest running in the Python runtime through the unchanged xt3d testbench host (Phase 3):
1. A black view with "objects 42": every object at the map corner, behind the camera.
2. Before that, a game that never stepped: the loading screen's gLoadingBusy stayed true.
3. Pressing 1 (hiding mode 1) hung the window for good.

## Cause
Three LiveCode rules we had wrong (each measured in LiveCode 9.6.3, LIVECODE_FACTS 25 Nov):
1. Array keys ignore case while the caseSensitive is false: the engine stores `gObjectTransforms[o]["X"]` and
   reads `["x"]`. Ours had exact keys, so every position read as empty (0).
2. The itemDelimiter (also lineDelimiter, numberFormat, caseSensitive) belongs to the handler. The host's
   xbFindAbove leaves it at "/"; ours kept that for every later handler, so `item 1 of sRect` in the loading
   screen failed inside a try, half-way through Loading.Begin.
3. `delete item 1 of "3,"` is empty in LiveCode; ours left ",", so the host's xbGameFill queue never emptied.

## Fix
values.XtArray (case-insensitive keys, first spelling kept); Interp.invoke gives each handler its own
itemDel / lineDel / numberFormat / caseSensitive; the delete takes the delimiter after the item.
tests/test_measured.py keeps all three (27 checks, three run modes).
