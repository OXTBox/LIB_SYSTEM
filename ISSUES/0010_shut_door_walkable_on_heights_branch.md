# 0010: a shut door (E07) can be walked through with the heights-floor-ceiling library

Opened 18 Nov 2026 (night, Fable session B). Status: **open**. Engine 1 (pure xTalk): LIB_BIT's
`lib_cellmap` walker, used by the LIB_EDITOR cards.

## What happens
E07 A Pad Opens A Door shuts a door by setting its cell to ceiling 1 (= its floor 1) and green 100:
"solid to the roof". With LIB_BIT on **main** the hero stops at the shut door. With LIB_BIT on
**heights-floor-ceiling** (the branch waiting for the owner's test) the hero walks straight
through it.

## How to see it
`python3 -I ~/projects/OXT-BEYOND/tests/oxt_headless.py ~/projects/LIB_EDITOR/tests/e07_headless.txt`
(with the E07 test from branch `editor-cards`, whose numbers were corrected tonight):
- LIB_BIT on main: 13 of 13 pass.
- LIB_BIT on heights-floor-ceiling: 12 of 13; "walking back west, the shut door stops the hero"
  gets `7,8` (through the door) instead of `9,8`.

## Guess (not checked)
Commit 4220248 "From Floor / From Ceiling for the floating blue block" changed how a column's
levels are built; a cell whose ceiling is at its ground may no longer count as solid. Check
`cmLevels` / `CellMap.Column` on that branch with floor 1, ceiling 1, green 100.

## Before merging heights-floor-ceiling
Run the LIB_EDITOR card tests (`tests/e*_headless.txt`) against it; E06/E07 doors depend on this rule.
