# Next session prompt (2026-11-15): Spark on games, Claude alone while the owner reviews

Paste everything below the line into a fresh Claude Code session in `~/projects`.

---

Read LIB_SYSTEM/LIB_ALPHA.md, STATUS.md and LIB_SYSTEM/NIGHT_WORK_11_14.md first. Today the owner
is going through the review list (LIB_LLMOUT/FOR_REVIEW.txt) and testing the BitEditor. Don't
use his screen or windows: no engine_play.sh, no LiveCode window tests, no LIB_MCP standalone.
Python, git and Spark only. Commit as you go (foundation work on main, games on their own
branches, never merge a game), add every file you make with
`python3 -I ~/projects/LIB_DEV/tools/for_review.py add <path> "work done"`, and keep a progress
file `LIB_SYSTEM/DAY_WORK_11_15.md`.

## 1. Spark on games: 10 minutes of work, then a 15-minute break, all day

- Pace: write `10 900` into `~/projects/LIB_SPARK/arcade/pace.txt` (10 work minutes, 900 s rest;
  the runner unloads the model during any rest of 2 minutes or more, and reads this file live).
- Queue: all 25 ideas in `~/projects/LIB_LLMIN/LIB_SPARK/GAME_IDEAS.txt` (the road-trip set) are
  done. Add 12 new ORIGINAL ideas, one line each, `Title | what happens` (2-4 sentences: view,
  goal, the rule that makes it a game, how a level gets harder). Genres, not copies of existing
  games. Lean toward what Vibecode3D draws well (wireframe vectors, top-down, side view, behind
  the car) and toward PROMPT & GLAZE (see memory prompt-glaze.md and ~/projects/PROMPT_GLAZE):
  maze crawls, rescue runs, small arenas, puzzle rooms that fit cellmap v2 mazes.
- Start: run `bash ~/projects/LIB_SPARK/run_designs.sh` in the background yourself. It writes a
  concept and a 5-level table per idea into `LIB_SPARK/arcade/out/` and skips done ideas. If it
  can't reach LM Studio from WSL, ask the owner to double-click `START_SPARK_GAME_DESIGNS.bat` (in
  LIB_SPARK) once. Spark writes words and numbers only, never scripts (LIB_SPARK/README.md).
- While it runs: after each batch, read the new drafts and give each one a verdict in a new section
  of `LIB_SPARK/arcade/REVIEW.md`: buildable as is / needs a change (say which) / drop. Do NOT
  write the games yet; the owner picks which ones to build.
- When the queue runs dry, write the next 12 ideas and keep going. Log each run's numbers in the
  LIB_SPARK/README.md table (requests, model time, speed).

## 2. Alone, in this order, between Spark batches

1. **couple_mazes.py --help** on LIB_GAMES branch `couple-cellmap` (A-50's last tool). The owner has
   main checked out, so commit with a temporary GIT_INDEX_FILE (read-tree the branch,
   hash-object -w, update-index --cacheinfo, write-tree, commit-tree -p, update-ref). Re-run
   `python3 -I tools/couple_mazes.py` first; all 12 mazes must still pass.
2. **P5:** `LIB_GLOBALS/tools/globals_census.py` takes `owner / type / content` from the GAD_Globals
   harvest (`XTJSON/batch/GAD_Globals/stack_GAD_Globals.json`, custom property `GAD_Globals`, 165
   globals) into globals.json and GLOBALS.md. Re-run and check.
3. **Globals purposes:** for the most-used globals with no purpose in GLOBALS.md, read where they
   are used and write `gName - what it holds and who sets it` into LIB_GLOBALS/PURPOSES.md (only
   what the code shows). Re-run the census.
4. **A-50 "one test that runs":** list which LIB_* repos have a test that runs
   (`tests/run_tests.py` or similar); for the ones with Python tools and no test, add one small
   test that runs without LiveCode. Add the count to `LIB_DEV/tools/help_audit.py`'s table.
5. **Hexes_but_bad_Offsets:** read its 404-line hex script
   (`XTJSON/batch/Hexes_but_bad_Offsets/scripts/`), find the offset fault, write a short note with
   the fix for LIB_MAP (a hex-grid layout in Python with a check that tiles meet edge to edge).
6. **Amazing Couple game notes** (ball resting on the floor; Q/E angled kicks): write the code on
   branch `couple-cellmap` only, compile-check with `~/projects/LIB_MCP/tools/lcmcp compile` if that
   runs without a window, otherwise leave a note that it waits for a test. No live play tests today.

## 3. Read the owner's feedback

Every hour or so: `python3 -I ~/projects/LIB_DEV/tools/for_review.py feedback` and
`LIB_LLMIN/LIB_GAMES/GAME_NOTES.txt`. Fix what he flags first (small fixes on the right branch),
answer in DAY_WORK_11_15.md. He may merge branches as he reviews: run `git status` before
touching any repo.
