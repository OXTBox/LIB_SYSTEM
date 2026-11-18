# DONE: what the LIB_ARRAY list has finished

The owner, 18 Nov 2026: "Lets turn this todo list to a DONE list." Every finished item from
`TODO.md` (13-18 Nov) is here, grouped by kind, with its ID, when, and where the work is. What is
still open stayed in `TODO.md`. The list exactly as it stood before, with the owner's notes written
into it, is `archive/TODO_2026-11-13_to_2026-11-18.md`.

"Not seen on screen" means tested headless only: the owner has not looked yet.

## The owner's lane

| ID | Task | Done |
|---|---|---|
| O-1 | Read LIB_ALPHA and the operating prompt; correct them | 13 Nov: "rules are fine". 18 Nov: operating prompt rewritten on his word (Project Map note) |
| O-2 | Play Thrmnlra | 13 Nov: "it's great, it needs work"; Thrmnlra stopped for now |
| O-3 | Review LIB_GAMES `thrmnlra` | 13 Nov: merged (ec025f4) |
| O-4 | Review LIB_GAMES `amazing-couple` | 13 Nov: merged (6332a27) |
| O-5 | Find LiveCode Server 9.6.3 (Linux) | 13 Nov: installed at `LIB_BIN/livecode-server/9.6.3-linux-x64`, tested |
| O-6 | The bridge's `ForClaude/ClaudeRead` folder | 13 Nov: deleted by the owner |
| O-8 | Sketch the LIB_TOOLBAR | 13 Nov: answered with the 2007 iGame3D main UI harvest; built as A-83 (the Ig3dEditor toolbar) and planned as A-40 |
| O-9 | The users list for window titles | 18 Nov: answered in LIB_USERS `PLAN.md` section 9 (OWNER, PLAYER, FABLE, OPUS, SONNET, HAIKU, SPARK, AGENT; personas lower case; `FOR OWNER` in titles) |
| O-11 | Keep an hour of each window | dropped 13 Nov: work to each limit, commit on branches |
| O-12 | Thrmnlra's public title | 13 Nov: name kept |
| O-13 | Genetic Anomaly draft words | 13 Nov: "a seeded automated simulation, it's fine"; 14 Nov rewritten over the `generic_array_data` base theme |

## XTJSON and the stack inbox

| ID | Task | Done |
|---|---|---|
| A-10 | Finish the 13 Nov batch | 13 Nov: 113 of 115 stacks harvested into `XTJSON/batch/` |
| A-11 | `customSample` for big stacks, retry the crashed ones | 13 Nov (one Web_Collector stack still crashes LiveCode, even sampled) |
| A-12 | Analyse the harvests: GAD/Generica first, then CLIP, DND/TTRPG, Enochian | 13-14 Nov: `LIB_GAD/GENERICA_TEMPLATE.md`; CLIP/DND/Enochian analysis (`NIGHT_WORK_11_14.md`) |
| A-13 | `XTJSON/newest/` links; tidy the inbox | 13-14 Nov: 80 newest harvests linked; inbox's non-stack files moved |
| A-14 | Document `customSample`; commit the harvester and watchdog | 13 Nov |
| A-63 | The 393 duplicate label files | 14 Nov: already gone from the inbox; the set is the source |
| A-70 | Provenance record of the inbox | 13 Nov: `tools/provenance.py`, 192 files, no copies |

## Spark manifest (iGame3D 2008)

| ID | Task | Done |
|---|---|---|
| A-15 | Review 4 of the drafts | 14 Nov: re-run |
| A-16 | GLOSSARY.md and PROCEDURES.md | 14 Nov: in LIB_ig3d |
| A-17 | Commit the manifest changes | 14 Nov: merged with every LIB_GAMES branch |

## Games

| ID | Task | Done |
|---|---|---|
| A-20 | Thrmnlra pace, answers grow by letters | 13 Nov: pace 70%, answers grow by letters; the rest stopped with Thrmnlra |
| A-21 | Merge `thrmnlra` | 13 Nov (the Sequencer moves to LIB_SEQUENCE only when a second game uses it) |
| A-22 | LIB_EDIT, a map editor | became LIB_EDITOR (examples E01-E13, cellmaps) and the BitEditor |
| A-94 | Three game tests failing on main | 17 Nov: t21 and t36 fine; t23 Block City was a real bug, fixed on `vector-toss-dangle` |

