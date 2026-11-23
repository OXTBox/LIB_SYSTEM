# 0017 Two arrow keys held on the Genetic Anomaly star map crash the XT engine (key presses pile up as pending messages) (closed 23 Nov 2026; opened 22 Nov)

**Found by:** play test 0001 (21 Nov 2026), from the owner's notes; logged by Claude (Fable), not yet looked into.

## What happened
Holding two arrow keys to scroll the Genetic Anomaly star map crashed Vibecode3D (the pure xTalk engine).
The owner's reading: key presses pile up in the message queue (the pendingMessages kind of trouble).

## Next
p1-05: one guard in the engine or Game Player (read keys once a frame, drop repeats still waiting), a held-key test with no window, then every game that reads keys by message (game_scan.py).
Plan: LIB_DEV/PriorityTube/PLAYTEST_0001_PLAN.md

## Design of the fix (Fable, 22 Nov 2026; for Opus, bubble p1-05). Not tested: read as a reasoned guess
What the code shows:
- Genetic Anomaly does NOT move the map from key messages. It reads `the keysDown` once a frame
  (`GA.Keys`). So the game is not the one queueing work.
- A held key still makes Windows send repeats: a stream of `rawKeyDown` (and `keyDown` / `arrowKey`)
  messages, doubled with two keys. Each one travels the whole path: front scripts (GameNotes), the
  card, the Game Player's `rawKeyDown`, the engine. Nothing uses them, but all are delivered.
- `Player.Tick` asks for the next frame in `max(1, wait - time spent)` ms. On a heavy picture (the star
  map) the frame overruns, so the next tick is due in 1 ms: the engine is never idle, and the key
  repeats arrive faster than they are worked off. That is the pile.
- An `arrowKey` nobody handles also reaches the engine's own card navigation (`the navigationArrows`).

Step 0, before any fix: reproduce it. In a real window hold two arrows on the star map for 30 s and log,
once a second, the number of lines of `the pendingMessages` and the frame time. With no window: send
60 `rawKeyDown` a second at the player while it runs. Keep the error text; "crash" may be a recursion
limit, a memory climb or a hang, and the fix differs.

The guard, three parts, all in the Game Player (and the same in the xt3d bench), no game changed:
1. **Repeats stop at the door.** A front script put in first (before GameNotes) keeps the set of keys
   that are down. A `rawKeyDown` for a key already in the set is a repeat: swallow it (no pass).
   `rawKeyUp` takes the key out. First presses pass as today, so Escape, F4, the notes key and typing
   in the console all work. The set is emptied on `suspend` (a key-up can be lost when the window
   loses focus). While the console line or the notes box has the keyboard, the guard is off (typing
   needs repeats).
2. **Room to breathe.** The least wait before the next tick is 4 ms, not 1, and only one `Player.Tick`
   may ever be waiting: cancel `sTickMsg` before sending a new one.
3. **`set the navigationArrows to false`** while a game plays (put back on stop).

Do not use `flushEvents("keyDown")` every frame: it would also throw away a real first press of
Escape. Look up `flushEvents` in the OXT-Beyond dictionary before trusting it at all.

Games that DO act on repeating key messages (the game scan, p1-01, lists them: `arrowKey`, `keyDown`,
`rawKeyDown` handlers in a game script) would stop repeating under part 1. For each: move it to
`the keysDown` once a frame, or let it ask for repeats (`uKeyRepeats` true on the card).

Done when: two arrows held 30 s on the star map, both engines: no crash, pending messages stay under
10, fps within 10% of no keys held, Escape still pauses in one frame, F4 and the notes key work. Keep
it as a test (OXT-BEYOND/tests) so it never comes back.

## Looked into (Claude Opus, 23 Nov 2026, night). Fixed on LIB_GAD branch `arrow-keys-stay`, waits for his look
Same cause as 0020 (Bat Duel): Genetic Anomaly had no `on arrowKey` handler (only a `rawKeyDown` for the wheel),
so Left reached the engine's card navigation = previous card. Not a pile-up; the guard design above is not needed.
- Already covered in the Game Player since LIB_DEV 8232292 (it swallows arrows no game took): the arrow test
  passed for Genetic Anomaly before any change.
- LIB_GAD arrow-keys-stay: empty `on arrowKey` in the game itself (covers the xRay bench too).
- Test OXT-BEYOND/tests/t71_arrow_keys_stay.txt now runs GeneticAnomaly too (copied from LIB_GAD into LIB_GAMES
  for the run, deleted after): 12/12 PASS both engines. t14 passes; t15 stops at Camera.Reset as before (ISSUES 0011).
Still to do: he holds two arrows on the star map, then says "merge".

## Closed (23 Nov 2026, night)
Owner, on the V: Library's Game Player: "Maximum Key mashing is crash free". Merged to main: LIB_GAD d4fce48;
the new game file copied onto V: (vibeapps/common/Genetic Anomaly).
