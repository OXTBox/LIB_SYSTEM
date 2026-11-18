# STATUS

Wednesday, November 18, 2026, midday. Rewritten by Claude (Opus 5.5) on the owner's Project Map
note ("Archive with date range in name, then update this document!"). Everything from 13 to 17 Nov
is in `archive/STATUS_2026-11-13_to_2026-11-17.md`; older plans in `Next_Steps_With_Claude/`.

Where to start a session: the Priority Tube (`LIB_DEV/PriorityTube/NEXT.md`) and the Project Map
(`LIB_DEV/ProjectMap`). This file says what is true today; the tube says what comes first.

## Done 18 November

| What | Who | Where |
|---|---|---|
| **Rename Day**: every engine call is `Group.Verb` (`Entity.`, `Camera.`, `Scene.`...), 22 old names kept as aliases for us only; the planned contract calls built (`Camera.SetLook`, `Camera.WorldToScreen`, `Entity.Set/Get/SetMesh`, `Engine.Mouse`, `Game.FindFile`, ...) | Fable plan, Opus build | LIB_ig3d `ENGINE_CONTRACT.md`, `RENAME_DAY.md`; merged |
| **Games moved to the new names**: 666 places in 54 scripts down to 76 in 4 (BlockCityHustle and VectorToss wait for `vector-toss-dangle`; `demo`, `Simple_Test2` retired) | Opus, overnight | `Next_Steps_With_Claude/FOR_OWNER_OVERNIGHT_11_18_2026.md` |
| Six ComfyUI genre kits; kit games live in `LIB_COMFY/games`; the stand-alone Comfy app parked | Opus | `COMFY_STANDALONE_NOTE_11_18_2026.md` |
| LIB_INPUT merged ("looks great"); LIB_SFX plays several sounds at once in xt3d | Opus | `FOR_OPUS_RENAME_DAY_STEP3_11_18_2026.md` |
| Occlusion culling in pure xTalk: answered yes, a plan, nothing built | Fable | `FOR_OPUS_OCCLUSION_CULLING_11_18_2026.md` |
| WSL slowness and the port 8770 freeze: tickets 0001-0003 | Opus | `ISSUES/INDEX.md` |
| LIB_USERS answers (FOR OWNER in titles, personas lower case, saves in Documents/My Games) | owner + Opus | LIB_USERS main |
| GAD battles taken off the list ("form follows function") | owner | - |
| This file, the operating prompt rewritten, TODO turned into a DONE list | Opus | LIB_SYSTEM |

## Running (no Claude usage)
| What | Where | State |
|---|---|---|
| Nothing | - | `LIB_DEV/tools/wait_for_tell.sh` runs only while a session is open and the owner is at the keyboard |
| Spark: iGame3D 2008 manifest | Spark's own window | stopped since 13 Nov; restart only when wanted |

## Waiting on the owner (with the default I'll take)
| ID | What | Default |
|---|---|---|
| B-1 | Branches to look at and merge: LIB_DEV `on-git-or-not` + `window-zoom` (boards, tube, zoom); LIB_GUI `gui-step1`; LIB_MENU `menu-steps`; LIB_EDITOR `editor-cards` (E03-E06); LIB_BIT `cellmap-v3-followups` + `cellmap-v3-checker`; `users-title` in LIB_BIT, LIB_BUILD, LIB_RTS, LIB_SCRIPTBLOCKS, LIB_TTRPG; LIB_GAMES `vector-toss-dangle`; `release-checklist` in LIB_EDITOR and LIB_ig3d | they wait unmerged; I keep working on top of them |
| W-1 | Try the new board menus ("Leave comment...", "Explore here...", Minimize) | none needed |
| W-2 | Look at LIB_GUI `notes.gui` (the GUI builder's first window) | waits |
| W-3 | Game pause menus follow LIB_MENU's rules: in developer mode only, or always? | developer mode only |
| W-4 | The "type Entity. and a space" suggestion window: which face after the small window? | the in-game console (Fable's guess) |
| F-3 | The BitEditor's Heights tab has not been seen on a screen | waits |
| Q-1 | LIB_LOGS file name | `<intention>_<result>_<names>_<seconds>.lib_log` |

## Next (AI)
From the top of `LIB_LLMIN/LIB_DEV/PRIORITY_ORDER.txt` (the owner's order), today:
1. LIB_GUI: a popup kind (right-click menus in .gui; FromStack reads them).
2. LIB_EDITOR cards E07 (half done, uncommitted in the working folder) to E12, E14, E15: an overnight job.
3. cellmap v3: BitEditor Slope tool, pack panel (the E12 checker is done on `cellmap-v3-checker`).
4. Step code for LIB_HOWTO (needs the owner's look at the outline first).
5. The last four Rename Day games, after `vector-toss-dangle` merges.

## Where things live
| Need | Look in |
|---|---|
| What comes first | `LIB_LLMIN/LIB_DEV/PRIORITY_ORDER.txt` (the Priority Tube) |
| The whole project at a glance, blockers | `LIB_DEV/ProjectMap/board.txt` |
| The owner's notes | `python3 -I LIB_DEV/tools/for_review.py feedback`, `LIB_LLMIN/LIB_GAMES/GAME_NOTES.txt` |
| Bugs | `ISSUES/INDEX.md` |
| Finished work | `DONE.md` |
| The open list | `TODO.md` |
