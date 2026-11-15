# Day work, 15 November (Opus; the owner reviews and tests the BitEditor)

Plan: `NEXT_SESSION_11_15.md`. No windows, no engine_play, no LiveCode window tests today:
Python, git and Spark only.

## Spark
| Time | What |
|---|---|
| 03:31 | pace `10 900` (10 min work, 15 min rest, model unloaded in the rest). 12 new ideas added to `LIB_LLMIN/LIB_SPARK/GAME_IDEAS.txt` ("Maze and rooms batch 1": Lantern Crawl, Two Key Doors, Echo Rescue, Push Block Vault, Ring Arena, Stair Hopper, Glass Corridors, Bargain Hall, Wire Sentries, Falling Floor, Tower Shift, Courier Run). `run_designs.sh` started from WSL; LM Studio answered. |
| 03:36 | batch 1 done (24 requests, 160 s); verdicts in `LIB_SPARK/arcade/REVIEW.md`: Ring Arena as is; Wire Sentries, Courier Run with a small change; Tower Shift dropped for now (needs stacked maps); the rest need changes. Spark's layouts are unusable: levels should come from a Python maze tool with a checker. |
| 03:43 | batch 2 done (24 requests, 181 s; one level table cut off). Every draft invented a Space key: my "no Space key" rule sat in a `#` line Spark never reads. Batch 3 puts the keys in each idea. |
| 03:47 | batch 3 (12 arena and run ideas) started. |
| 03:50 | batch 3 done (24 requests, 232 s). 10 of 12 still invented Space: the real cause was `arcade_prompt.md` itself ("CONTROLS: Only arrow keys and Space", and "what costs a life"). Prompt fixed (LIB_SPARK 30f1117). Verdicts: Echo Chamber as is; Hold The Square, Gate Runner, Lamp Lighter Run with a small change. 14 games across 3 batches are near enough to build. |
| 03:56 | batch 4 started: the first run with the fixed prompt. |
| 03:57 | batch 4 done (24 requests, 232 s): keys right in 12 of 12, so the prompt fix works. Lives still on everything, because the level table's columns were fixed (speed / count / lives / bonus). `run_designs.sh` now takes `| columns: ...` per idea (LIB_SPARK 8d15b81; the old queue builds the same). Verdicts: Pipe Flow Room, Tunnel Digger, Hover Polo with a small change. |
| 04:00 | batch 5 started, each idea with its own columns. |
| 04:05 | batch 5 done (24 requests, 279 s): own columns right in 12 of 12; "cells" read as screen pixels in 5. Sentinel Ring as is; Lockstep Bridge, Herd The Sparks, Bucket Line, Dark Elevator with a small change. Eight two-hero ideas now exist for a PROMPT & GLAZE co-op world. Ideas with own columns no longer get a LAYOUTS picture (LIB_SPARK 6a5a799; every cut-off was there). |
| 04:08 | batch 6 started: columns carry their ranges, no pictures. |
| 04:10 | batch 6 done (24 requests, 119 s, half the time, no cut-offs): every table inside its ranges. Fuse Runner and Rope Swing Gap as is; 8 more with a small change. Running count: 28 games near enough to build. Prompt: LOSE now names what ends a try, or "nothing: moves against par" (LIB_SPARK 8a5eb08). |
| 04:13 | batch 7 started. |
| 04:15 | batch 7 done (24 requests, 120 s): LOSE names a cause in 8 of 12 (was about 2). 3 drafts copied the prompt's example wording into CONTROLS: reworded. Dust Devil Chase, Train Yard Switch, Clock Tower Climb as is; 5 with a small change. **Running count: 36 games near enough to build** (`LIB_SPARK/arcade/REVIEW.md`). |
| 04:35 | batch 8 done after the first real rest (rest 04:16-04:31, work 04:31-04:35, 118 s): keys right in 12 of 12. Hedge Cutter, Lift Bridge, Echo Bats, Lost Lambs as is; 6 with a small change. **Running count: 46.** |
| 04:36 | batch 9 (04:36-04:40, same work period as batch 8): Moth Lamp Maze, Ice Block Tower as is; 5 with a small change. **Running count: 53.** |
| 05:08 | batches 10 and 11 (24 ideas, one run): rest 04:45-05:00, work 05:00-05:08. Keys right 24 of 24; 5 as is, 13 small change. **Running count: 71.** |
| 04:16 | **My mistake: Spark had no rest from 03:31 to 04:15.** Each batch took under 10 minutes and every run restarted the work clock, so the 10-on / 15-off pace never fired. The clock now carries across runs (LIB_SPARK 1c6fa70, tested); batch 8 began with a 15-minute rest, model unloaded, until about 04:31. |
| 03:31 | yesterday's 14 road-trip drafts were uncommitted in LIB_SPARK: committed on main (0fa4c14). |