## The rules, applied everywhere

| ID | Task | Done |
|---|---|---|
| A-30 | Window titles | 17 Nov: `Users.Title` in LIB_USERS; 9 scripts ask it (branches `users-title`, waiting for review) |
| A-35 | LIB_GLOBALS | 14 Nov: `GLOBALS.md`, 498 globals; 15 Nov: purposes of the 44 most used |
| A-50 | README, `--help`, one test that runs, in every project | 14-15 Nov: `tests/run_tests.py` in the LIBs (plain Python) |

## New LIBs

| ID | Task | Done |
|---|---|---|
| A-40 | LIB_TOOLBAR | plan done: `LIB_TOOLBAR/PLAN.md` (the build is still open in TODO) |
| A-41 | LIB_RAYGUI | plan done: `LIB_RAYGUI/PLAN.md` (the build is still open in TODO) |
| A-43 | LIB_USERS | 17-18 Nov: plan kept, `Users.Title` built, the owner's answers in; on main |

## LIB_GENERICA and LIB_SCRIPTBLOCKS

| ID | Task | Done |
|---|---|---|
| A-61 | Genetic Anomaly theme | 14 Nov: rewritten over `generic_array_data` ("the most generic word for everything", the owner's note) |
| A-64 | Script-block browser (GAD's code palette) | 13 Nov: LIB_SCRIPTBLOCKS |
| A-73 | GAD script blocks as inactive text, with an editor | 13 Nov: `LIB_GENERICA/Data/Example` |

## iGame3D, old and new

| ID | Task | Done |
|---|---|---|
| A-83 | Reuse the old iGame3D main UI | 13 Nov: card `Play.Ig3dEditor`, 26 tools, the old menu bar, 755 models as wireframes; now iGame3D XT in LIB_EDITOR |
| A-84 | Inspector (Object, Animation pages) | 15 Nov, not seen on screen |
| A-85 | `.wtf` animations to BVH | 15 Nov: 58 BVH in `LIB_BVH/iGame3D_DeadDays` |
| A-86 | Replace With Model... / skins | 15 Nov, not seen on screen |
| A-87 | Library preview drag into the view | 15 Nov, not tried with a real mouse |
| A-88 | Game design document outline | 15 Nov: explained in `LIB_ig3d/GDD_OUTLINE_A88.md`; built only on the owner's word |
| A-91 | Genetic Anomaly Detector gets its home | 16 Nov: LIB_GAD `GeneticAnomaly/` with the 2018 Galactica 3 GUI as its base |
| A-80, A-81 | The 2008 engine running headless | parked 13 Nov: the old engine is reference, not ongoing |

## LIB_THEME

| ID | Task | Done |
|---|---|---|
| A-89 (theme) | Theme Studio stack | 15 Nov |
| A-90 (theme) | The white scrollbars | 15 Nov: answered (OXT-Beyond draws them dark with Windows dark mode) |

## Kept 17 Nov: the engine and the maps

| ID | Task | Done |
|---|---|---|
| A-92 (1)(2)(5) | cellmap v3: slopes drawn, map packs, E13 walks two rooms; the E12 checker | 17 Nov, on LIB_BIT `cellmap-v3-followups` and `cellmap-v3-checker` (waiting for review). (3)(4) still open |
| A-93 | Engine contract: the planned calls, retire the debts | 18 Nov: every planned call built (`contract_calls.livecodescript`), no planned call left; debts retired game by game with Rename Day |
| A-96 | Look with roll, games off `gCameraYaw/Pitch` | 18 Nov: `Camera.SetLook` (the owner's `Engine.SetLook`, renamed), games moved |
| A-98 | Rename Day | 18 Nov: 24 calls `Group.Verb`, 22 aliases; games: 666 places down to 76 in 4 scripts |
| A-99 | Type `Entity.` and see the list | 18 Nov: built (`lib_suggest`, `suggest_window`), not seen on screen |

## Questions answered

| ID | Question | Answer |
|---|---|---|
| Q-2 | Thrmnlra's G.O.A.T.-style test, a name of ours | "HAHA maybe": later, with the funny typos, when the games get a demo release |
| Q-3 | LIB_GAD a git repo? | yes: local repo, Galactica sources ignored |
