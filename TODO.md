#TOD FOR CLAUDE. CLear   JOB # 1
# TODO: the LIB_ARRAY list

Draft 1, 2026-11-13. IDs stay fixed (O = owner, S = Spark, A = AI models, Q = questions).
Done items move to `DONE.md` with their date. Order inside a lane = priority.

## Owner (posted early: do them whenever suits; time is a rough guess)

| ID | Task | Time | Needed for |
|---|---|---|---|

I STOPPED HERE.
| O-7 | Say whether the two LIB_PUBLIC notes ("any text to use...", "dowhathouwilt.txt") were already used | 1 min | LIB_PUBLIC | Those are place holder instructions for later. (DO NOT track this until further notice, after merge note to write notes to project) **PAUSED (not tracked until the owner says).**

| O-8 | Sketch (words or a photo) the LIB_TOOLBAR you want: which buttons, where it sits | 10 min | A-40 | You should be able to extract from the data of : Start here: "\\wsl$\Ubuntu\home\igame3d\projects\XTJSON\batch\rev\ig3d_MainUI050107\stack_ig3d_UI_MAIN_may2007.json"   
Now it's fill in the blanks. 
Get the MAIN stack concept remade with your new graphic systems. 
Choose  unicode characters for the appropriately named  missing images

buttons and menu intention and remake the GUI valid for what we have available for the VECTOR Thing we are doing.
With the binary strings. 

| O-9 | Pick the users list for window titles (LIB_USERS): OWNER, CLAUDE, SPARK, ...? and their short tags | 2 min | A-30 |
| O-10 | Look at 3 or 4 Spark GUI design drafts when they land (S-3) and mark keep / redo | 20 min | A-45 |
| O-11 | (dropped 2026-11-13: I work to each limit and commit on branches) | - | - |  
Everything is the most generic term for everything and collapse it into a spread sheet at a tap of a key.


gentica_anomaly should be based on our successs and knowledge gains by generic_array_data development.
 people with paranormal powers and/or experiences real and imagined, with escalating levels of super strange and powerful beings. Who are all stickfigures. in procedural world. Lets go! Work on this. We don't see a lot of aniamtion , focus on the whole big map point plotting angle. The Super hero stuff has to be a big shocker when the gameplay is largely good and Ed Zevada will say 

START ON igame3d UI reuse  NOW 1014 PM 11 11 2026


## Spark (local, free; I prepare the prompts, you start `START_SPARK.bat` when a run is ready)

| ID | Task | Status |
|---|---|---|
| S-0 | iGame3D 2008 manifest run (Fluid, Levels, Shaders, WTF...) | running, ~800 requests left |
| S-1 | First-look catalogue of every harvested stack's scripts (XTJSON batch output), newest builds first | prompt to write (A-12) |
| S-2 | Draft LIB_ABOUT pages from each project's README + harvest (Claude reviews) | prompt to write (A-31) |
| S-3 | GUI window and widget designs for interacting with our LIBs: file inputs, asset browsers, timelines, inspectors, toolbars: as text descriptions XTJSON can rebuild ("redeem") | prompt to write (A-45) |
| S-4 | Port plans for approved LiveCode UIs to raygui, Dear ImGui and tkinter | after O-10 |
| S-5 | LIB_GLOBALS: list every global in the corpus and harvests with where it is set and used | prompt to write (A-35) |

## AI models (Opus unless marked)

### XTJSON and the stack inbox
| ID | Task |
|---|---|
| A-10 (done) | Finish the 2026-11-13 batch (32 stacks left; the watchdog stopped with the last session): resume under `LIB_XTJSON/tools/xtjson_batch_watch.sh` |
| A-11 (done) | Batch app: pass `customSample=5` for stacks over 2 MB; retry CRASHED stacks with sampling; then decide LiveCode Server (one process per stack) after O-5 |
| A-12 | Analyse all harvests, newest builds first (`XTJSON/batch/_NEWEST.md`): GAD/Generica as a reusable template (variables, options, save/load), then CLIP, DND/TTRPG, Enochian, the rest; map Generica's variables onto `LIB_GAD/GAD_ESSENCE_AND_VARIABLES.md` |
| A-13 | Make `XTJSON/newest/` links; move the inbox's non-stack files to `LIB_LLMOUT/Read` once analysed (no PNG reading) |
| A-14 (done) | Document `customSample` in `LIB_XTJSON/docs/HARVEST_FORMAT.md`; commit LCHarvest2 + watchdog |