## Alone
1. **couple_mazes.py --help: DONE.** LIB_GAMES `couple-cellmap` 18c408a (temporary index; main stays
   checked out). Re-run first: all 12 mazes OK, the files came out byte for byte the same.
2. **P5: DONE.** LIB_GLOBALS 1901fc4. The GAD_Globals harvest's per-global records
   (`Defined_Globals`) hold one record under an empty name, so owner/type/content were never saved
   per global; only the 165 comments were. GLOBALS.md now has a GAD column: owner / type / content,
   marked "(rule)" where it is the stack's own default (Application, Integer 0, or Boolean false for
   a name starting with b; so `buildItem`, an item number, shows Boolean). The comments fill the
   purpose where nothing better is known. 164 of 165 are declared in scanned scripts; `myWord` is not.

3. **Globals purposes: DONE.** LIB_GLOBALS 6ea541c: 19 more (gViewLeft/Right, bMouseLook, the
   GenericaProperties outline editor's globals, gHandlerPrefix/Suffix: "on"/"end" spelled in
   pieces so the generating script does not start a handler), census re-run. Skipped as unclear:
   gTop/gLeft/gRight/gBottom (only read and reset in the files I have).
4. **A-50 one test that runs: DONE.** New `tests/run_tests.py` on plain Python (no LiveCode) in
   LIB_MCP (linter), LIB_MOCAP (BVH + forward kinematics), LIB_GENERICA (theme over base),
   LIB_GLOBALS (census), LIB_SCRIPTBLOCKS (handler cutting), LIB_XTJSON (typeless compare),
   LIB_DEV, LIB_SPARK, LIB_SYSTEM, LIB_GAMES (uDead grid helpers), xtalk_py, xt3d: all pass.
   `help_audit.py` has a Test column: **15 of 28 LIB repos have a test that runs, 10 on plain
   Python, 5 need LiveCode** (BIT, DATA, EDITOR, MAP, TRACE). LIB_UPBGE has no test (its one tool
   needs Blender).
   **My mistake:** before reading which tests need LiveCode I ran the four old LIB_* tests (BIT,
   DATA, MAP, TRACE: all passed), and they start the LIB_MCP standalone `xt3d_MCP.exe` on
   Windows, which today's plan forbids. My attempt to close it was refused by the permission
   check, so it may still be running: close it from Task Manager, or `! taskkill.exe /IM xt3d_MCP.exe /F`.
5. **Hexes_but_bad_Offsets: DONE.** LIB_MAP 330c8fe: `docs/HEX_OFFSETS.md` and `python/hexgrid.py`.
   Three faults: the repeating tile is 1.5 s wide (must be 3 s with a whole hex plus four corner
   quarters), paintTarget shifts odd rows by 0.75 s (must be 1.5 s, with columns 3 s apart), and
   `tHextRect` (typo) moves the snapshot sideways only. The check fails the old numbers, passes the fix.
