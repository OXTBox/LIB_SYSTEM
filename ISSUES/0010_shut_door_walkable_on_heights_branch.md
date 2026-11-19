# 0010: a shut door (E07) can be walked through with the heights-floor-ceiling library

Opened 18 Nov 2026 (night, Fable session B). Status: **fixed 19 Nov 2026** on LIB_EDITOR branch `cards-heights` (see the end). Engine 1 (pure xTalk): LIB_BIT's
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

## Fixed (19 Nov 2026, Opus)
The guess was right, and it is not a library bug: the heights branch changed what green means.
Old: green = the roof's thickness over a ceiling (ceiling 1 + green 100 = solid from 1 to 101).
New (CELLMAP_V2.md 3b): the roof is a thin sheet at the ceiling, and green 100 is a block floating at
345-355 hu. So a shut door became a sheet at 1 hu the hero stands on and walks over.
Fix in the cards, the new way to say "solid up to the roof": the door cell is **From Ceiling**
(`[from]` 2) and the yard map names `top 101`, so the door is solid from its ceiling up to 101.
`maps/cards_yard.cellmap` (green layer gone, `[from]` 2 at both doors, `top 101`), E06 and E07
`SetDoor` set from 2 instead of green. LIB_EDITOR `cards-heights` a6de99a (= heights-floor-ceiling +
editor-cards + this fix). All 13 card tests pass against LIB_BIT heights-floor-ceiling (166 checks).
Merge LIB_BIT heights-floor-ceiling and LIB_EDITOR cards-heights together; on LIB_BIT main the
cards-heights doors would be walkable (main has no `[from]`).