### Spark manifest (iGame3D 2008)
| ID | Task |
|---|---|
| A-15 | Review 4 when S-0 ends: run `check_drafts.py`, fix prompts if a new fault shows |
| A-16 | Build `GLOSSARY.md` and `PROCEDURES.md` from the reviewed drafts into `LIB_ig3d` |
| A-17 | Commit the manifest changes (prompt v4, HOLD/ONLY, Mappers review) to `spark-review` |

### Games STOP PRODUCTION OF Thrmnlra its fine for now.
| ID | Task |
|---|---|
| A-20 | Thrmnlra pace: slower defaults; answers grow by letters (Y/N → OK/NO → YAY/NAY); a fitness-of-service test (G.O.A.T. style) as the Trainer's frame; play-test the Intro launch prompt and the recall/detonate stage under the new layout |
| A-21 | Merge `thrmnlra` after O-3; promote the Sequencer to `LIB_SEQUENCE` when a second game uses it |
| A-22 | LIB_EDIT: an Edit_Map UI for live-tuning generated scenes (grid colour like 10,40,10, nearly invisible) and saving preferred first-launch configs |
| A-23 | Sequencer: a visual timeline view of a `.seq` file (lanes and bars) |

### The rules, applied everywhere
| ID | Task |
|---|---|
| A-30 | Window titles (LIB_ALPHA 13-14) in Vibecode3D, xt3d, the batch app, every game card |
| A-31 | LIB_ABOUT: a one-page About for every LIB (rule 17), and an About card in every stack |
| A-32 | LIB_TEST and LIB_LOGS folders with READMEs; the test-stack save step (rule 16) as a library handler |
| A-33 | Escape/pause with developer options and an MCP command-line toggle (rules 18-20) as a shared library every game uses |
| A-34 | Developer card 1 blank; cards laid out as a grid on screen |
| A-36 | Close-and-free pattern (LIB_ALPHA 12b) in every stack: GAME_Browser, Game_Player (+ launcher), Status_Browser (+ launcher), BitEditor, Vibecode3D, the xt3d benches, LIB_HOWTO, LIB_EDITOR, the batch app; check none stays in memory after its window closes |
| A-35 | LIB_GLOBALS: register every global, its use and its Python equivalent, so standalone scripts reuse them safely |

### New LIBs (plan first, with Fable when the owner switches) 
| ID | Task |
|---|---|
| A-40 | LIB_TOOLBAR: a floating, always-in-front launcher for the latest and most important stacks, menus and folders (after O-8) |
| A-41 | LIB_RAYGUI: raygui in xt3d, mirroring what we do in Vibecode3D and LiveCode; look: white page, 0.5 mm technical-pen colour lines |
| A-42 | LIB_GUI: a GUI builder that keeps the system alive outside the LiveCode engine (the "put away the old IDE" test) |
| A-43 | LIB_USERS: who is at the controls (for titles, logs and permissions) |
| A-45 | Spark GUI design prompts (S-3), then test the approved ones in LiveCode via XTJSON redeem |

### LIB_GENERICA (approved 2026-11-13)
| ID | Task |
|---|---|
| A-60 | Thrmnlra and Amazing Couple take their UI words and event strings from LIB_GENERICA sets (a `thrmnlra` theme) |
| A-61 | Genetic Anomaly theme: fill the other game-state lists with the owner (O-13) |
| A-62 | A label editor stack (LIB_TEST): browse categories, edit labels, save the files |
| A-63 | Move the 393 duplicate label .txt files in LIB_LLMIN/LIB_XTJSON to `LIB_LLMOUT/Read` (the set is now the source) |

| A-64 | (now LIB_SCRIPTBLOCKS: owner agreed 2026-11-13) Script-block browser: GAD's code palette (handlers by name prefix, one button per category) over any harvest or live stack (LIB_MCP), read-only first (`LIB_GAD/GAD_SELF_WRITING_SCRIPTS.md`) |
| A-65 | (now LIB_SCRIPTBLOCKS) A developer library for GAD's script tools (insert global, global init builder, trace codes, block compare) that edits OTHER stacks or script files, with a backup before each write; fix the bugs listed in the GAD doc |