6. **Amazing Couple ball: WRITTEN, NOT COMPILED OR PLAYED.** LIB_GAMES `couple-cellmap` 0474a35.
   The first ball rests on the floor, whole, until a hero touches it; Q kicks it angled right
   (from its left side), E angled left, from the hands or at your feet. That needed E, so
   **pick up / straight kick moved from E to F** (your call: say if you want another key).
   Linted clean. Waits for a compile check and your play.
   Before merging couple-cellmap: delete the untracked `LIB_GAMES/tools/couple_mazes.py` in the
   main checkout (the older copy of the branch's file; git will refuse the merge over it).

## Owner's feedback
- 03:25 GLOBALS.md ("these lists are great"): nothing to fix.
- 03:50 your Fuel Line note (14 Nov, 8:09 PM, "too much damn traffic") had no fix yet. LIB_GAMES
  `spark-roadtrip` d2f143e: cars are 30% of what spawns (was 45%), fuel cans 45% (was 30%, so fuel
  is no harder to find), oil 25% as before; 35% of cars swerve at you (was 50%). Linted, not played.
- Your Genetic Anomaly note (14 Nov, 8:13 PM: advancement economy, big scrolling/zooming map,
  turn based with End Turn) is a design job, not a quick fix: it waits for you to say go.

## Your notes in MAIN_UI_REUSE.md (04:17)
- Your five answers are now **A-84 to A-88** in TODO.md (LIB_SYSTEM 27f8b43); your edits to the file
  committed as they are (LIB_ig3d 8ca871b). A-84, A-86, A-87 need LiveCode: not today.
- **A-85 done (the Python part): .wtf animations DO convert to BVH**, so per your condition it goes
  forward. Only 10 of the 775 distinct .wtf files have animations (the DeadDays models; the
  others are copies). Each has its own rig. Format decoded from officer.wtf's geometry: each bone's
  pair is (its joint vertex, parent + 1), and bone 0 is the whole model turning about its feet.
  `LIB_MOCAP/tools/wtf_anim.py` wrote **58 BVH** into `LIB_BVH/iGame3D_DeadDays` (officer, human,
  zombietobi, robothead, robotheadgun). Checked without a screen: rest pose exact, bone lengths
  constant in every frame, walks keep the feet on the ground, Die ends with the head on the floor.
  **Not checked:** the rotation order (I used the one wif.py fitted for iGame3D's tables). One look
  in a BVH viewer will tell. LIB_MOCAP 1a7cb38, LIB_BVH (local only).
- A-88 explained, since you asked: GameOverViewData was your 2007 game-design-document form, with
  tabs Overview, Philosophy, Goals, World Layout, Scheduled, Sounds, Music, Weapons, Camera. A-88
  would turn those tabs into a blank outline (headings and a one-line prompt each) that every new
  game starts from: PROMPT & GLAZE's design doc, and a step in LIB_HOWTO ("write your design doc").

## Spark's next job: procedural entities (owner, 05:1x: "Yes!")
Answered by the owner: Spark now designs **entities** instead of more game designs.
- Spark writes a RECIPE: parts (box, prism, pyramid, sphere, lathe, loft, line, tri) with sizes,
  positions and turns; words and numbers only. `LIB_SPARK/entities/entity.py` checks it (size,
  every part joined, base on the ground, left/right mirror, at most 160 edges), draws a top and a
  side view in characters, and writes the Vibecode3D `Ent.<Name>Mesh` function (the same calls
  the games use). A failed recipe goes back to Spark once with the checker's faults.
- Calibrated on the demo's sail boat: as a recipe it passes with 31 edges (its comment says 31)
  and the generated function makes the same calls as the hand-written one.
- Pilot queue (`entities/entities.tsv`): Cable Car, Ice Fishing Hut, Hover Polo Craft, Sentry
  Drone, Dock Crane, Lighthouse, Penguin, Robot Vacuum, Clock Gear, Hot Air Balloon, Train
  Engine, Two Key Door. Started 05:22 (rest until about 05:37, then work). LIB_SPARK a260cc6.
- The game-design batch 12/13 was stopped after 4 of its 24 ideas; the other 20 stay queued.
- Not done: entity "stacks" (one generic stack reading recipe files) need LiveCode.

## Question for you (answered: entities)
Spark's game-design format is now settled and **46 designs are near enough to build**, more than
we can build soon. More batches add more of the same. Options: (a) keep making designs all day
(the plan; default), (b) switch Spark to another job, e.g. the HOWTO step words or the 2008
manifest drafts, (c) you pick 4 to 6 designs and I write their level checkers next.

## Your clarifications to Fable's globals questions (05:03)
- The four Fable skipped now have purposes in `LIB_GLOBALS/PURPOSES.md`, in your words:
  gGlobalList (the globals list.script.globals finds), gEditorState (one undo/history state of the
  bitmap animation editor), gGridSize (cells per row; "can be scrapped"), tArray (a temp array made
  global while bug hunting: drop the declaration and run).
- Your prefixes are in the census now (LIB_GLOBALS ba756c9): `bName` is a boolean global and stays
  as it is ("ok (b)", 37 of them no longer get a rename proposal); a `t`/`p` name declared global is
  marked "leftover?" with "drop the global?" (18, tArray among them). 416 of 498 globals now follow
  your naming; 82 still get a proposal; name clashes fell from 6 to 2. The prefixes are written
  in LIB_GLOBALS/README.md and in my memory, so I use them in xTalk I write.
- Your file moved to `LIB_LLMOUT/Read/LIB_GLOBALS/`.
