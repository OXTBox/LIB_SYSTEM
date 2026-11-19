# 0006: four headless tests count the wrong number after the 18 Nov merge

**Status:** open
**Opened:** 18 Nov 2026 · **Area:** OXT-BEYOND/tests

## What we saw (every branch merged to main, 18 Nov evening, OXT-Beyond engine)
- t46 suggest: counts one more call than it expects (84, wants 83; Entity 21, wants 20; setters 9, wants 8). The contract got a new Entity setter (Entity.SetColor) and the test was not told.
- t27 launcher: 51 titles, wants 52; Tools 4, wants 5 (the test expects iGame3D XT on this PC).
- t17 inspector: "clips listed (1000+)" false: probably the local BVH library is not where the test looks.
- t48 LIB_INPUT: "profiles listed" differs.
- t39: see 0005.

Fixed the same evening: t22 and t28 stopped at Camera.Reset / Mesh.Lathe because their stand-in engine lacked the Rename Day names; they now add LIB_ig3d's alias file (as t45 does). The real engine already has them. 20 and 18 checks pass on both engines.

## Cause / Fix
Not looked at yet: probably the tests' expected numbers need updating, not the code.
