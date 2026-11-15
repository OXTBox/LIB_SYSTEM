# STATUS

Saturday, November 14, 2026, afternoon. Rewritten by Claude (Fable) at the end of the window
Opus briefed (`Next_Steps_With_Claude/previous_steps/FABLE_BRIEF_11_14_2026.md`). Next plan:
`Next_Steps_With_Claude/WHEN_WE_RESUME_AFTER_FABLE_11_14_2026.md`.

## Done 15 November (Opus, TTRPG Studio iteration 1, from LIB_TTRPG/OPUS_BUILD.md)
Stack built (LIB_TTRPG branch `ttrpg-studio-1`; copy in LIB_TEST branch `ttrpg-studio-1`, README section 4).
Owner's test ALL PASS through the stack's engine with real models (gemma alone; gemma + lfm3-omni-2b;
Voices fallback); headless self / mock / UI tests pass. Tuning in `LIB_TTRPG/TUNING.md`: a pressed-out
secret is now shown by code; qwen-7B makes better scenes but qwen + a 2B filled memory to 95%; 13B is
out of reach. All models unloaded. **Waiting:** the owner opens the window (not yet seen on a screen).
Not done: step 9 (old studio's world code), by design "later".
Later the same day: skills drive the play (18 skills, skill buttons), self-play by a model, the owner played
the terminal version ("That was great!"). **Resume from `LIB_TTRPG/NEXT.md`.**

## Running (no Claude usage)
| What | Where | State |
|---|---|---|
| Nothing started by this window | - | `LIB_DEV/tools/wait_for_tell.sh` ends with the session: the next session starts it again |
| Spark: iGame3D 2008 manifest | Spark's own window | stopped since 13 Nov (LM Studio was down); restart when wanted |

## Done today (14 November)
**Opus, night (no screen needed):** Amazing Couple mazes as 12 checked cellmap files, the game draws
and collides from them (LIB_GAMES branch `couple-cellmap`); A-12 CLIP/DND/Enochian analysis; A-15 review
re-run; A-16 GLOSSARY.md + PROCEDURES.md in LIB_ig3d. Details: `NIGHT_WORK_11_14.md`.
**Merged to main (owner: "merge everything that is not a game"):** LIB_DEV `game-browser`, LIB_BIT
`1bit-to-3d`; LIB_BIN, LIB_BUILD, LIB_GENERICA, LIB_SCRIPTBLOCKS, LIB_SYSTEM, LIB_TEST, LIB_UPBGE got
a main from their only branch. Still open: LIB_GAMES `spark-roadtrip` (games).
**Opus, evening: Spark road trip, all 15 vehicle games** on LIB_GAMES branch `spark-roadtrip`
(Neon Drift Wastes, Dodge Tunnel, Grid Sprint, Coast Road, Bounce Rally, Interceptor Run, Fuel Line,
Fare Dash, Block City Hustle, Tabletop Racers, Wreck Ring, Light Trail Arena, Crater Crawler, Ramp
Rider, Squad Buggy). Each played on the real engine with `LIB_GAMES/tools/engine_play.sh` and
snapped; all on FOR_REVIEW with caveats (feel and tuning need your hands; test keys only).
**Fable window (architecture):**
- **cellmap v2**, the hub between the editor and the engines: `LIB_BIT/editor/CELLMAP_V2.md`.
  Five heights a cell (floor and ceiling greys 0-255 where 100 = a full hallway; red digs down,
  green builds up, blue floats a slab), links, objects, stacked maps; one rule set turns a map into
  a level (line segments by class, walking by `CellMap.Walk`) for Vibecode3D and xt3d.
  Python and LiveCode libraries give identical answers (tested); version 1 files still read.
- **BitEditor Heights tab** (the owner's floor / ceiling colour paint mode): Floor and Ceiling
  tools, grey / red / green / blue swatches, pick, Blocks view. Tested headless with pixels read
  back; not yet seen on a screen.
- **Sample map** `maps/wizard_pool.cellmap`: swimming pool, raised dais, wizard's tower, clouds,
  a maze corner, a screen of glyphs laid flat to walk on.
- **E13 Walk The Map** (`LIB_EDITOR/examples`): the sample as a 3D wire level; Amazing Couple's
  hero walks the pool steps, the dais, the tower, teleports to the clouds, falls, crosses the
  roofed maze. 11 headless scenes pass; 30 frames a second in the real Vibecode3D.
- **Merge plan** `Next_Steps_With_Claude/MERGE_PLAN_11_14_2026.md`: 22 branches in 8
  repositories, all tried, all merge clean; the order; the loose files to clear first.
- Commits: LIB_BIT `1bit-to-3d` (+5 today), LIB_EDITOR `main` (+1), LIB_SYSTEM `lib-system-draft1`.

**Opus, morning (from its brief):** LIB_HOWTO outline finished (18 topics, 92 steps); LIB_EDITOR
started (plan from Forge / Anvil / Tomb Raider editor manuals, E01, E02); BitEditor with the
Aquarius font, 1bit and Cells tabs, ghost preview; LIB_THEME; LIB_DEV Status_Browser and the
review list; Amazing Couple's ball (kick and hold).

Confirmed by the owner (14 Nov): cellmap v2's five numbers a cell; the Heights tab opens showing glyphs ("so the user doesn't get lost between general design and detail design"), Blocks stays an optional button.

**Merged on the owner's word (14 Nov, 13:05):** every branch in LIB_GAMES (12), LIB_XTJSON, LIB_ig3d,
LIB_SPARK and xt3d; Vibecode3D's XTJSON deletions committed. Details at the top of
`Next_Steps_With_Claude/MERGE_PLAN_11_14_2026.md`. Only LIB_BIT `1bit-to-3d` is still open (the
editor is not tested yet). The owner's play test "went great, really lovely".
**Spark:** a game-design run finished at 13:05: 14 new designs in `LIB_SPARK/arcade/out/` (124 Grid
Sprint ... 945 Tabletop Racers) wait for a review and scripts (Opus).

## Waiting on the owner (with the default I'll take)
| ID | Question | Default |
|---|---|---|
| F-3 | Test the BitEditor (Heights tab). LIB_BIT `1bit-to-3d` merged to main 14 Nov (owner: "merge everything that is not a game"); two uncommitted editor script edits from 13:31 ride along, unreviewed | they stay uncommitted until you look |
| R-2 | Play Amazing Couple on branch `couple-cellmap` (mazes from files: any invisible walls left?); merge if good | waits unmerged |
| R-1 | Play the 15 road-trip games (LIB_GAMES `spark-roadtrip`); merge when happy | the branch waits unmerged |
| O-1 | Correct LIB_ALPHA / OPERATING_PROMPT | they stand as written |
| Q-1 | LIB_LOGS file name | `<intention>_<result>_<names>_<seconds>.lib_log` |
Full list: `TODO.md`, owner lane.

## Next (AI): see the resume plan, section 2

- **TTRPG Studio (15 Nov, Fable):** new repo `LIB_TTRPG`, branch `ttrpg-studio-1`. Design, prompts and a
  tested terminal engine are done (`python3 ref/ttrpg_ref.py play "<idea>"`; owner's test steps 2 to 6
  pass on gemma 2B, and on gemma + lfm3-omni-2b). **Opus next:** build the LiveCode stack from
  `LIB_TTRPG/OPUS_BUILD.md` (3 to 4 hours), then the tuning pass. No more Fable time needed for iteration 1.
1. Opus: Amazing Couple on cellmap v2 (each maze made once as a file, walls exactly as drawn:
   answers the owner's invisible-wall notes of 14 Nov, which are still open).
2. Opus: E13 in the xt3d games bench; `CellMap.LevelBoxes` in LiveCode for the solid look.
3. Opus: LIB_EDITOR E03-E12, E14, E15 on the v2 format; LIB_HOWTO step code. Spark: step words.
4. Fable, only when needed: stacked maps and slopes (format changes); LIB_ig3d convergence.

## Earlier (12-14 November, kept as written)
- **13–14 Nov, late:** the plan for next time and the long-term goals are in
  `Next_Steps_With_Claude/WHEN_WE_RESUME_AFTER_11_14_2026.md`. Done since the last entry: all 9
  round-two games, Probe vs Cone reworked (aim, ricochets, orbiters, arm), uDead ammo and
  feedback, arrow keys never open menus, WASD everywhere, HUDs below the top bars, LIB_UPBGE (22
  template specs) and Trench Run, Linux LiveCode server, **game notes (` or F2) and the in-game
  command line (/next /back /play /games)** in Vibecode3D and the xt3d bench.
- **iGame3D main UI remade in Vibecode3D (A-83, LIB_GAMES branch `ig3d-ui-remake`):** card
  `Play.Ig3dEditor`: the 26-tool toolbar with Unicode icons and old tooltips, the old menu bar,
  and Library = the asset browser: 755 models from the 2008 Data load as wireframes. Primitives,
  camera, colours, play/orbit, undo, boom wired. Launch: `LIB_TEST/install_all_games_vibecode3d.sh Ig3dEditor`.
- **LIB_BUILD** (2026-11-13 evening): `collector.livecodescript` + `parts.txt` collect the xt3d
  bench, Vibecode3D standalone, games and libraries into one portable folder (tested:
  `C:\LIB_DEMO`, 3,146 files, 311 MB). Thrmnlra: Return-in-field fixed (the xt3d bench bug),
  answers grow by letters. Round two games (owner's concepts) on LIB_GAMES `spark-arcade`:
  VectorPong3D, JaiAlaiBlock, FloppyFlynn, VectorBlobApocalypse, BigBallOfVectors (compile; first
  three pass headless). Spark drafted concepts and levels for all nine (LIB_SPARK/arcade/out/2*);
  still to script: PromptAndGlazeMaze, ShaftDescent, MatrixLock, ProbeVsCone.
- **WEEKEND HANDOVER (usage nearly out until Sunday's reset):** `LIB_TEST/README.md` is the test
  sheet; `PLAY_Thrmnlra_Vibecode3D.bat` and `PLAY_Thrmnlra_xt3d.bat` launch the game in each engine
  without an AI. Thrmnlra runs unchanged in the xt3d games bench (labels line up, 27 fps). Pace is
  70% (`kPace`), grid at rest 10,40,10. Owner's notes go in `LIB_TEST/OBSERVATIONS.txt`.
  NOT done: answers growing by letters, the fitness-of-service test, Escape pause menu, titles (A-20, A-30, A-33).
- **LIB_BIN:** LiveCode Community Server 7.1.4 (32-bit) and 9.6.3 (64-bit) installed and running
  from WSL. **The 2007 iGame3D Pro external loads in 7.1.4** (123 commands, 53 functions), starts
  (OpenGL 4.6) and **runs Lua** (`print(6*7)` → 42). Why it seemed dead: the LC7 stack names the
  Mac `.bundle`, and only a 32-bit engine can load it. `LIB_ig3d/IGAME3D_EXTERNAL.md` (+ `_API.md`).
  The owner: the old engine stays a reference and template (what was tried 20 years ago); not
  ongoing. Reuse every non-junk element of the old stack (A-83).
- **Owner's SUPER_IMPORTANT note:** images ignored by every model incl. Spark (rule 4); provenance
  then dedupe (rule 4b, `tools/provenance.py`; record in `LIB_LLMOUT/Read/LIB_XTJSON/PROVENANCE.md`:
  192 files, no identical copies). The inbox's ~2,900 non-stack files were cleared before this
  (not by me): say if that wasn't you.
- **New stacks harvested:** iGame3D main UI 2007 (`ig3d_MainUI050107.rev`: 17 stacks, 41 cards,
  971 controls, 315 scripts) and 2026 (`ig3d_UI_MAIN_11_13_2026`: 19 stacks, 46 cards, 1,226
  controls, 328 scripts). The harvester had been renamed to `.txt` (owner): tools accept both.
- **LIB_SCRIPTBLOCKS** (owner agreed): harvest / manage / export script blocks. Examples in
  `LIB_GENERICA/Data/Example`: 24 blocks (all 351 handlers of GAD_WORKING + Generica), 47 generic
  object scripts, inactive text. ScriptBlocks stack: edit, Check, Find, Replace in all, Export, Apply.
- **Harvester bug fixed (LIB_XTJSON branch `harvester-nested-groups`, checked out):** every group
  inside a group was dropped (LiveCode error 242). Re-harvested with 0 errors: Invaders (73 objects
  were missing), TTRPG_STUDIO, GenericaAnyData_04042018a, **GAD_Globals (7)**, **Game_Object_Properties_Manager**,
  GenericaProperties 03162026a / Day_2_Part6 / Day_3_Part1, XMLdemo, video_capture; and the Vibecode3D
  engine harvest (29 missing; Vibecode3D branch `xtjson-nested-groups`). GAD notes written from the
  old GAD_Globals / Game_Object_Properties_Manager harvests may need a second look.
- All 19 `LIB_` folders are git repositories (LIB_ALPHA rule 2); LIB_LLMOUT items now in `Read/`.
- LIB_SYSTEM started: `LIB_ALPHA.md`, `LIB_OMEGA.md`, `OPERATING_PROMPT.md`, `TODO.md`, this file.
- XTJSON batch: 113 of 115 stacks harvested into `~/projects/XTJSON/batch/`, originals moved to
  `LIB_LLMOUT/Read/LIB_XTJSON/`. Left: `Web_Collector_Watcher_..._newest.livecode` (crashes LiveCode,
  even sampled: A-11) and `Bezier.livecode/__MACOSX/._Bezier.livecode` (Mac junk, not a stack).
- Newest builds of each stack family listed: `XTJSON/batch/_NEWEST.md`; `XTJSON/newest/` links
  the 80 newest harvests (33 older builds left out) (A-13, first half).
- A-12, GAD first: `LIB_GAD/GENERICA_TEMPLATE.md`. Generica = a 37-category, 637-label
  schema of a game's words (Galactica's); data unchanged since Feb 2024, the 2026 builds load it
  from the .txt files; maps onto Galactica-4's variables; GAD_WORKING is a separate line (the game).
- **LIB_GENERICA** (approved): `sets/galactica` (49 lists, 533 labels from the newest Generica),
  `sets/genetic_anomaly` (DRAFT overlay, 7 lists), LiveCode + Python loaders (overlays, slot
  filling), Sequencer `{@list:n}`. Tested in Python and in LiveCode. Branch `lib-generica-1`.
- GAD's self-writing system mapped: `LIB_GAD/GAD_SELF_WRITING_SCRIPTS.md` (code as data, the
  script-block palette, globals written into the stack script, Generica's file import and global
  init builder, the trace-code instrumenter; 5 bugs found). New TODO A-64, A-65.
- Rules updated: work to each 5-hour limit, committing on branches (LIB_ALPHA rule 7, operating prompt §5).
- Branch commits: LIB_SYSTEM `lib-system-draft1`, LIB_XTJSON `xtjson-batch`, LIB_GAMES `spark-review`.