### From the owner's SUPER_IMPORTANT note (2026-11-13)
| ID | Task |
|---|---|
| A-70 | (tool: `LIB_SYSTEM/tools/provenance.py`; first record 2026-11-13: 192 files, no copies) Provenance record of the LIB_XTJSON inbox and harvests by file kind (where each copy was, what needs it, what changed, where it came from; content hashes), then move the oldest redundant copies to LIB_LLMOUT/Read (LIB_ALPHA rule 4b) |
| A-71 | Show unfinished stacks: a viewer that displays any harvested stack (cards, controls, scripts) even when the stack itself can't run |
| A-72 | **Visualise a stack script in vectors:** handlers as nodes (grouped by category/prefix), calls as lines, globals as a ring, drawn in Vibecode3D's vector style (and as an image for the docs) |
| A-73 | DONE 2026-11-13 (LIB_SCRIPTBLOCKS + LIB_GENERICA/Data/Example): GAD script blocks into LIB_GENERICA `Data/Example/`: generic scripts per object type and per code category, stored INACTIVE (text), with an editor to browse and edit them all at once; applied to objects only on purpose |

### iGame3D, running again (2026-11-13)
| ID | Task |
|---|---|
| A-80 | (PARKED 2026-11-13: the old engine is reference, not ongoing) Find iGame3D's shutdown call so the 7.1.4 server exits cleanly (signal 11 now) |
| A-81 | (PARKED) Run a 2008 level headless-ish: ig3d_Init on the LIB_BIN Data, load a level by Lua, CopyGLToRevWindow into an image, save a screenshot |
| A-83 | **Reuse inventory of the old iGame3D main UI** (2007 `.rev` vs 2026 `.livecode` harvests): every stack, card, control and script group sorted keep / adapt / junk, with where each kept piece goes now (LIB_SCRIPTBLOCKS examples, LIB_GENERICA, Vibecode3D/xt3d editors, LIB_TOOLBAR) |
| A-82 | Harvest with the 9.6.3 server one process per stack (timeout each): the Collector stacks again |
| A-84 | (owner accepted 2026-11-15, from A-83) **Vibecode3D editor Inspector**: Window > Inspector, one card per object kind (material, bones, colours), UIs with placeholder scripts filled when a game needs them. Only what games and procedural assets need; no iGame3D mesh editing ("Blender stays king"). First real card: a **BVH / bones animation previewer with a keyframe clipper** (stop before the glitch part) that adds clips to the game's Animation List, inherited by models, not embedded in them. Needs LiveCode. |
| A-85 | (owner accepted, conditional) `.wtf` `#Animations` reader -> Sequencer clips (with A-23) **only if it converts to our glb/BVH**; otherwise .wtf goes on the back burner. Meshes stay glb/glTF (and USD). Python feasibility check first (no LiveCode needed). |
| A-86 | (owner accepted) "Replace with model...": a small UI that swaps the placeholder geometry in template games and saves the choices as an alternate **Skin**. Needs LiveCode. |
| A-87 | (owner accepted) Library preview drag: the preview goes into a temporary stack that follows the mouse over the viewport, works across stacks (maybe into other apps), drops the model into the scene. Needs LiveCode. |
| A-88 | (owner: "not sure what this is, but sounds good") A game-design-document outline built from GameOverViewData's tabs, for LIB_HOWTO and PROMPT & GLAZE. Explain it in one paragraph with an example before building. |
| O-14 | (owner, when convenient) try the iGame3D Player exe / the LC7 main UI on the desktop if you have LiveCode 7.1.4 (desktop) somewhere | 

### Project health
| ID | Task |
|---|---|
| A-50 | Every project: README up to date, `--help` on every tool, one test that runs |
| A-51 | Independence pass: list every external asset/code dependency per LIB and what replaces it |
| A-52 | Usage visibility: find out whether Claude Code's status line can show the 5-hour window; if so set it up |

## Questions waiting (with the default I'll take)

| ID | Question | Default |
|---|---|---|
| Q-1 | LIB_LOGS file name: `<intention>_<result>_<names>.livecode<seconds>.lib_log` exactly, or `<...>_<seconds>.lib_log`? | `<intention>_<result>_<names>_<seconds>.lib_log` (a saved .livecode stack inside) |
| Q-3 | Make `LIB_GAD` a git repo (third-party Galactica sources ignored, local only)? | yes, local only, the Galactica folders in `.gitignore` |
| Q-2 | Thrmnlra's G.O.A.T.-style test: name it something of ours in public? | "Fitness of Service test" | HAHA mayb. We have to work on funny typos, later and see how it holds up in a demo release of the games in on go.

