# 0020 Bat Duel quits on the arrow keys (open, 22 Nov 2026; CONFIRMED by the owner 23 Nov)

**Found by:** play test 0001 (21 Nov 2026), from the owner's notes; logged by Claude (Fable), not yet looked into.

## What happened
The game ended when the tester pressed arrow keys (the note has a question mark: not confirmed).

## Next
p1-04.
Plan: LIB_DEV/PriorityTube/PLAYTEST_0001_PLAN.md

## Confirmed (owner, 23 Nov 2026, morning)
Holding Down + Left together crashed Bat Duel in about a tenth of a second (Game Player, XT engine).
So it is not "quits": it is a crash, and very fast, faster than a queue could pile up in 0.1 s.
Likely the same family as 0017 (held keys), but the speed says look for an error first.
Bat Duel reads `the keysDown` once a frame (its own function near line 81; Game.OnUpdate line 88, 65364 = Down);
no keyDown/arrowKey handler of its own. Owner moved this to the top of the priority (before n-15396035).
Start: read the Game Player error log LIB_LLMIN/LIB_DEV/GAME_PLAYER_ERRORS.txt (newest lines) and the play record
(an "open" BatDuel run = no quit line), then the whole Game.OnUpdate with Down+Left both in tKeys
(two arrows at once: a diagonal path, e.g. a divide by zero, a normalize of 0, a bat moved out of range).
Then the 0017 guard design if it is the key repeats. Test: send both keys with no window (headless runner).
