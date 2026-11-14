# STATUS

Friday, November 13, 2026, 01:30. Rewritten at every milestone (OPERATING_PROMPT section 4).

## Running (no Claude usage)
| What | Where | State |
|---|---|---|
| Spark: iGame3D 2008 manifest | Spark's own window; log `LIB_GAMES/igame3D_2008_Texts/_manifest/spark/_run.log` | ~800 requests left (~9 h); `.fl` files skipped; Fluid/Mappers: 5 final builds only |

## Done today
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

## Waiting on the owner (with the default I'll take)
| ID | Question | Default |
|---|---|---|
| O-1 | Correct LIB_ALPHA / OPERATING_PROMPT | they stand as written |
| O-5 | LiveCode Server 9.6.3 Linux zip? | I'll look for it online when you say so |
| Q-3 | Make LIB_GAD a git repo? | yes, local only, Galactica sources ignored |
| Q-1 | LIB_LOGS file name | `<intention>_<result>_<names>_<seconds>.lib_log` |
Full list: `TODO.md`, owner lane.

## Next (AI)

1. A-83: reuse inventory of the iGame3D main UI (2007 vs 2026); then A-12: then CLIP, DND/TTRPG, Enochian, the one-offs.
2. Both Collector stacks (Collector_v11022026, Web_Collector_Watcher) hang LiveCode on harvest, even
   sampled (guess: a browser widget). Their scripts are already exported as text in the inbox
   (`CollectorStacks/*.txt`): analyse those; one-process test later (A-11).
3. LIB_SCRIPTBLOCKS: open the ScriptBlocks stack in LiveCode and test it; the palette view.
4. A-72: a stack script drawn in vectors (handlers as nodes, calls as lines).
