# Night work, 14 November (Opus, no Windows screen needed)

Order the owner approved: 1 Amazing Couple on cellmap v2, 2 A-12 harvest analysis, 3 A-16 glossary/procedures.
A wake-up is scheduled for 22:33 (session-only: only if this Claude session is still open).

## 1. Amazing Couple on cellmap v2: DONE (needs the owner's play)
- 12 mazes as files: `LIB_BIT/editor/maps/amazing_couple_mazes/maze_01..12.cellmap` (+ CHECK.txt, all OK). LIB_BIT main.
- `LIB_GAMES/tools/couple_mazes.py` writes and checks them: 0 file = intended maze, 1 beacon reachable,
  2 walking (radius 12) blocked exactly by the cells drawn as walls, tags included, 3 every drawn wall line
  sits on a wall/corridor edge and every such edge is drawn. Proven to catch an invisible wall (negative test).
- The game (LIB_GAMES branch `couple-cellmap`, not merged): walls drawn by CellMap.LevelSegments from the
  file, collision grid from the same file's heights; falls back to the old built maze if a file is missing.
  Played on the real engine as a temporary copy: walls draw, heroes walk the first corridor, 18 fps.
- Not done: the ball-on-the-floor/kick notes (Q/E kicks) from GAME_NOTES; a wall colour per the 11:37 note.

## 2. A-12: next
## 3. A-16: after
