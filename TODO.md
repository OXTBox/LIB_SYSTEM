# TODO: what is still open

Rewritten 18 Nov 2026 (Opus) when the owner said "Lets turn this todo list to a DONE list":
everything finished went to `DONE.md`; the list as it stood, with the owner's notes in it, is
`archive/TODO_2026-11-13_to_2026-11-18.md`. IDs never change (O = owner, S = Spark, A = AI, Q = question).

**This is the long list, not the order.** What comes first is the Priority Tube
(`LIB_LLMIN/LIB_DEV/PRIORITY_ORDER.txt`). An item here that the owner wants soon becomes a bubble there.
When an item is finished, its row moves to `DONE.md` with the date and where the work is.

## Owner

| ID | Task | Note |
|---|---|---|
| O-10 | Look at 3 or 4 Spark GUI design drafts when they exist (S-3) and mark keep / redo | after S-3 |
| O-14 | Try the iGame3D Player exe / the LC7 main UI, if LiveCode 7.1.4 desktop is somewhere | when convenient |
| O-7 | The two LIB_PUBLIC placeholder notes | **paused** by the owner until he says |

## Spark (local, free; Claude writes the prompt, the owner starts the run)

| ID | Task | State |
|---|---|---|
| S-0 | iGame3D 2008 manifest run | stopped 13 Nov with ~800 requests left; restart when wanted |
| S-1 | First-look catalogue of every harvested stack's scripts, newest first | prompt not written |
| S-2 | Draft About pages from READMEs (for A-31) | prompt not written |
| S-3 | GUI window and widget designs as text XTJSON can rebuild | prompt not written (A-45) |
| S-4 | Port plans for approved UIs to raygui, Dear ImGui, tkinter | after O-10 |
| S-5 | Every global with where it is set and used | mostly covered by LIB_GLOBALS; probably drop |

## AI

### The rules, applied everywhere
| ID | Task | State |
|---|---|---|
| A-31 | A one-page About for every LIB, an About card in every stack (LIB_ALPHA 17) | 4 of 44 LIBs have one |
| A-32 | LIB_LOGS with its README; the test-stack save step as a library handler | LIB_TEST exists; LIB_LOGS does not (waits on Q-1) |
| A-33 | Escape pauses every loop, developer options, an MCP command line toggle (LIB_ALPHA 18-20), one shared library | not built; game pause menus should follow LIB_MENU (question W-3 in STATUS) |
| A-34 | Developer card 1 blank; cards laid out as a grid | not built |
| A-36 | Close-and-free (LIB_ALPHA 12b) in every stack | 17 scripts have it; the full check (nothing left in memory after closing) not done |
| A-51 | Independence pass: every outside asset/code each LIB needs and what replaces it | not started |
| A-52 | Show the 5-hour window in Claude Code's status line | not started |

### New LIBs
| ID | Task | State |
|---|---|---|
| A-40 | LIB_TOOLBAR: a floating launcher for the newest stacks, menus, folders | plan done, build open |
| A-41 | LIB_RAYGUI: raygui in xt3d, white page, technical-pen lines | plan done, build open |
| A-42 | LIB_GUI: the GUI builder that lives outside the old IDE | stages 1-3 + FromStack on `gui-step1`; next: the popup kind (tube #1) |
| A-45 | Spark GUI design prompts (S-3), then test the approved ones via XTJSON | not started |

### Games and editors
| ID | Task | State |
|---|---|---|
| A-23 | Sequencer: a timeline view of a `.seq` file | not started (Thrmnlra stopped) |
| A-89 | iGame3D XT (LIB_EDITOR): generators, Aquarius, stick figures, the 2008 Lua as xTalk, DeadDays, the editor | ongoing; the owner picks the order |
| A-90 | LIB_Taylor: a customize-your-character editor | later |
| A-92 (3)(4) | cellmap v3: BitEditor Slope tab, pack window, preview hiding | DONE, merged 19 Nov (LIB_BIT main 7b838d7) |
| A-97 | Retire `demo` and `Simple_Test2` (as `original_demo`, `Original_Simple_Test2`), rename `Simple_Test1` to `Simple_Cube` | the files are still under the old names |

### LIB_GENERICA, LIB_SCRIPTBLOCKS, stack tools
| ID | Task | State |
|---|---|---|
| A-60 | Thrmnlra and Amazing Couple take their words from LIB_GENERICA | not started (Thrmnlra stopped) |
| A-66 | LIB_GENERICA refers to LIB_LISTS lists by name (`<set>/<list>.txt`), never copies them; the Python and xTalk loaders follow the reference (owner, 18 Nov) | not started |
| A-62 | A label editor stack | not started |
| A-65 | GAD's script tools (insert global, init builder, trace codes) as a library that edits other stacks, with a backup | not started; the GAD doc lists 5 bugs |
| A-71 | A viewer that shows any harvested stack even when it cannot run | not started |
| A-72 | A stack's script drawn in vectors: handlers as nodes, calls as lines | not started |
| A-82 | Harvest with the 9.6.3 server, one process per stack: the Collector stacks | not started |

### Last on the list
| ID | Task | State |
|---|---|---|
| A-95 | Spark with OXT-Beyond: Spark fills a control table, a script checks it and builds on a copy | about an hour; never tried |

## Questions waiting (with the default I'll take)

| ID | Question | Default |
|---|---|---|
| Q-1 | LIB_LOGS file name | `<intention>_<result>_<names>_<seconds>.lib_log` (a saved stack inside) |
