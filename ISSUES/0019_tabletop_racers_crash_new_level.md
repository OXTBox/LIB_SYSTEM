# 0019 Tabletop Racers: a crash seen at a new level (not confirmed) (not reproduced, 23 Nov 2026)

**Found by:** play test 0001 (21 Nov 2026), from the owner's notes; logged by Claude (Fable), not yet looked into.

## What happened
The owner's note: 'Seems there was a crash there on a new level.' No error text.

## Next
p1-14: play through level changes with no window and catch the error before the grid start is built.
Plan: LIB_DEV/PriorityTube/PLAYTEST_0001_PLAN.md

## 23 Nov 2026 (Opus, p1-14): not reproduced
Played headless in the real Game Player, both engines (OXT-BEYOND/tests/t75_tabletop_grid.txt): all five
tables changed through the loading screen, off the table again and again, game over and Space, a long
wait while the rivals race: no error anywhere. Likely the "crash" was the hard start itself (racing from
the first frame, clutter right ahead). The grid start (pull up, 3 2 1 GO) is on LIB_GAMES branch
`tabletop-grid`. Close when the owner has played it and seen nothing.
