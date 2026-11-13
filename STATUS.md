# STATUS

Friday, November 13, 2026, 01:30. Rewritten at every milestone (OPERATING_PROMPT section 4).

## Running (no Claude usage)
| What | Where | State |
|---|---|---|
| Spark: iGame3D 2008 manifest | Spark's own window; log `LIB_GAMES/igame3D_2008_Texts/_manifest/spark/_run.log` | ~800 requests left (~9 h); `.fl` files skipped; Fluid/Mappers: 5 final builds only |

## Done today
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
1. A-12: the other newest builds: CLIP, DND/TTRPG, Enochian, then the one-offs (a table per family).
2. A-13: move the inbox's non-stack files to `LIB_LLMOUT/Read` once analysed.
3. A-14: document `customSample`; commit LIB_XTJSON (harvester, batch app, watchdog).
