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

## Cause and fix (Claude Opus, 23 Nov 2026, evening). Fixed on branches `arrow-keys-stay`, waits for his look
Not a pile-up and not an error (nothing in GAME_PLAYER_ERRORS.txt, no BatDuel line in the play record).
Bat Duel was one of two games (with Floppy Flynn) with no `on arrowKey` handler. Every other game has an empty
one. So the arrow went on to the engine's card navigation (`the navigationArrows`, true by default):
**Left = go to the previous card**, so the play card went away at the first press. Down only steps through recent
cards, which is why Down alone never showed it. Holding Down+Left just meant Left was pressed.
- LIB_GAMES 3d606cb: empty `on arrowKey` in Bat Duel and Floppy Flynn.
- LIB_DEV 8232292: the Game Player swallows any arrow a game did not take (it still passes while the console line
  is typed in), so a new game without the handler can't do it again.
- Test: OXT-BEYOND/tests/t71_arrow_keys_stay.txt. A real key can't be pressed with no window (a sent arrowKey
  nobody handles throws), so each arrow is dispatched to the play card and must come back "handled"; then 120
  arrows with frames between and the game must still be on its card, playing, no error. Before the fix:
  Bat Duel and Floppy Flynn FAIL (all four arrows unhandled); after: 10/10 PASS (5 games). t70 BatDuel still PASS.
- Not done: the xRay (xt3d) bench has no arrowKey guard of its own. The game fix covers Bat Duel there too.
  0017 (Genetic Anomaly star map) is a different game and stays open.
Still to do: he holds Down+Left in Bat Duel in the Game Player (XT), then says "merge".

## Closed (23 Nov 2026, evening)
Owner: "Fixed Achieved, I held down as many keys as I have fingers and no crash." Merged to main: LIB_GAMES 3d606cb, LIB_DEV 8232292.
