# STATUS

Wednesday, November 18, 2026, midday. Rewritten by Claude (Opus 5.5) on the owner's Project Map
note ("Archive with date range in name, then update this document!"). Everything from 13 to 17 Nov
is in `archive/STATUS_2026-11-13_to_2026-11-17.md`; older plans in `Next_Steps_With_Claude/`.

Where to start a session: the Priority Tube (`LIB_DEV/PriorityTube/NEXT.md`) and the Project Map
(`LIB_DEV/ProjectMap`). This file says what is true today; the tube says what comes first.

## Update 25 November 2026, late (Opus): Pythonizing, the fast translator
- xtalk_py branch `fast-translate` (on phase2-thorough; not merged, not pushed): stack scripts are translated to
  Python before they run (owner's word). Raycasting_101: 12 ms a game step (was 85-125), the window no longer
  freezes (ISSUES 0024). Tests 421 / 847 / 132; survey identical to the interpreter. Waits for his look on screen
  (`tools/open_stack.sh ~/projects/XTJSON/xTalk_Raycasting_101_02_2024_NewMap`), then uDead CullTest.

## Update 25 November 2026 (Opus): Pythonizing, Phase 2 thorough
- xtalk_py branch `phase2-thorough` (13 commits, not merged, not pushed): every harvested stack loads and runs its
  clicks except TKInter-izer 14/15 (its own missing button) and GAD 65/77 (skipped by the owner). Each rule measured
  in LiveCode first; what is done and the open questions: `xtalk_py/docs/HANDOFF_PHASE3.md` ("Phase 2 thorough:
  done so far"). Bug of the day: ISSUES 0023 (script-level globals).

## Update 21 November 2026 (Opus, after /clear)
- Every branch in every repo is merged to main (owner: "merge everything", 20 Nov); the B-1 list below is history. All 46 repos are public in org OXTBox since 21 Nov.
- Owner's two open Project Map notes answered: RELEASE_CHECKLIST.md lives in `LIB_EDITOR/iGame3D_XT/` on main (keep); "face" = which screen shows the Entity. suggestion list (default: in-game command line).
- Priority Tube holds only: Comfy Games app (built and merged, owner to try) and Pythonizing day (his word). Nothing else queued; waiting for his next pick.

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
| LIB_GUI popup kind (right-click menus; FromStack reads them): t41 251 pass, not seen on screen | Opus helper | LIB_GUI `gui-step1` d10143f |
| Users.Title: built apps get no driver head (owner's NEXT.md note); t42 32 pass | Opus | LIB_USERS main |
| Rule: word lists live in LIB_LISTS, LIB_GENERICA refers to them by name (TODO A-66) | owner | LIB_ALPHA map |
| **GAD battles plan** (one page, from the owner's answers): turn-based travel, fights resolve on arrival, optional 3D zoom, one unit by default, rendezvous X (U), send-to points, squads form in one place | Opus + owner | LIB_GAD `gad-battles`; copy `LIB_LLMOUT/LIB_GAD/BATTLES_PLAN_for_review.md` |

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
1. **GAD battles step 2** (`LIB_GAD/BATTLES_PLAN.md` on `gad-battles`, section "Step 2"), when the owner says go (asked 18 Nov, no answer yet).
   Owner's rule for the tube: small and old jobs first; big ones wait at the bottom.
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
