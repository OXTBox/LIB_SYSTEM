# Progress, newest first

Made Wednesday, November 18, 2026 11:01 by `LIB_SYSTEM/tools/progress.py` (run it again to refresh). Last 3 days, every project.

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

## Running (no Claude usage)

| What | Where | State |
|---|---|---|
| Nothing | - | `LIB_DEV/tools/wait_for_tell.sh` runs only while a session is open and the owner is at the keyboard |
| Spark: iGame3D 2008 manifest | Spark's own window | stopped since 13 Nov; restart only when wanted |

## Next (AI)

From the top of `LIB_LLMIN/LIB_DEV/PRIORITY_ORDER.txt` (the owner's order), today:
1. LIB_GUI: a popup kind (right-click menus in .gui; FromStack reads them).
2. LIB_EDITOR cards E07 (half done, uncommitted in the working folder) to E12, E14, E15: an overnight job.
3. cellmap v3: BitEditor Slope tool, pack panel (the E12 checker is done on `cellmap-v3-checker`).
4. Step code for LIB_HOWTO (needs the owner's look at the outline first).
5. The last four Rename Day games, after `vector-toss-dangle` merges.

## Branches waiting for your review

| last commit | project | branch | commits | latest |
|---|---|---|---|---|
| Wed Nov 18, 10:40 | LIB_DEV | `on-git-or-not` (checked out) | 41 | Zoom settled in all four boards (owner, 18 Nov): task and its comment closed |
| Wed Nov 18, 01:21 | LIB_BIT | `cellmap-v3-checker` (checked out) | 3 | cellmap v3: the E12 checker (A-92 5): CellMap.Check / CheckPack and check() / check_pack() |
| Wed Nov 18, 01:09 | LIB_DEV | `window-zoom` | 32 | Window zoom: Shift + wheel stays in the Status Browser only; the tube and the boards get LIB_MENU's Minimize instead |
| Wed Nov 18, 01:09 | LIB_MENU | `menu-minimize` | 3 | LIB_MENU: Minimize, the third line of every menu's ending |
| Wed Nov 18, 01:09 | LIB_MENU | `menu-steps` (checked out) | 3 | LIB_MENU: Minimize, the third line of every menu's ending |
| Tue Nov 17, 23:53 | LIB_EDITOR | `editor-cards` (checked out) | 5 | E06 a door that rises: the door's ceiling goes up 4 hu a step while the hero is near, CellMap.Walk reads it; tests/e06_headless.txt 11 checks on both engines |
| Tue Nov 17, 23:51 | LIB_GUI | `gui-step1` (checked out) | 4 | LIB_GUI Gui.FromStack: read a hand-laid window out of a stack into a .gui file |
| Tue Nov 17, 23:43 | LIB_GAMES | `vector-toss-dangle` (checked out) | 5 | Block City Hustle: SPACE at the ringing booth answers it; cars never parked at a booth; the last booth does not ring first on a new level (A-94, t23) |
| Tue Nov 17, 23:41 | LIB_EDITOR | `cellmap-v3-followups` | 1 | E13 walks the map pack two_rooms (A-92 2) |
| Tue Nov 17, 23:38 | LIB_BIT | `cellmap-v3-followups` | 2 | cellmap v3: slopes drawn in LevelSegments, CellMap.PackSegments (A-92 1) |
| Tue Nov 17, 22:33 | LIB_BIT | `users-title` | 1 | Window titles: ask Users.Title (LIB_USERS) when in use, else "FOR OWNER / ..." |
| Tue Nov 17, 22:33 | LIB_BUILD | `users-title` (checked out) | 1 | Window titles: ask Users.Title (LIB_USERS) when in use, else "FOR OWNER / ..." |
| Tue Nov 17, 22:33 | LIB_RTS | `users-title` (checked out) | 1 | Window titles: ask Users.Title (LIB_USERS) when in use, else "FOR OWNER / ..." |
| Tue Nov 17, 22:33 | LIB_SCRIPTBLOCKS | `users-title` (checked out) | 1 | Window titles: ask Users.Title (LIB_USERS) when in use, else "FOR OWNER / ..." |
| Tue Nov 17, 22:33 | LIB_TTRPG | `users-title` (checked out) | 1 | Window titles: ask Users.Title (LIB_USERS) when in use, else "FOR OWNER / ..." |
| Mon Nov 16, 19:41 | LIB_ig3d | `release-checklist` | 1 | LIB_ig3d README rewritten as the map of the knowledge base: what each file is for and how fresh, what moved to LIB_EDITOR / LIB_DATA / LIB_PUBLIC / LIB_GAD since 12 Nov, duplicates and stale copies listed (nothing deleted); ENGINE_CONTRACT.md named as arriving with engine-contract |
| Mon Nov 16, 19:40 | LIB_EDITOR | `release-checklist` | 2 | RELEASE_CHECKLIST: nothing stated that was not checked (the founding year, Windows versions and WindowLab's code are the owner's to state); file and link counts corrected |

## Every commit, newest first

### Wednesday, November 18

- **10:56** `LIB_USERS` / `main`: **PLAN: Haiku off the save-stacks list for now; models off that list may get their own LIB_LLMOUT/<TAG>/ output folder (owner, 18 Nov)**
- **10:43** `LIB_USERS` / `main`: **Merge users-title: LIB_USERS plan, Users.Title, owner's answers of 18 Nov (main's 17 Nov answers kept as section 10)**
- **10:40** `LIB_DEV` / `on-git-or-not`: **Zoom settled in all four boards (owner, 18 Nov): task and its comment closed**
- **10:35** `LIB_DEV` / `on-git-or-not`: **Project Map: LIB_USERS answers done (18 Nov)**
- **10:35** `LIB_PUBLIC` / `main`: **LAYOUT: saves in Documents/My Games/<Game>, edits in Documents/Vibecode3D/Data (owner, 18 Nov)**
- **10:35** `LIB_USERS` / `users-title`: **Owner's PLAN answers (18 Nov): titles say the role (FOR OWNER), never a name; Users.Tag keeps personas lower case; saves in Documents/My Games**
- **09:54** `LIB_SYSTEM` / `main`: **ISSUES: plain-file ticket tracker; 0001 wsl.exe CPU, 0002 vmmem 4GB, 0003 port 8770 freeze**
- **09:23** `LIB_DEV` / `main`: **The owner moved the stacks into livecode/ (GAME_Browser, its layout, Game_Player_Launcher, Status_Browser_Launcher): fewer like names at the top. The builds, README and the browser's hint follow; GAME_Browser.livecode is rebuilt with the no-freeze script (save it as Game_Browser.exe)**
- **09:23** `LIB_DEV` / `main`: **Game Browser never freezes on the bench: GB.Http talks HTTP over its own socket (wait with messages, busy cursor; ping 1.5 s, run 15 s) instead of shell(curl) with 15 s; programs start with open process (15 ms) instead of shell start (20-50 s on 18 Nov); one bench request at a time; 'already open' said plainly. Tried against the running bench: ping 20 ms, POST /run 20 ms, dead port gives up in 1.5 s, the request after a timeout works**
- **09:23** `LIB_DEV` / `on-git-or-not`: **The owner moved the stacks into livecode/ (GAME_Browser, its layout, Game_Player_Launcher, Status_Browser_Launcher): fewer like names at the top. The builds, README and the browser's hint follow; GAME_Browser.livecode is rebuilt with the no-freeze script (save it as Game_Browser.exe)**
- **09:12** `LIB_COMFY` / `comfy-genres`: **PLAN_STANDALONE: the owner's direction (keep Comfy games apart, isolated genre system, public and effortless)**
- **09:11** `LIB_COMFY` / `comfy-genres`: **Comfy games live in LIB_COMFY/games, apart from the hand-made games in LIB_GAMES**
  Build Game (and the kits) now write to LIB_COMFY/games by default; save_to keeps the LIB_GAMES
  choice so old workflows still load. The workflows pick the new folder. The 21 kit-made games the
  owner tested move here; one ComfyPong demo stays in LIB_GAMES as the teaser.
- **09:11** `LIB_GAMES` / `main`: **Comfy games move to LIB_COMFY/games; ComfyPong1 stays here as the one demo (owner: the kit-made games would clutter the hand-made prototypes)**
- **09:06** `LIB_PORTS` / `main`: **The Ports window (Ports.oxtstack, script in livecode/ports_window.livecodescript): every registered port, who listens, whether it answers, Close older copy (wmic start times, asks first), Edit registry, the next free port. lib_ports: AllListeners (one netstat), NextFree. Tried: all 8 ports right; start times read for two live processes**
- **09:04** `LIB_DEV` / `on-git-or-not`: **Game Browser never freezes on the bench: GB.Http talks HTTP over its own socket (wait with messages, busy cursor; ping 1.5 s, run 15 s) instead of shell(curl) with 15 s; programs start with open process (15 ms) instead of shell start (20-50 s on 18 Nov); one bench request at a time; 'already open' said plainly. Tried against the running bench: ping 20 ms, POST /run 20 ms, dead port gives up in 1.5 s, the request after a timeout works**
- **09:04** `LIB_MCP` / `main`: **DevServer.Start looks before it listens (LIB_PORTS rule 2): when another process listens on the port (netstat), it does not start, leaves the token file alone, and returns 'DevServer: IN USE: ...'; the standalone launcher then closes the new copy. 18 Nov: two benches on 8770, the second overwrote the token. Tried: Start 8770 beside the running bench -> IN USE, token untouched**
- **09:04** `LIB_PORTS` / `main`: **Rule 3: sockets not shell(curl), open process not start, leave a timed-out socket to settle; Ports.Answers does that (error 10038 on the next socket otherwise)**
- **09:04** `xt3D_Raylib_Livecode_Bridge` / `master`: **Bench launchers: when DevServer.Start says the port is IN USE (another bench runs), show why and close this copy in 5 s instead of opening a bench with no server. Needs LIB_MCP one-copy-per-port; takes effect when the benches are next built**
- **09:03** `LIB_COMFY` / `comfy-genres`: **PLAN_STANDALONE: a stand-alone Comfy Games app (genre menu, games menu, star ratings, sort by stars and date); waits until other projects clear**
- **09:02** `LIB_GAMES` / `main`: **ComfyUI games: 20 games made by the genre kit nodes (Bricks, Waves, Worm, Dodge, Lander, Rocks, Pong), each workflow's default and two seeds; owner tested the node output 18 Nov**
- **08:36** `LIB_PORTS` / `main`: **LIB_PORTS: the port registry (ports.tsv), RULES.md, lib_ports.livecodescript (Listeners from netstat, Answers, MayListen) and tools/ports_check.py (live, scan). Tried live: finds both xt3d-bench-mcp copies on 8770; scan finds no unregistered ports**
- **07:54** `LIB_COMFY` / `comfy-genres`: **install.sh: copy the kits/ folder too (the pack imports it; without it ComfyUI fails to load the pack)**
- **07:30** `LIB_GAMES` / `rename-day-games`: **uDead: a targeted person's strobe and every change of look recolour the figure in place (Entity.SetColor, Entity.SetMesh) instead of killing and respawning it every half second; an empty ammo crate goes grey the same way. Headless on the real engine: targets strobe both reds, the drawn colour is the tint, a living figure keeps its id (the old script respawned 14 times in 600 steps)**
- **07:30** `LIB_GAMES` / `rename-day-games`: **Stand-ins: Entity.SetColor, and Entity.Get(pId, "color") (contract_check --stubs: exactly the contract)**
- **07:30** `LIB_ig3d` / `main`: **Entity.SetColor pId, pColor (the owner: no textures, so colour is how a game marks things; uDead's targets). Moves the object to the new colour's batch graphic; Entity.Get(pId, "color") reads it back (the spawn colour until recoloured). XT and xRay yes; words regenerated. Tried on the real engine headless: Game Player drawing and the xRay frame both show the new colour, the old batch clears, mesh and place stay**
- **07:30** `xt3D_Raylib_Livecode_Bridge` / `entity-setcolor`: **Engine made again with LIB_ig3d's Entity.SetColor (contract_calls); nothing else changed**
- **03:19** `LIB_COMFY` / `comfy-genres`: **Genre kit: Rock Blaster (Blaster Ship, Rock Field, Saucer, Rock Rules); autopilots that aim; Ball dice**
  Rock Blaster: turn, thrust and drift through wrapping space; rocks split big > middle > small; a saucer
  crosses and shoots; one more rock each level; an extra ship every N points. workflows/rocks_variants.json.
  The brick autopilot aims at the lowest brick (without it the ball could climb the same gap for ever),
  the wave autopilot leads its target and steps aside from bombs. Ball's speed-up dice: every kit but Pong
  rolls only the part above 1 (Pong unchanged: seed 2102167373 makes the same ComfyPong).
  tests/kit_play_test.py passes for seeds 1 to 10 (18 checks each, six kits); with ComfyUI's own Python
  and torch: 31 nodes, all widget defaults in range, every API workflow runs node by node.
- **03:06** `LIB_COMFY` / `comfy-genres`: **Genre kit: Lander (Lander Craft, Ground, Lander Rules; Vibecode3D/Lander)**
  Rotate-and-burn or slide craft, fuel, ground of segments with pads 1 to 3 segments wide (narrow pads
  score up to three times), stronger pull and wind level by level; the thrust is raised when it could
  not beat the last level's pull. Lander.TestAuto flies to the nearest pad: the small chain lands all
  three levels on the stand-ins; the full one plays 900 steps; it runs and draws on the real engine.
  workflows/lander_variants.json.
- **03:03** `LIB_COMFY` / `comfy-genres`: **README and NOTES: the genre kits, how they were tested without ComfyUI, the dangling-else trap, adding a kit**
- **03:02** `LIB_COMFY` / `comfy-genres`: **Genre kits: chains as data (tools/kit_chains.py), a workflow file per kit, a headless play test**
  tools/make_kit_workflows.py writes workflows/<kit>_variants.json (drag in) and _api.json (POST /prompt)
  for brick, wave, coil and dodge, widget order read from the nodes. tests/kit_play_test.py builds every
  kit and plays it in OXT-Beyond's headless engine: the small chain past level 1 on the stand-ins with the
  autopilot, the full chain 900 steps, and the full game in the Game Player on the bridge engine (12 of 12).
  preview.py loads PIL only when it draws, so plain python3 builds games. The kit registry imports its
  kits plainly again (a broken kit should fail loudly).
  Checked with ComfyUI's own Python and torch: 24 nodes, every widget default in range, each API workflow
  run node by node gives a game and a [1,600,900,3] preview; the Pong workflow gives ComfyPong1 unchanged.
- **02:59** `LIB_COMFY` / `comfy-genres`: **Genre kit: Lane Dodger (Runner, Hazard, Pickup, Dodge Rules; Vibecode3D/Lane Dodger)**
  Lanes (one press a lane) or free running, keys or the mouse; hazard kinds with speed, rate, wobble and spin;
  pickups coin, shield, slow time, extra life; the floor scrolls by its own pattern's period. Dodge.TestAuto
  picks the safest lane or place; on the stand-ins the small chain runs all three levels, the full one into
  level 2, and it runs and draws on the real engine.
- **02:56** `LIB_COMFY` / `comfy-genres`: **Genre kit: Grid Worm (Worm Board, Worm, Food, Worm Rules; Vibecode3D/Grid Worm)**
  Walls or wrapping edges, scattered / bar / box blocks that grow each level, food kinds plain, gold (moves
  when its time is up), shrink and slow. Coil.TestAuto finds the nearest food breadth first; with it both test
  chains eat their way through all three levels on the stand-ins, and it runs and draws on the real engine.
  The worm is one colour: an entity keeps the colour it was spawned with (no Entity.SetColor in the contract).
- **02:51** `LIB_COMFY` / `comfy-genres`: **Genre kits: Brick Breaker and Wave Shooter, a shared Arena node, and parts/common/vec (wire shapes, floors, keys, mouse)**
  New nodes: Arena (Vibecode3D/Shared); Brick Wall, Bat, Power-Up, Breaker Rules (Vibecode3D/Brick Breaker);
  Shooter Ship, Enemy Wave, Shields, Wave Rules (Vibecode3D/Wave Shooter). Palette and Ball carry over.
  kits/ holds one module a kit (settings, fix-ups, config, header, preview); Build Game sends every kit but
  Pong there, Pong is unchanged. tests/kit_test.py builds each chain through the node classes.
  Tested headless: both compile and play on the stand-ins (autopilot hooks Brick.TestAuto / Wave.TestAuto:
  the small brick wall is cleared level after level) and run and draw on the real engine.
- **02:40** `LIB_COMFY` / `comfy-genres`: **Rename Day: the cpong parts take the new names (Camera.Reset, Mesh.Box, Entity.SetPosition); a game made from them at seed 2102167373 is the moved LIB_GAMES copy, line for line. Needs an engine with the aliases (the V: install from 16 Nov has none: refresh it first)**
- **02:40** `LIB_GAMES` / `rename-day-games`: **Rename Day: ComfyPong2102167373 takes the new names (7 places); made by LIB_COMFY: its parts take the same names on LIB_COMFY branch comfy-genres, and the game made again from them at this seed is this file. Headless: same end state as before on the stand-ins (300 frames, one seed) and the same picture on the real engine (120 frames)**
- **02:40** `LIB_GAMES` / `rename-day-games`: **Rename Day: ComfyPong1 takes the new names (6 places); made by LIB_COMFY: its parts take the same names on LIB_COMFY branch comfy-genres, and the game made again from them at this seed is this file. Headless: same end state as before on the stand-ins (300 frames, one seed) and the same picture on the real engine (120 frames)**
- **02:39** `LIB_EDITOR` / `main`: **Rename Day: Ig3dEditor takes the new names (28 places); Engine.SetCam turned round to Camera.SetPosition (the orbit view: same sign change as the alias, so the same picture); gCameraYaw/Pitch writes -> Camera.SetLook; unused engine globals dropped. Same picture on the real engine (120 frames); t20 and t37 pass on the moved script**
- **02:39** `LIB_GAD` / `main`: **Rename Day: GeneticAnomaly takes the new names (7 places); both Engine.SetCam lines turned round to Camera.SetPosition; unused engine globals dropped. Same picture on the real engine (120 frames); t14, t15 pass on the moved script**
- **02:38** `LIB_GAMES` / `rename-day-games`: **Rename Day: Thrmnlra takes the new names (14 places); both Engine.SetCam lines turned round; camera writes -> Camera.SetLook; Thrm.SetMesh -> Entity.SetMesh (keeps the old radius); Thrm.FindFile retired for Game.FindFile (it climbed 8 folders); unused engine globals dropped. Same end state on the stand-ins. Mat3/ProjectVertex, gMeshCache and its own controls left**
- **02:38** `LIB_GAMES` / `rename-day-games`: **Rename Day: uDead takes the new names (9 places); Engine.SetCam turned round (by hand: sPX * kM, -kEye * kM, sPZ * kM); camera put-writes -> Camera.SetLook; uDead.SetMesh -> Entity.SetMesh (keeps the old radius); uDead.FindFile retired for Game.FindFile; unused engine globals dropped. Same end state on the stand-ins, same picture on the real engine. Mouse look and cursor lock left**
- **02:38** `LIB_GAMES` / `rename-day-games`: **Rename Day: Amazing_Couple takes the new names (9 places); Engine.SetCam turned round; camera writes -> Camera.SetLook; Couple.SetMesh -> Entity.SetMesh (keeps the old radius); Couple.FindFile retired for Game.FindFile (same search, plus more); unused engine globals dropped. Same end state on the stand-ins and picture on the real engine against the old names with the same two edits**
- **02:38** `LIB_GAMES` / `rename-day-games`: **Rename Day: Antack takes the new names (19 places); Engine.SetCam turned round; camera writes -> Camera.SetLook; Antack.SetMesh -> Entity.SetMesh (keeps the old radius); Antack.FindFile retired for Game.FindFile (it climbed 8 folders, Game.FindFile 6 plus the engine's and the projects folder); unused engine globals dropped. Same picture on the real engine. Xform.Object (Antack.ScreenOf) and the mouse left**
- **02:38** `LIB_GAMES` / `rename-day-games`: **Rename Day: AntackFresh takes the new names (19 places); Engine.SetCam turned round; camera writes -> Camera.SetLook; Antack.SetMesh -> Entity.SetMesh (keeps the old radius); unused engine globals dropped. Same end state on the stand-ins, same picture on the real engine, t28 9/9. Xform.Object (Antack.ScreenOf) and the mouse left**
- **02:38** `LIB_GAMES` / `rename-day-games`: **Rename Day: Canyon takes the new names (15 places); Engine.SetCam turned round to Camera.SetPosition; gCameraYaw/Pitch writes -> Camera.SetLook, their globals dropped. Same picture on the real engine (120 frames). Its engine-table debts (Scene.Register, Scene.ColorGraphic, gObjectTransforms) left for their own visit**
- **02:38** `LIB_GAMES` / `rename-day-games`: **Rename Day: Hunter takes the new names (26 places); Engine.SetCam turned round to Camera.SetPosition; gCameraYaw/Pitch put-writes -> Camera.SetLook. Same picture on the real engine (120 frames); t48 passes with the moved script on the current engine. Its engine-table debts (Scene.AddObject, RayCastScene, gObjectTransforms) and mouse look are left for their own visit**
- **02:35** `LIB_GAMES` / `rename-day-games`: **Rename Day: DeadDays takes the new names (15 places); Engine.SetCam turned round to Camera.SetPosition; gCameraYaw/Pitch writes -> Camera.SetLook; unused engine globals dropped. Headless: same end state on the stand-ins (300 frames), t36 passes on the current engine (19/19); on the real engine DeadDays draws differently run to run before and after. DD.FindTool kept (another folder layout than Game.FindFile)**
- **02:35** `LIB_GAMES` / `rename-day-games`: **Rename Day: DotMaze takes the new names (9 places); unused engine globals dropped. Headless: same end state as before on the stand-ins (300 frames, one seed); on the real engine DotMaze draws differently run to run before and after (not a rename difference)**
- **02:35** `LIB_GAMES` / `rename-day-games`: **Rename Day: SquadBuggy takes the new names (33 places); the mouseH/V -> Engine.Mouse in Squad.MousePoint. Headless: same end state as before on the stand-ins (300 frames, one seed) and the same picture on the real engine (120 frames)**
- **02:35** `LIB_GAMES` / `rename-day-games`: **Rename Day: ProbeVsCone takes the new names (24 places); the mouseLoc -> Engine.Mouse. Headless: same end state as before on the stand-ins (300 frames, one seed) and the same picture on the real engine (120 frames)**
- **02:35** `LIB_GAMES` / `rename-day-games`: **Rename Day: InterceptorRun takes the new names (23 places); unused engine globals dropped. Headless: same end state as before on the stand-ins (300 frames, one seed) and the same picture on the real engine (120 frames)**
- **02:35** `LIB_GAMES` / `rename-day-games`: **Rename Day: CraterCrawler takes the new names (19 places); unused engine globals dropped. Headless: same end state as before on the stand-ins (300 frames, one seed) and the same picture on the real engine (120 frames)**
- **02:35** `LIB_GAMES` / `rename-day-games`: **Rename Day: NeonDriftWastes takes the new names (17 places); unused engine globals dropped. Headless: same end state as before on the stand-ins (300 frames, one seed) and the same picture on the real engine (120 frames)**
- **02:35** `LIB_GAMES` / `rename-day-games`: **Rename Day: GridSprint takes the new names (15 places); unused engine globals dropped. Headless: same end state as before on the stand-ins (300 frames, one seed) and the same picture on the real engine (120 frames)**
- **02:35** `LIB_GAMES` / `rename-day-games`: **Rename Day: LightTrailArena takes the new names (14 places); Engine.SetCam turned round to Camera.SetPosition; gCameraYaw/Pitch writes -> Camera.SetLook; unused engine globals dropped. Headless: same end state as before on the stand-ins (300 frames, one seed) and the same picture on the real engine (120 frames)**
- **02:35** `LIB_GAMES` / `rename-day-games`: **Rename Day: FareDash takes the new names (14 places); unused engine globals dropped. Headless: same end state as before on the stand-ins (300 frames, one seed) and the same picture on the real engine (120 frames)**
- **02:35** `LIB_GAMES` / `rename-day-games`: **Rename Day: PromptAndGlazeMaze takes the new names (13 places); unused engine globals dropped. Headless: same end state as before on the stand-ins (300 frames, one seed) and the same picture on the real engine (120 frames)**
- **02:35** `LIB_GAMES` / `rename-day-games`: **Rename Day: FuelLine takes the new names (13 places); unused engine globals dropped. Headless: same end state as before on the stand-ins (300 frames, one seed) and the same picture on the real engine (120 frames)**
- **02:35** `LIB_GAMES` / `rename-day-games`: **Rename Day: CoastRoad takes the new names (13 places); unused engine globals dropped. Headless: same end state as before on the stand-ins (300 frames, one seed) and the same picture on the real engine (120 frames)**
- **02:35** `LIB_GAMES` / `rename-day-games`: **Rename Day: VineRun takes the new names (12 places); unused engine globals dropped. Headless: same end state as before on the stand-ins (300 frames, one seed) and the same picture on the real engine (120 frames)**
- **02:35** `LIB_GAMES` / `rename-day-games`: **Rename Day: VectorBlobApocalypse takes the new names (11 places); Engine.SetCam turned round to Camera.SetPosition; gCameraYaw/Pitch writes -> Camera.SetLook; unused engine globals dropped. Headless: same end state as before on the stand-ins (300 frames, one seed) and the same picture on the real engine (120 frames)**
- **02:35** `LIB_GAMES` / `rename-day-games`: **Rename Day: TrenchRun takes the new names (11 places); Engine.SetCam turned round to Camera.SetPosition; gCameraYaw/Pitch writes -> Camera.SetLook; unused engine globals dropped. Headless: same end state as before on the stand-ins (300 frames, one seed) and the same picture on the real engine (120 frames)**
- **02:35** `LIB_GAMES` / `rename-day-games`: **Rename Day: ShaftDescent takes the new names (11 places); Engine.SetCam turned round to Camera.SetPosition; unused engine globals dropped. Headless: same end state as before on the stand-ins (300 frames, one seed) and the same picture on the real engine (120 frames)**
- **02:35** `LIB_GAMES` / `rename-day-games`: **Rename Day: BigBallOfVectors takes the new names (11 places); Engine.SetCam turned round to Camera.SetPosition; gCameraYaw/Pitch writes -> Camera.SetLook; unused engine globals dropped. Headless: same end state as before on the stand-ins (300 frames, one seed) and the same picture on the real engine (120 frames)**
- **02:35** `LIB_GAMES` / `rename-day-games`: **Rename Day: TabletopRacers takes the new names (10 places); unused engine globals dropped. Headless: same end state as before on the stand-ins (300 frames, one seed) and the same picture on the real engine (120 frames)**
- **02:35** `LIB_GAMES` / `rename-day-games`: **Rename Day: SkyRaiders takes the new names (10 places); unused engine globals dropped. Headless: same end state as before on the stand-ins (300 frames, one seed) and the same picture on the real engine (120 frames)**
- **02:35** `LIB_GAMES` / `rename-day-games`: **Rename Day: RockField takes the new names (10 places); unused engine globals dropped. Headless: same end state as before on the stand-ins (300 frames, one seed) and the same picture on the real engine (120 frames)**
- **02:35** `LIB_GAMES` / `rename-day-games`: **Rename Day: RampRider takes the new names (9 places); unused engine globals dropped. Headless: same end state as before on the stand-ins (300 frames, one seed) and the same picture on the real engine (120 frames)**
- **02:35** `LIB_GAMES` / `rename-day-games`: **Rename Day: JaiAlaiBlock takes the new names (9 places); unused engine globals dropped. Headless: same end state as before on the stand-ins (300 frames, one seed) and the same picture on the real engine (120 frames)**
- **02:35** `LIB_GAMES` / `rename-day-games`: **Rename Day: DodgeTunnel takes the new names (9 places); unused engine globals dropped. Headless: same end state as before on the stand-ins (300 frames, one seed) and the same picture on the real engine (120 frames)**
- **02:35** `LIB_GAMES` / `rename-day-games`: **Rename Day: BounceRally takes the new names (9 places); unused engine globals dropped. Headless: same end state as before on the stand-ins (300 frames, one seed) and the same picture on the real engine (120 frames)**
- **02:29** `LIB_GAMES` / `rename-day-games`: **Rename Day: Face takes the new names (3 places); unused engine globals dropped; its own Face.FindFile retired for Game.FindFile. Headless the end state differs from before on purpose: the stand-in Game.FindFile finds the face file, so the face is now built (before: FACE: LIB_MCP NOT FOUND)**
- **02:29** `LIB_GAMES` / `rename-day-games`: **Rename Day: WreckRing takes the new names (8 places); unused engine globals dropped. Headless: same end state as before on the stand-ins (300 frames, one seed)**
- **02:29** `LIB_GAMES` / `rename-day-games`: **Rename Day: VectorPong3D takes the new names (8 places); unused engine globals dropped. Headless: same end state as before on the stand-ins (300 frames, one seed)**
- **02:29** `LIB_GAMES` / `rename-day-games`: **Rename Day: MatrixLock takes the new names (8 places); Engine.SetCam turned round to Camera.SetPosition; gCameraYaw/Pitch writes -> Camera.SetLook; unused engine globals dropped. Headless: same end state as before on the stand-ins (300 frames, one seed)**
- **02:29** `LIB_GAMES` / `rename-day-games`: **Rename Day: DeepDive takes the new names (8 places); unused engine globals dropped. Headless: same end state as before on the stand-ins (300 frames, one seed)**
- **02:29** `LIB_GAMES` / `rename-day-games`: **Rename Day: WallBreaker takes the new names (7 places); unused engine globals dropped. Headless: same end state as before on the stand-ins (300 frames, one seed)**
- **02:29** `LIB_GAMES` / `rename-day-games`: **Rename Day: LongWorm takes the new names (7 places); unused engine globals dropped. Headless: same end state as before on the stand-ins (300 frames, one seed)**
- **02:29** `LIB_GAMES` / `rename-day-games`: **Rename Day: CityShield takes the new names (7 places); unused engine globals dropped. Headless: same end state as before on the stand-ins (300 frames, one seed)**
- **02:29** `LIB_GAMES` / `rename-day-games`: **Rename Day: BatDuel takes the new names (7 places); unused engine globals dropped. Headless: same end state as before on the stand-ins (300 frames, one seed)**
- **02:29** `LIB_GAMES` / `rename-day-games`: **Rename Day: FloppyFlynn takes the new names (6 places); unused engine globals dropped. Headless: same end state as before on the stand-ins (300 frames, one seed)**
- **02:29** `LIB_GAMES` / `rename-day-games`: **Rename Day: CrossTraffic takes the new names (6 places); unused engine globals dropped. Headless: same end state as before on the stand-ins (300 frames, one seed)**
- **02:29** `LIB_GAMES` / `rename-day-games`: **Rename Day: StackDown takes the new names (4 places); unused engine globals dropped. Headless: same end state as before on the stand-ins (300 frames, one seed)**
- **02:29** `LIB_GAMES` / `rename-day-games`: **Rename Day: SoftLanding takes the new names (4 places); unused engine globals dropped. Headless: same end state as before on the stand-ins (300 frames, one seed)**
- **02:29** `LIB_GAMES` / `rename-day-games`: **Rename Day: Simple_Test1 takes the new names (4 places); unused engine globals dropped. Headless: same end state as before on the stand-ins (300 frames, one seed)**
- **02:27** `LIB_ig3d` / `main`: **rename_day.py: moves a game to the Rename Day names in code only; Engine.SetCam lines turned round only with --setcam, each printed; quoted text, own handlers and the debts (mouseLoc, gCameraYaw/Pitch writes, own FindFile) listed for the hand. test_rename_day.py: 29 checks**
- **02:17** `LIB_DEV` / `on-git-or-not`: **Project Map: contract-calls merged**
- **02:14** `LIB_DEV` / `on-git-or-not`: **Project Map: the contract's new calls on contract-calls, waiting for the owner**
- **02:14** `LIB_DEV` / `main`: **Game Player says gV3DEdition XT (and no optional parts) before Vibe.Begin, for Engine.Info("edition") and Engine.Has**
- **02:14** `LIB_GAMES` / `rename-day-games`: **Stand-ins for the contract's new calls (Camera.SetLook, Camera.WorldToScreen, Entity.Set/Get/SetMesh, Scene.Objects, Mesh.Has, Engine.Has, Engine.Mouse, Game.FindFile) and Engine.Info edition**
- **02:14** `LIB_ig3d` / `main`: **The contract's new calls (A-93, A-96) under their final names: Camera.SetLook (with roll), Camera.WorldToScreen, Entity.Set/Get/SetMesh, Scene.Objects, Mesh.Has, Engine.Has, Engine.Mouse, Game.FindFile, Engine.Info("edition"). livecode/contract_calls.livecodescript, appended to the engine by xt3d's make_vibe_xt3d.py; XT and xRay cells yes; words regenerated**
- **02:14** `xt3D_Raylib_Livecode_Bridge` / `entity-setcolor`: **make_vibe_xt3d.py appends LIB_ig3d's contract_calls after the overrides (same replace rule); engine made again; the games bench says gV3DEdition xRay. Tried in the games bench: edition, roll, WorldToScreen, FindFile**
- **02:06** `LIB_DEV` / `on-git-or-not`: **Project Map: LIB_INPUT merged (the owner's yes)**
- **02:06** `LIB_INPUT` / `main`: **NEXT: merged to main, the owner's yes**
- **02:03** `LIB_DEV` / `on-git-or-not`: **Project Map rebuilt: the input-steps branches show for review**
- **02:03** `LIB_DEV` / `on-git-or-not`: **Project Map 18 Nov: Rename Day merged (NOW, xt3d, LIB_ig3d cards), LIB_INPUT and LIB_SFX cards; maps rebuilt; the owner's tube comment**
- **02:03** `LIB_INPUT` / `main`: **NEXT: its pieces in other repos are on input-steps branches made from main**
- **02:03** `LIB_ig3d` / `main`: **Contract: Input. in the libraries table (LIB_INPUT). Written by Fable with LIB_INPUT**
- **02:03** `LIB_DEV` / `main`: **Game Player: LIB_INPUT for a game with an actions file (Player.LoadInput, Input.Poll each step, ... > Controls...). Written by Fable with LIB_INPUT, committed apart from on-git-or-not**
- **02:03** `LIB_GAMES` / `rename-day-games`: **Hunter: its actions file for LIB_INPUT; reads the actions when LIB_INPUT is there, key codes otherwise. Written by Fable with LIB_INPUT**
- **02:01** `LIB_SFX` / `main`: **LIB_SFX with xt3d: several sounds at once through raylib's mixer (8 presets together, overlapping alias copies with pan and pitch). demos/sfx_xt3d_cacophony.livecodescript; README notes it runs in the xt3d bench, not LIB_MCP's standalone**
- **01:50** `LIB_SYSTEM` / `main`: **LIB_ALPHA map: LIB_SFX (owner, 18 Nov: "LIB_SFX goes in, it's important")**
- **01:49** `LIB_SFX` / `main`: **LIB_SFX: an xTalk bridge to rfxgen (sfxr sound effects). xtsfx.dll + xtsfx.lcb, the Sfx. script library, a demo, a 30-check test**
- **01:21** `LIB_BIT` / `cellmap-v3-checker`: **cellmap v3: the E12 checker (A-92 5): CellMap.Check / CheckPack and check() / check_pack()**
  One line a problem (kind, map id, col,row, plain words): slope traps, all corners lifted, a slope
  on an empty cell or through a roof, a step that cuts an area off, a hole with nothing under it,
  a door onto a cell nobody can stand on, a link without a target, no start, and every area nobody
  can walk to (the walker's rules cell by cell, stacked maps together, doors and teleports joined).
  Same lines in Python and xTalk on every map in maps/ and two made-bad test maps:
  py_check_test 22 checks, lc_check_test 26 (beyond and server engines); v2 and v3 tests unchanged.
- **01:13** `LIB_INPUT` / `main`: **LIB_INPUT: actions, presets, profiles and the two settings faces**
  Steps 1-5 of PLAN.md: the library (lib_input), four shipped presets, the app
  face and the developer face (.gui, shown by LIB_GUI). Tested by
  OXT-BEYOND/tests/t48_lib_input.txt (113 checks, both engines).
- **01:09** `LIB_DEV` / `window-zoom`: **Window zoom: Shift + wheel stays in the Status Browser only; the tube and the boards get LIB_MENU's Minimize instead**
  The owner (18 Nov): the wheel is already the tube's scroll and the map's zoom, and Shift was
  ignored there; minimizing to a small widget from the menu is the better way (LIB_MENU branch
  menu-minimize). The Status Browser keeps the owner's own handlers.
- **01:09** `LIB_MENU` / `menu-minimize`: **LIB_MENU: Minimize, the third line of every menu's ending**
  The owner (18 Nov): minimize to a small widget-sized window from a line at the bottom of the popup,
  and any mouse down on the mini window brings it back. Menu.Minimize scales the window down to
  about 220 pixels wide (the whole app still showing) under a clear cover that takes the next
  mouse down; Menu.Restore puts back the size and place. Every app that routes its ending through
  Menu.EndPick gets it with no change. Headless t43: 69 pass (14 new).
- **00:57** `LIB_DEV` / `window-zoom`: **Window zoom: Shift + mouse wheel scales the whole window in the Status Browser, the Priority Tube, the Project Map and On Git or Not**
  The owner's mouseWheelScroll and rawKeyDown from Status_Browser.livecode (15 Nov) copied into
  status_browser.livecodescript (bubble n-7bcf81f6); the same zoom added to priority_tube and
  board_canvas, where the plain wheel keeps its job. Headless: t13 26, t39 89, t40 52, new t47 15 pass.
- **00:45** `LIB_ig3d` / `rename-day`: **Rename Day plan: the owner confirms Camera.SetPosition takes the camera's real place**
- **00:38** `LIB_ig3d` / `rename-day`: **Rename Day plan: the owner's yes to the three Scene -> Entity moves (everything being an entity)**
- **00:26** `LIB_ig3d` / `rename-day`: **Suggestion window: opens in the middle of the screen (it landed half off the top left in OXT-Beyond)**
- **00:25** `LIB_ig3d` / `rename-day`: **Rename Day step 2: the renames table in the contract (new names in the tables, a Camera section), make_names.py (aliases, suggestion words, Contract menu, all from the contract), the checker taught the old and new names, lib_suggest and its small window**
- **00:25** `xt3D_Raylib_Livecode_Bridge` / `rename-day`: **Rename Day: make_vibe_xt3d.py appends the contract aliases (LIB_ig3d/livecode/contract_aliases.livecodescript); the engine made again with them. This also brings in the engine source's variable renames of 15 Nov (Vibecode3D cd5560c)**
- **00:14** `LIB_ig3d` / `rename-day`: **Rename Day plan: owner's answers 18 Nov (Get/Set stay; old names gone before release)**
- **00:11** `LIB_ig3d` / `rename-day`: **Rename Day plan: Camera. gets its own group (owner, 18 Nov); Camera.SetPosition takes the camera's real place**
- **00:01** `LIB_ig3d` / `rename-day`: **Rename Day plan (step 1): RENAME_DAY.md, the old -> new name table, aliases, game order, the suggestion list. For the owner's yes; no code yet.**
### Tuesday, November 17

- **23:54** `LIB_DEV` / `window-zoom`: **NEXT: popup kind, E07 half done, Status Browser handlers; for a fresh session**
- **23:53** `LIB_EDITOR` / `editor-cards`: **E06 a door that rises: the door's ceiling goes up 4 hu a step while the hero is near, CellMap.Walk reads it; tests/e06_headless.txt 11 checks on both engines**
- **23:52** `LIB_DEV` / `window-zoom`: **Gui.FromStack done**
- **23:51** `LIB_GUI` / `gui-step1`: **LIB_GUI Gui.FromStack: read a hand-laid window out of a stack into a .gui file**
  Gui.FromStack / Gui.FromStackToFile (.gui paths only; reads, never writes a stack).
  Built controls keep their kind and options; hand controls get kinds from type and style;
  unmappable ones become '# unknown:' lines. Round trip of stage3.gui and notes.gui exact.
  gui/status_browser_from_stack.gui: the owner's Status Browser, 7 of 8 controls mapped.
  t41_lib_gui: 221 checks pass on both engines.
- **23:51** `LIB_EDITOR` / `editor-cards`: **E05 slopes: I J K L lift an edge, 1-4 a corner, Shift lowers, 0 flattens, tidy into the floor, steep shown; drawn by LevelSegments; tests/e05_headless.txt 15 checks on both engines**
- **23:50** `LIB_EDITOR` / `editor-cards`: **E04 ceilings: W / S move a cell's roof, T roofs the ~ tunnel, air under the roof shown; tests/e04_headless.txt 14 checks on both engines**
- **23:50** `LIB_DEV` / `window-zoom`: **Tube reloaded with LIB_MENU menu; Status Browser handler copy sized**
- **23:49** `LIB_DEV` / `window-zoom`: **Priority Tube and Status Browser use LIB_MENU: right-click menus end with Leave comment / Explore here**
  Priority Tube: right-click a bubble = Move to top / Move to bottom / Remove from the tube, then
  LIB_MENU's ending; comments go to BOARD_COMMENTS.txt (board PRIORITY TUBE, target = bubble id);
  Explore here opens the bubble's part folder or source file. Status Browser: the file menu ends the
  same way (board STATUS BROWSER, target = the file's path). Both load LIB_MENU themselves and work
  without it (plain menus, no error). Tests: t40 52 checks, t13 26 (now in its own folder _work_t13).
- **23:49** `LIB_EDITOR` / `editor-cards`: **E03 elevation colours: the map coloured by height (Forge's elevation view); maps for the cards (tools/make_card_maps.py); tests/e03_headless.txt 10 checks on both engines**
- **23:43** `LIB_DEV` / `window-zoom`: **cellmap v3 follow-ups done; BVH title blocker cleared; next sized**
- **23:43** `LIB_DEV` / `window-zoom`: **LIB_MENU steps 1-2 done, boards reloaded with LIB_MENU; next sized**
- **23:43** `LIB_SYSTEM` / `main`: **TODO: A-92 (1)(2) and A-94 done on branches for review**
- **23:43** `LIB_MENU` / `menu-minimize`: **README/NEXT: boards work with or without LIB_MENU**
- **23:43** `LIB_GAMES` / `vector-toss-dangle`: **Block City Hustle: SPACE at the ringing booth answers it; cars never parked at a booth; the last booth does not ring first on a new level (A-94, t23)**
  t23 'never the same booth twice running' failed about one run in three: a parked car
  beside the ringing booth took the SPACE press (the job never started), and a new level
  forgot which booth had just rung. 40 runs of t23 clean on both headless engines after.
- **23:43** `LIB_DEV` / `window-zoom`: **Boards work without LIB_MENU: every Menu.* call guarded (pmMenuOn)**
  Without the library: plain menus (no ending), the help bar says Menus need LIB_MENU, records
  are written by the board itself, Explore says the path. t39 89 pass (6 new, board run with
  LIB_MENU absent), t43 57 pass; real inbox md5 unchanged.
- **23:42** `LIB_DEV` / `window-zoom`: **LIB_GUI stage 3 done (seen on screen); FromStack next, sized**
- **23:41** `LIB_GUI` / `gui-step1`: **LIB_GUI stage 3: panel, slider, tabs, view; resizing by stick= (Gui.Resize)**
  Panels are groups widgets go in= (places count from the panel); sliders are
  scale scrollbars (fractions via 0..1000 inside); tabs are LIB_THEME drawn tabs
  that show and hide tab= pages; a view is a placeholder box that gives its rect
  and fires a click point. Built windows lay out again on resizeStack.
  Example gui/stage3.gui; NEXT.md says how to open it.
- **23:41** `LIB_EDITOR` / `cellmap-v3-followups`: **E13 walks the map pack two_rooms (A-92 2)**
  M cycles to two_rooms: drawn with CellMap.PackSegments, walked with PackWalk (stairs up
  through the loft's hole, the sloped ramp to the goal, down the hole), E takes a door or
  ladder (PackDoors / PackEnter). tests/e13_headless.txt: the old ten scenes plus the pack,
  20 PASS on the OXT-Beyond headless engine.
- **23:41** `LIB_DEV` / `window-zoom`: **Boards use LIB_MENU: ending, safe labels, record lines and Explorer from lib_menu**
  board_canvas loads ~/projects/LIB_MENU/livecode/lib_menu.livecodescript itself (pmUseMenu at
  every build); the ending's picks come back as menuLeaveComment / menuExploreHere; record headers
  go through Menu.AppendLine. t39 (now in its own work folder) 83 pass; real inbox md5 unchanged.
- **23:40** `LIB_MENU` / `menu-minimize`: **LIB_MENU steps 1 and 2: lib_menu (ending, safe labels, record lines, Explorer) and menus from files**
  Default set in Menus/Default, the user's files in Data/Scripts/Menus win file by file;
  Head/Sub/Item lines, folders:/kinds: filled at open time, one handler a menu, Menu.Loaded,
  Menu.Reset. Example Library.txt. Tested by OXT-BEYOND/tests/t43_lib_menu.txt (57 pass).
- **23:38** `LIB_BIT` / `cellmap-v3-followups`: **cellmap v3: slopes drawn in LevelSegments, CellMap.PackSegments (A-92 1)**
  Sloped ground edges run corner to corner (floor when the neighbour's edge matches),
  uprights from corner heights, a twisted cell's diagonal; a pack's place drawn as one.
  Python and xTalk give the same lines; py_v3 38 ok, lc_v3 28 PASS on both engines, v2 unchanged.
- **23:18** `LIB_DEV` / `window-zoom`: **LIB_GUI look fixes done**
- **23:17** `LIB_GUI` / `gui-step1`: **LIB_GUI look fixes: dark closed menus and choice, list selection light, field hint shows**
  Menus and choices: light text on the panel colour when closed, dark text while
  their list is open (LIB_THEME menu rule). Menu strip dark. List selected line
  white on the hilite colour. hint= shows dimmed while the field is empty;
  Gui.Get gives empty under it. t41: 104 checks pass.
- **22:58** `LIB_DEV` / `window-zoom`: **LIB_GUI: owner saw Notes ('LOVELY'); look fixes sized**
- **22:57** `LIB_DEV` / `window-zoom`: **NEXT: where tonight ended**
- **22:56** `LIB_MENU` / `main`: **PLAN: the 2013 Default/Menus set (default list, registry + reset, folder-filled Wizard menu, one browser)**
- **22:55** `LIB_MENU` / `main`: **PLAN: the owner's 2009 iGame3D menus and Data path system as the model for step 2**
- **22:52** `LIB_DEV` / `window-zoom`: **LIB_MENU gets its own LIB: board part, two next steps sized**
- **22:51** `LIB_MENU` / `main`: **LIB_MENU: README and PLAN (owner: its own LIB, 17 Nov)**
- **22:34** `LIB_DEV` / `window-zoom`: **Tube reloaded after tonight's helpers**
- **22:33** `LIB_DEV` / `window-zoom`: **Project Map: hand-made window titles moved to Users.Title (done)**
- **22:33** `LIB_USERS` / `users-title`: **TITLES_TO_MOVE, NEXT: the ten hand-made titles moved to Users.TitleStack**
- **22:33** `LIB_BIT` / `users-title`: **Window titles: ask Users.Title (LIB_USERS) when in use, else "FOR OWNER | ..."**
  The hand-made title stays as the plain fallback (no real name), then
  dispatch "Users.TitleStack" lets LIB_USERS word it when the library is in
  use; dispatch does nothing when nothing handles it, so the script still
  works alone. List: LIB_USERS/TITLES_TO_MOVE.md.
- **22:33** `LIB_BUILD` / `users-title`: **Window titles: ask Users.Title (LIB_USERS) when in use, else "FOR OWNER | ..."**
  The hand-made title stays as the plain fallback (no real name), then
  dispatch "Users.TitleStack" lets LIB_USERS word it when the library is in
  use; dispatch does nothing when nothing handles it, so the script still
  works alone. List: LIB_USERS/TITLES_TO_MOVE.md.
- **22:33** `LIB_DEV` / `window-zoom`: **Window titles: ask Users.Title (LIB_USERS) when in use, else "FOR OWNER | ..."**
  The hand-made title stays as the plain fallback (no real name), then
  dispatch "Users.TitleStack" lets LIB_USERS word it when the library is in
  use; dispatch does nothing when nothing handles it, so the script still
  works alone. List: LIB_USERS/TITLES_TO_MOVE.md.
- **22:33** `LIB_RTS` / `users-title`: **Window titles: ask Users.Title (LIB_USERS) when in use, else "FOR OWNER | ..."**
  The hand-made title stays as the plain fallback (no real name), then
  dispatch "Users.TitleStack" lets LIB_USERS word it when the library is in
  use; dispatch does nothing when nothing handles it, so the script still
  works alone. List: LIB_USERS/TITLES_TO_MOVE.md.
- **22:33** `LIB_SCRIPTBLOCKS` / `users-title`: **Window titles: ask Users.Title (LIB_USERS) when in use, else "FOR OWNER | ..."**
  The hand-made title stays as the plain fallback (no real name), then
  dispatch "Users.TitleStack" lets LIB_USERS word it when the library is in
  use; dispatch does nothing when nothing handles it, so the script still
  works alone. List: LIB_USERS/TITLES_TO_MOVE.md.
- **22:33** `LIB_TTRPG` / `users-title`: **Window titles: ask Users.Title (LIB_USERS) when in use, else "FOR OWNER | ..."**
  The hand-made title stays as the plain fallback (no real name), then
  dispatch "Users.TitleStack" lets LIB_USERS word it when the library is in
  use; dispatch does nothing when nothing handles it, so the script still
  works alone. List: LIB_USERS/TITLES_TO_MOVE.md.
- **22:29** `LIB_DEV` / `window-zoom`: **Boards: menus, decisions loaded into the stacks**
- **22:28** `LIB_DEV` / `window-zoom`: **Board menus end with Leave comment / Explore here; On Git or Not step 4 decisions**
  Every menu on both boards (a part card's click menu, a chip's files, a red blocker,
  a yellow note) ends with the same two lines from one handler (pmMenuEnd, via
  pmPopupMenu). Explore here opens the part's folder (new P-row column) or a chip's
  single file; nothing on disk is touched until a pick.
  Loose files (F rows flagged decide by git_map.py) offer Commit / Ignore / Delete /
  Leave, appended to LIB_LLMIN/LIB_DEV/GIT_DECISIONS.txt for Claude; chips and menu
  lines show what is decided. for_review.py feedback prints the file; CLAUDE.md says
  how Claude carries them out. LIB_MENU_PLAN.md: the menu rules (a plan).
- **22:27** `LIB_DEV` / `window-zoom`: **LIB_GUI stages 1-2 done; stage 3 sized**
- **22:26** `LIB_GUI` / `gui-step1`: **LIB_GUI stages 1-2: .gui reader/writer and the native face**
  Gui.Load/Parse/Problems/Text/Save; Gui.Build for window label button toggle
  choice list field text menu line, coloured by LIB_THEME; Gui.Get/Set/Show/Enable;
  guiDo and do= messages. Examples gui/status_browser.gui, gui/notes.gui.
  Headless test OXT-BEYOND/tests/t41_lib_gui.txt: 84/84 pass.
- **22:23** `LIB_DEV` / `window-zoom`: **Users.Title done; next step sized**
- **22:22** `LIB_USERS` / `users-title`: **LIB_USERS: Users.Title and Users.TitleStack words window titles (FOR OWNER | ... / Opus | ...); list of hand-made titles to move; NEXT.md**
  Test: OXT-BEYOND/tests/t42_users_title.txt, 21 pass headless.
- **22:07** `LIB_DEV` / `window-zoom`: **Priority Tube: an unsized bubble no longer stops the script when selected**
- **22:04** `LIB_DEV` / `window-zoom`: **Size the gateway comment**
- **22:04** `LIB_DEV` / `window-zoom`: **Priority Tube: Delete takes a bubble off the tube for good (TUBE_REMOVED.txt), U brings it back**
- **21:23** `LIB_SYSTEM` / `main`: **TODO: engine contract answered; A-96..A-99 from the owner's answers**
- **21:23** `LIB_ig3d` / `rename-day`: **Engine contract: the owner's five answers (17 Nov)**
- **21:17** `LIB_GAMES` / `vector-toss-dangle`: **Merge branch 'main' into vector-toss-dangle**
- **21:17** `LIB_GAMES` / `rename-day-games`: **ComfyPong seed 2102167373 goes in (owner, 17 Nov)**
- **21:10** `LIB_GAMES` / `vector-toss-dangle`: **Merge branch 'main' into vector-toss-dangle**
- **21:10** `LIB_GAMES` / `rename-day-games`: **ComfyPong level 1 goes in (owner, 17 Nov); levels 2 and 3 stay out**
- **21:08** `LIB_DEV` / `window-zoom`: **Point the feedback log at its real place (LIB_LLMOUT/LIB_DEV)**
- **20:59** `LIB_DEV` / `window-zoom`: **Comment window title says what was clicked; size two new tube comments**
- **20:52** `LIB_DEV` / `window-zoom`: **Priority Tube: NEXT.md, the one-note-at-a-time loop for the next session**
- **20:50** `LIB_DEV` / `window-zoom`: **Priority Tube: owner's first look, "there's something there"; we feel it out (echoes the old post-Antack T3D game menu)**
- **20:45** `LIB_DEV` / `window-zoom`: **Priority Tube: bubbles in a test tube, Claude's compute-time order first, the owner's drag/arrow order wins**
  tube_items.py gathers board comments + Project Map next steps with Claude's sizes; the stack
  saves the order to LIB_LLMIN/LIB_DEV/PRIORITY_ORDER.txt at every move. Headless: t40 (17 checks).
- **20:31** `LIB_DEV` / `window-zoom`: **Boards: right-click anything to comment (big box, yellow note nodes); order of comments is not priority**
  Shared board_canvas: comment box on any box, chip, column, string, panel line or the black;
  notes tied by a string, move with their part, drag/edit/delete; BOARD_COMMENTS.txt read by
  for_review.py feedback. Popup button reused across rebuilds; help-bar writes guarded.
  Headless: OXT-BEYOND t39, 48 checks.
- **20:23** `LIB_DEV` / `window-zoom`: **On Git or Not board: git_map.py survey + stack on the Project Map's canvas, now one shared script**
  The canvas (livecode/board_canvas.livecodescript) reads board settings from B rows and its
  panel order from L rows; the Project Map keeps its defaults. Headless: OXT-BEYOND t39 (16 checks).
- **20:17** `LIB_DEV` / `main`: **OnGitOrNot plan: scope = this machine now, the NOT ON GIT side made visible (remotes later)**
- **20:15** `LIB_DEV` / `main`: **OnGitOrNot: one-page plan (a Project Map of what is on git and what is not)**
- **19:53** `LIB_DEV` / `main`: **Project Map stack saved with the merged board**
- **19:53** `LIB_DEV` / `main`: **Project Map board: LIB_DEV card shows the map done and merged**
- **19:53** `LIB_SYSTEM` / `main`: **STATUS: the Project Map (17 Nov)**
- **19:53** `LIB_DEV` / `main`: **Merge project-map: the Project Map (owner's word, 17 Nov)**
- **19:50** `LIB_DEV` / `main`: **Project Map: red blockers take feedback and file paths for Claude (MAP_NOTES.txt)**
  Click a red chip: Feedback on this blocker... / Select file(s) for Claude... (paths only).
  Lines go to LIB_LLMIN/LIB_DEV/MAP_NOTES.txt; for_review.py feedback prints them; CLAUDE.md says what to do.
- **19:36** `LIB_DEV` / `main`: **Project Map: review from the map (Open / Reviewed / Feedback... per file, T tells Claude)**
  Writes the Status Browser's own REVIEW_STATE / REVIEW_FEEDBACK / TELL_CLAUDE files in their
  formats; Reviewed rebuilds the map keeping the view. Loose files only open.
- **19:34** `LIB_DEV` / `main`: **for_review relink: moved review files get their new path; the Project Map runs it every rebuild**
  Lines in FOR_REVIEW.txt whose file moved point to where it is now (LIB updated, caveat says
  from where); a file already listed again at its new place loses its old line. REVIEW_STATE /
  REVIEW_FEEDBACK are never moved or changed: the old path's lines are appended under the new one.
  Mirror copies inside build folders are not taken for the new home. First run: 14 relinked, 1 dropped.
- **19:30** `LIB_DEV` / `main`: **Project Map: moved review files open where they are now ([moved]); gone ones open the nearest folder**
  Explorer /select on a missing file falls back to This PC (owner's report). make_map.py finds
  moved files by name at rebuild (common names must share a folder with the old path).
- **19:25** `LIB_DEV` / `main`: **Project Map: pink chips list their files in a popup; a pick opens Explorer on the file**
  make_map.py writes each review / loose file (group, label, Windows path, folder flag) as F rows;
  the stack keeps them per chip in cFiles (no disk search on click) and opens Explorer with
  start (returns at once). Also fixes the total: single-file chips were left out (125 -> 136).
- **18:45** `LIB_DEV` / `main`: **Project Map: the whole project as a zoomable board of cards and strings (OXT-Beyond)**
  board.txt (hand-kept) + tools/make_map.py (counted facts) -> map_data.txt; ProjectMap.oxtstack
  draws it: core purple/yellow, green features, lavender demos, gold done lists, pink reviews, red
  blockers with red strings to YOU; focus, blockers-only, fly-to panel, fit, rebuild.
- **14:02** `LIB_SYSTEM` / `main`: **TODO: cellmap v3, engine contract and LIB_USERS plan kept (owner 17 Nov); follow-ups A-92..A-94; Spark with OXT-Beyond last (A-95)**
- **14:02** `LIB_USERS` / `main`: **LIB_USERS plan (Fable, 16 Nov), kept by the owner 17 Nov with his answers**
  Titles say FOR OWNER, never a real name; the bar is fine; Claude models may
  save stacks; V: (VIBE) is the install-test drive, not a user.
- **13:42** `LIB_DEV` / `main`: **Add bash/audit.sh: list every file under a folder by extension, skipping LIB_LLMOUT**
  Moved from LIB_LLMIN/LIB_BAT. Skipping the done pile drops ~/projects from
  5,992 to 533 .livecodescript files.
- **11:57** `LIB_SYSTEM` / `main`: **STATUS: LIB_COMFY node editor working**
- **11:57** `LIB_COMFY` / `comfy-vector-pong`: **NOTES.md: everything learned getting the first node-built game working, and how to make more workflows**
- **11:46** `LIB_COMFY` / `comfy-vector-pong`: **install.sh: every Comfy Desktop install, or the one named**
- **11:11** `LIB_COMFY` / `comfy-vector-pong`: **Vibecode3D node pack: Game Start, Palette, Court, Paddle, Ball, Match Rules, Build Game; cpong parts; starter workflow**
  Build Game picks up the script parts the chain needs and writes a playable
  Vibecode3D_Play_<Name>.livecodescript. Seeds 2 and 3 compiled and played on the engine.
- **11:11** `LIB_COMFY` / `comfy-vector-pong`: **LIB_COMFY: ComfyUI as a node editor for Vibecode3D games (readme)**
- **10:01** `LIB_GAMES` / `vector-toss-dangle`: **Vector Toss: the owner's Stamina note for HANG TIME (not built yet)**
- **09:43** `LIB_BVH` / `main`: **Harold Lloyd, Safety Last! (1923): captured by the owner, with credit**
- **09:43** `LIB_GAMES` / `vector-toss-dangle`: **Vector Toss: dangling in a hole is Harold Lloyd's hang from Safety Last! (1923), frames 134-198, played forward then back; credit in the header**
- **09:43** `LIB_MOCAP` / `main`: **Clip Harold_Lloyd_Safety_Last_1923 (hang for Vector Toss)**
- **09:38** `LIB_SYSTEM` / `main`: **LIB_ALPHA: no Fable time left (17 Nov); Opus plans architecture on one page first**
- **09:38** `LIB_GAD` / `main`: **Galactica sample save removed (owner, 17 Nov): star names now in LIB_LISTS; fetch a fresh save from Ed Zavada's repo when GAD writes Galactica 4 files**
- **09:38** `LIB_LISTS` / `main`: **LIB_LISTS: the MasterLists stack's lists, one file each, catalogued by name; Galactica star names (owner)**
- **09:10** `LIB_RTS` / `main`: **LIB_RTS: the 2008 iGame3D RTS (RNDRTS + RTS_Functions) as an xTalk library and demo stack**
  Library: map maker, click/box selection, orders, senses, behaviours, tasks,
  health and rising dead, distance-map paths. Demo: top-down view, drag to
  select, click to command, notes to the AI. Headless tests pass on OXT-Beyond
  (library also on 9.6.3).
### Monday, November 16

- **19:58** `LIB_RAYGUI` / `main`: **PLAN: step 0 wording; note on the theme file's comments and new keys**
- **19:57** `LIB_GUI` / `main`: **PLAN: glyph= option noted (1-bit symbols that draw the same in every face)**
- **19:57** `LIB_RAYGUI` / `main`: **LIB_RAYGUI: own repository; README and PLAN.md (A-41): raygui in the xt3d bridge, fed mouse, value-in value-out calls, the Rapidograph look**
- **19:57** `LIB_TOOLBAR` / `main`: **PLAN: say exactly which launcher targets are not settled**
- **19:55** `LIB_GUI` / `main`: **PLAN: boundary rule 4 says an app's tools may float in a LIB_TOOLBAR strip (same words in all four plans)**
- **19:55** `LIB_TOOLBAR` / `main`: **LIB_TOOLBAR: own repository; README and PLAN.md (A-40): the 2007 strip as data, the .toolbar content file, actions, the projects launcher**
- **19:55** `LIB_USERS` / `library-plans`: **PLAN: boundary rule 4 says an app's tools may float in a LIB_TOOLBAR strip (same words in all four plans)**
- **19:54** `LIB_GUI` / `main`: **LIB_GUI: own repository; README and PLAN.md (A-42): the .gui layout file, faces, Gui.* calls, the GUI Builder**
- **19:52** `LIB_USERS` / `library-plans`: **LIB_USERS: PLAN.md (A-43): roster, current user, one title wording, log stamps, permission words**
- **19:41** `LIB_ig3d` / `release-checklist`: **LIB_ig3d README rewritten as the map of the knowledge base: what each file is for and how fresh, what moved to LIB_EDITOR / LIB_DATA / LIB_PUBLIC / LIB_GAD since 12 Nov, duplicates and stale copies listed (nothing deleted); ENGINE_CONTRACT.md named as arriving with engine-contract**
- **19:40** `LIB_EDITOR` / `release-checklist`: **RELEASE_CHECKLIST: nothing stated that was not checked (the founding year, Windows versions and WindowLab's code are the owner's to state); file and link counts corrected**
- **19:40** `LIB_EDITOR` / `release-checklist`: **iGame3D XT: RELEASE_CHECKLIST.md, every step from today to an itch.io build (who, how to check, what blocks), the owner's blockers on top, what done means for 1.0, the ship list with source and licence, drafts of the credits and the page**
- **19:30** `LIB_GAMES` / `engine-contract`: **engine_stubs: exactly the engine contract (LIB_ig3d/ENGINE_CONTRACT.md)**
  One stand-in for every contract call the XT engine has; two debts kept alive; test hooks.
- **19:30** `LIB_ig3d` / `engine-contract`: **Engine contract: ENGINE_CONTRACT.md, tools/contract_check.py and its test**
  Every call a game may make, for the four editions (iGame3D XT, xRay, Box2DXT, xRayBox),
  and the debts: what games use outside it.
- **16:08** `LIB_BIT` / `cellmap-v3`: **cellmap v3: slopes, stacked maps, map packs (design, readers, walker, example, tests)**
  CELLMAP_V3.md decides: a [slope] section (four corner rises a cell), stacked maps joined
  by geometry (stairs, holes) in one place of a .cellpack, doors for what cannot be walked.
  lib_cellmap.livecodescript and cellmap.py read and write version 3 and packs, walk slopes
  and stacked maps with the same answers (tests/py_v3_test.py, tests/lc_v3_test.txt).
  Every version 1 and 2 map reads and writes back unchanged. Two walking fixes for all maps:
  a drop goes through air only; an actor can walk away after dropping off a ledge.
  Example: maps/two_rooms (cellar, loft, pack). Drawing of slopes and packs is not built.
- **15:43** `LIB_PUBLIC` / `main`: **vibeinstall after the merges (16 Nov): every source is main; the 17 betas listed by name (BETAS) so they stay betas; titles living in another repository (HOMES) are always in the catalog; catalog: 52 titles (Antack Fresh joins)**
- **15:41** `LIB_BUILD` / `main`: **The owner's build stack (14 Nov); the build folders themselves are ignored**
- **15:41** `LIB_MCP` / `main`: **The owner's headless_lmStudio.bat**
- **15:41** `LIB_SPARK` / `main`: **Spark's first LIB_HOWTO outlines (14 Nov), kept beside the newer howto/out**
- **15:41** `xt3D_Raylib_Livecode_Bridge` / `rename-day`: **The owner's bench stacks and start_claude_LITE.bat, the rebuilt extension; build output ignored**
- **15:41** `LIB_SPARK` / `main`: **Merge spark-designs-v2 (owner: merge everything, 16 Nov)**
- **15:41** `LIB_SPARK` / `main`: **Spark's output: the latest arcade ideas (16 Nov 10:38) and the LIB_HOWTO outlines in howto/out**
- **15:41** `LIB_SYSTEM` / `main`: **The night of 15-16 Nov: the owner's prompt and the work report**
- **15:41** `LIB_TEST` / `main`: **Merge ttrpg-studio-1 (owner: merge everything, 16 Nov)**
- **15:41** `LIB_TTRPG` / `main`: **Merge ttrpg-studio-1 (owner: merge everything, 16 Nov)**
- **15:41** `LIB_TTRPG` / `main`: **The owner's TTRPG_Player_Client stack**
- **15:41** `xt3D_Raylib_Livecode_Bridge` / `rename-day`: **Merge vector-toss-font (owner: merge everything, 16 Nov)**
- **15:41** `xt3D_Raylib_Livecode_Bridge` / `rename-day`: **Merge editor-hooks (owner: merge everything, 16 Nov)**
- **15:40** `LIB_BIT` / `cellmap-v3`: **The owner's changes: BitEditor.livecode (15 Nov), his review and build stacks, his maps**
- **15:40** `LIB_BIT` / `cellmap-v3`: **Merge biteditor-feedback (owner: merge everything, 16 Nov)**
- **15:40** `LIB_THEME` / `main`: **The owner's dark theme (15 Nov)**
- **15:40** `LIB_THEME` / `main`: **Merge theme-studio, which holds tabstrip (owner: merge everything, 16 Nov)**
- **15:40** `Vibecode3D` / `main`: **Merge clear-names (owner: merge everything, 16 Nov)**
- **15:40** `Vibecode3D` / `main`: **The owner's clean-up: old stack and script into Archive/ (with the bug report and WHAT_CAN_WE_CLEAN), the new GUI stack VIBECODE3D_GUI_v1**
- **15:40** `LIB_DATA` / `main`: **Merge data-forwarding (owner: merge everything, 16 Nov)**
- **15:40** `LIB_DATA` / `main`: **The owner's Images folder note**
- **15:40** `LIB_MOCAP` / `main`: **Merge anim-list (owner: merge everything, 16 Nov)**
- **15:40** `LIB_PUBLIC` / `main`: **Merge vibe-install (owner: merge everything, 16 Nov)**
- **15:40** `LIB_USERS` / `main`: **Merge vibe-install (owner: merge everything, 16 Nov)**
- **15:40** `LIB_USERS` / `main`: **The owner's changes: .gitignore keeps BILL/ private; Vibe/About_vibe.txt**
- **15:40** `LIB_ig3d` / `release-checklist`: **Merge v3d-editor-tools (owner: merge everything, 16 Nov); ig3d-editor-works and ig3d-editor-standalone held the same files**
- **15:39** `LIB_GAMES` / `vector-toss-dangle`: **Merge deaddays (owner: merge everything, 16 Nov)**
- **15:39** `LIB_GAMES` / `vector-toss-dangle`: **Merge spark-roadtrip (owner: merge everything, 16 Nov)**
- **15:39** `LIB_GAMES` / `vector-toss-dangle`: **Merge vector-toss (owner: merge everything, 16 Nov)**
- **15:39** `LIB_GAMES` / `vector-toss-dangle`: **Merge couple-cellmap (owner: merge everything, 16 Nov)**
- **15:39** `LIB_GAMES` / `vector-toss-dangle`: **Merge install-findfile (owner: merge everything, 16 Nov)**
- **15:39** `LIB_GAMES` / `vector-toss-dangle`: **Merge fresh-math (owner: merge everything, 16 Nov)**
- **15:39** `LIB_GAMES` / `vector-toss-dangle`: **Merge game-tell (owner: merge everything, 16 Nov)**
- **15:39** `LIB_GAMES` / `vector-toss-dangle`: **The owner's Simple_Test1 skins (ACTIVE, alt1, alt1b)**
- **15:38** `LIB_EDITOR` / `main`: **Merge ig3d-editor-standalone: iGame3D XT (owner: merge everything, 16 Nov). The earlier edition is tag edition/known-works**
- **15:38** `LIB_DEV` / `main`: **Merge window-shape (owner: merge everything, 16 Nov)**
- **15:38** `LIB_DEV` / `main`: **Merge player-at-rest (owner: merge everything, 16 Nov)**
- **15:38** `LIB_DEV` / `main`: **The owner's quality-of-life changes to the browser stacks (scaleFactor and more): GAME_Browser, Status_Browser, Status_Browser_Launcher**
- **15:30** `LIB_DEV` / `main`: **WindowShape: Shape.FromControl moves a control of the stack to its top left first, so drawing and outline line up (else only overlaps show: dashes)**
- **15:30** `LIB_EDITOR` / `main`: **iGame3D XT drag preview: outline from a 6-wide line, the wire drawn 3 wide inside it, lined up (owner's screenshot: dashes)**
- **15:23** `LIB_EDITOR` / `main`: **iGame3D XT: the drag preview's window is the model's own wire (Tools/window_shape, a copy of LIB_DEV's WindowShape)**
- **15:23** `LIB_DEV` / `main`: **WindowShape library (after Scott Rossi's WindowLab): any image as a window's outline (Shape.FromImage/FromFile/FromControl/Make rect,round,oval), paint mode (Shape.PaintStart/Brush/Eraser/PaintClear/PaintEnd), Shape.DragWindow for a window with no title bar; Shape Lab, WindowLab remade on it; test t38**
- **15:03** `LIB_DEV` / `main`: **game_player: gV3DTickMS, a game's own frame time (the editor's View > Frame Rate)**
- **15:03** `LIB_EDITOR` / `main`: **iGame3D XT layout (owner 16 Nov): the menu bar on top in Macintosh order (File Edit View Library Mesh Dev Window Help), unfinished items dimmed, View ticks; the tools along one side (View > Toolbar At Top/Bottom/Left/Right) after a ]< that snaps them to a draggable ]>; the Library is a preview over a short list: a click chooses and shows, a double-click or Return/Enter places it where the mouse was in the view, dragging the preview drops it; View > Frame Rate 15/30/60; layout kept in Vibecode3D/igame3d_xt_layout.txt**
- **14:39** `LIB_PUBLIC` / `main`: **launcher: the stack saved visible again (the last save kept it hidden: no window), rebuilt**
- **14:34** `LIB_PUBLIC` / `main`: **launcher: the stack saved with the new script and rebuilt as Vibecode3D Library.exe (OXT-Beyond)**
- **14:30** `LIB_PUBLIC` / `main`: **launcher: Play starts the game copy with Windows' start (returns at once, so the library can answer the copy's relaunch; 'launch with' left the first Play's copy hanging with no window, owner 16 Nov); a game copy closes its library stack (destroyStack true) once the game window is open, and quits if none opened in 3 s; every start is logged with its arguments (launcher.txt)**
- **13:54** `LIB_PUBLIC` / `main`: **vibeinstall: rename the old exe only when it was copied**
- **13:54** `LIB_PUBLIC` / `main`: **vibeinstall: never copy the old Vibecode3D.exe (the Library program takes its place), so a reinstall works while a game is open**
- **13:54** `LIB_DEV` / `main`: **game_player: paused while in the background (keys typed elsewhere never reach the game), going on when back in front; fps shown at rest too; the status line above the game's own panels**
- **13:54** `LIB_EDITOR` / `main`: **iGame3D XT: the Library list keeps only Return (no arrows or letters: the camera's); a close X just above its top right corner**
- **13:22** `LIB_DEV` / `main`: **game_player: bStill, a game at rest (the editor) is not stepped or drawn until a key, the mouse or the game wakes it; status says at rest**
- **13:22** `LIB_EDITOR` / `main`: **iGame3D XT Library list (owner 16 Nov): folders (categories) with .. ; a click loads, a double-click or Return opens a folder or goes back up; the street and the showcase first; the list sized to the window (900x600 from the launcher); at rest (no keys, no orbit, no message) it sets bStill so the player stops drawing**
- **13:21** `LIB_SYSTEM` / `main`: **LIB_OMEGA 32: pgrep -f waiters match themselves**
- **13:09** `LIB_PUBLIC` / `main`: **vibeinstall: skip program files that are already the same, and say so (not crash) when Windows locks a running one**
- **13:07** `LIB_PUBLIC` / `main`: **vibeinstall: Vibecode3D.exe is the Library program, so Start Menu, Desktop and Play <Game>.cmd no longer open the old app; says so when the old exe is running**
- **11:15** `LIB_SPARK` / `main`: **Entities round 3: 1/12 pass raw, 2/12 after snap; ROUND3.md (sizes, loose parts, front, retries resend the same numbers); musing lines like 'So burner: box | ...' no longer read as parts**
- **10:54** `LIB_PUBLIC` / `main`: **install: --include-held puts the titles held back from shipping on this PC too (the owner tries iGame3D XT from Vibecode3D Library > Tools); verify knows iGame3D XT carries its own Data and Tools. V: reinstalled with it: 51 titles; t27 expects 51 titles, 5 tools**
- **10:54** `LIB_SPARK` / `main`: **entity.py snap: the tool makes the stated ON TOP OF / BELOW relations true by moving parts' heights (Spark's retries resend the same numbers); writes *_snapped.txt with a note per move; test added (18/18)**
- **10:53** `LIB_EDITOR` / `main`: **Replace With Model reworked (owner 16 Nov): card 1 Models, the models made from their names (buildings, houses, the 17 prop groups, characters) with a preview; card 2 Folder ('Use Folder'): any folder of .wtf / .obj models, its subfolders listed to explore. The game, its meshes, the preview and the skin are shared by both cards. Saving writes each model as a .wtf beside the skin (Skins/<Game>/models), so the Game Player and the engine play skins as before; the skin keeps where each came from (gen:Vehicles/car). Ig.Projects finds the projects above the editor (no WSL). Tests t19 (rewritten, 19 checks), t18 (its own model), t20**
- **10:44** `LIB_SYSTEM` / `main`: **STATUS: LIB_SPARK FUN round + entity checker**
- **10:43** `LIB_SPARK` / `main`: **Entities round 2 moved to out/round2 before round 3 (checker reads Spark's wordings)**
- **10:43** `LIB_SYSTEM` / `main`: **LIB_OMEGA 31: Spark echoes fun, does not invent it**
- **10:43** `LIB_SPARK` / `main`: **FUN round: 12 drafts with the FUN block (12/12 filled, tables in range, fun only where the brief had it, 4 stories flipped); REVIEW_FUN_ROUND.md merges the owner's answers into build-ready designs (Ghost Light Mine, One Cent Raise, Dont Break The Walls, Hollow Mountain with its glitch, Courier Run extras, UFO x3 incl. Fellout AP rules) and answers the Stair Hopper question**
- **10:39** `LIB_SPARK` / `main`: **Entity checker reads Spark's own wordings (sits on, the hull, on the ground, in front of, behind, beside, plurals = every part of that kind; front is +z): round 2's 'cannot read' faults are gone and what remains is real geometry. Round 2 drafts kept. Arcade CONCEPT prompt gets a FUN section (toy, choice, surprise, moment, extra) after the owner's note that the designs read as mechanics, not fun; runner --out for side-by-side output; FUN-round ideas from his review answers + UFO idea**
- **09:39** `LIB_EDITOR` / `main`: **iGame3D XT: the plan says where it stands (every workstream done, tests, sizes, speeds; what is left for the owner)**
- **09:39** `LIB_PUBLIC` / `main`: **install: iGame3D XT's model tools in Vibecode3D Common/Tools (DeadDays builds its city with them); DeadDays as a beta (LIB_GAMES deaddays); the editor's home is LIB_EDITOR ig3d-editor-standalone with Tools, Data, Help_2008 (still held back); verify knows Common/Tools; catalog rebuilt (51 titles). V: reinstalled: 50 titles; the removed iGame3D clips no longer installed. t27: 50 titles, 17 betas**
- **09:37** `LIB_GAMES` / `vector-toss-dangle`: **DeadDays: the owner's 2008 iGame3D story (best story) remade as a third-person shooter on Vibecode3D, every building, prop and person made by iGame3D XT's tools (LIB_EDITOR iGame3D_XT/Tools, found beside an install or above). The city of the dead, a robot that hunts them, a shotgun and a rifle to find; the police station door, its stairs, the upstairs office; somewhere else: a park, the temple, its altar: TO BE CONTINUED. Test t36 (20 checks; real engine: the city made in 104 ms)**
- **09:32** `LIB_EDITOR` / `main`: **iGame3D XT: A (123 props in 17 groups, generic names, Tools/v3d_props), C (our stick figure by role, Tools/v3d_figures; 2008 characters -> roles, civilian_001...; Data/Models/stick_figure.gltf by tools/stick_gltf.py), D (levels as xTalk files: Data/Levels/<name>/load_script.xtalk, Lvl.* commands for the 2008 Lua hooks, Data/Scripts/LEVEL_API.txt; Library > Levels, File > Save; only Lvl. lines run; four levels shipped), F part (Library > Set Data Folder..., this edition's own Data folder, axes on the floor, Help > the 2008 pages kept as legacy docs in Help_2008). Showcase of every model. Tests t35 (24), t34, t33**
- **09:18** `LIB_EDITOR` / `main`: **iGame3D XT, workstream A: buildings from their names (Tools/v3d_buildings: kind and roof from the name, sizes from its hash; the owner's window heights by kind; uDead's breakable doors and windows with hit points). Editor: Library > Models without the 2008 data lists the 51 names and a street of each kind; Edit > boom breaks doors and windows first, then flattens; File > Clear and Undo take a building's parts with it. Test t34 (24 checks; real engine: 20 buildings made and placed in 110 ms)**
- **09:10** `LIB_GAMES` / `vector-toss-dangle`: **udg_to_udead.py: its 2009 source was removed (owner 16 Nov); udead_levels.txt is the master now**
- **09:10** `LIB_SYSTEM` / `main`: **remove_ig3d_assets.sh: the list says when there is nothing left (owner removed iGame3d_To_Recreate, 16 Nov)**
- **09:08** `LIB_SYSTEM` / `main`: **Night shutdown checklist (tools/night_shutdown.sh, NIGHT_SHUTDOWN.md); remove_ig3d_assets.sh (owner 16 Nov: the iGame3D assets out of the projects; run: LIB_MOCAP c5358c6, LIB_BVH 5f3463b, the untracked 2008 copies deleted; iGame3d_To_Recreate waits for --all); TODO A-89 (iGame3D XT in LIB_EDITOR), A-91 (GAD in LIB_GAD)**
- **09:08** `LIB_BVH` / `main`: **Remove the iGame3D BVH sources no game uses (owner 16 Nov: remove the iGame3D assets; kept: reachhigh throwtoss1 underHandThrow)**
- **09:08** `LIB_MOCAP` / `main`: **Remove the iGame3D clips no game uses (owner 16 Nov: remove the iGame3D assets; kept: reachhigh throwtoss1 underHandThrow)**
- **09:07** `LIB_PUBLIC` / `main`: **install: Genetic Anomaly installs from its new home, LIB_GAD main (HOMES; owner 16 Nov). V: reinstalled, 49 titles; t30 no longer expects the held-back editor**
- **09:06** `LIB_GAMES` / `vector-toss-dangle`: **Game.FindFile (install/LAYOUT.md 5.1) in Antack, uDead, Thrmnlra, Face, Amazing_Couple, GeneticAnomaly (GA.GenRoot) and Ig3dEditor (Ig.DataRoot), each keeping its own handler name: the script's own folder first (from the uScriptFile the launcher and GL.Open set; LIB_GAMES/Vibecode3D_Games/X/... is <script folder>/X/...), then Vibecode3D Common beside it, then the walk up, and the wsl$ fallback last. Global bNoWSL (test hook) turns the fallback off. Test OXT-BEYOND/tests/t30_install_findfile.txt**
- **09:06** `LIB_GAMES` / `vector-toss-dangle`: **GeneticAnomaly and the iGame3D editor leave LIB_GAMES (owner 16 Nov: the editor is a tool, not a game; GAD is a long-term project): GeneticAnomaly -> LIB_GAD/GeneticAnomaly (2e194a6), the editor -> LIB_EDITOR/iGame3D_XT (619040e, standalone edition on ig3d-editor-standalone), the 2008 manifest -> LIB_EDITOR/iGame3D_XT/_manifest_2008. Branches ga-turns, editor-tools, ig3d-editor-works (with the 2008 Data folder, 5a62a5d) and ig3d-editor-standalone stay as their history**
- **09:06** `LIB_EDITOR` / `main`: **iGame3D XT standalone edition, moved from LIB_GAMES (ig3d-editor-standalone c2543eb): Aquarius from one bitmap (Data/Text/Aquarius.pbm), the plan, decisions, inventory and tools; the editor opens its own Tools/ copies first (Ig.ToolFile) and finds Data/ beside its script. Tests t33 (here), t20**
- **09:05** `LIB_EDITOR` / `ig3d-editor-works`: **iGame3D XT moves home (owner 16 Nov: a tool, not a game): the editor as it works today (LIB_GAMES editor-tools), its tool windows (LIB_ig3d v3d-editor-tools), the 2008 manifest (from LIB_GAMES); README with the editions and names**
- **09:05** `LIB_GAD` / `main`: **GeneticAnomaly moves home: the prototype from LIB_GAMES (ga-turns, with the Game.FindFile order in GA.GenRoot) and the owner's 2018 Galactica 3-based GUI (XTJSON harvest GenericaAnyData_04042018a) as the base for GAD's own UI; notes on the owner's direction (16 Nov)**
- **07:27** `LIB_GAMES` / `refs/tags/archive/ig3d-editor-standalone`: **iGame3D XT, workstream B: the 256 Aquarius models from ONE bitmap. Data/Text/Aquarius.pbm (128x128 P1, from the owner's 2008 AquariusCharactersPMB.lua bitmaps; tools/aquarius_bitmap.py), built into the editor as kAquaHex too; Library > Text lists the characters, its first line lays all 256 on the floor, timed (Ig.AquariusLevel, Ig.AquaMesh: pixel outlines, raised). Library list display split out as Ig.ShowLibrary. Test t33 (21 checks; real engine: made 304 ms, placed 32 ms, first frame 395 ms); t20 still passes**
- **07:12** `LIB_GAMES` / `refs/tags/archive/ig3d-editor-standalone`: **Ig3dEditor standalone: the shipping names (owner 16 Nov): iGame3D XT; xRay on the xt3d core; Box2DXT and xRayBox with Box2D; on itch.io as xAction**
- **07:12** `LIB_PUBLIC` / `main`: **install: the editor's shipping title is iGame3D XT (owner 16 Nov; still held back)**
- **07:01** `LIB_PUBLIC` / `main`: **LAYOUT 6: the owner's decisions of 16 Nov (motion clips: only what the games use, Animazoo and CMU credited; the editor ships as its standalone edition)**
- **07:01** `LIB_GAMES` / `refs/tags/archive/ig3d-editor-standalone`: **Ig3dEditor standalone: the owner's decisions (16 Nov 6:58 AM) in ASSET_CHECKLIST.tsv and the plan (generate / replace / convert / keep / hold / remove; workstreams A-F incl. the DeadDays shooter); the 2008 Data folder inventoried name by name (tools/inventory.py -> INVENTORY.md, INVENTORY.tsv: 1,394 files)**
- **07:01** `LIB_GAMES` / `refs/tags/archive/ig3d-editor-works`: **Ig3dEditor 'we know it works' edition: the 2008 iGame3D Data folder (igame3D_2008_Texts: WTF models, Levels, Lua Scripts, Emitters, Fluid, Shaders, OBJ, Help, Exporters), never in git before. Kept here for the Lua / Defold / LOVE return (owner 16 Nov); the standalone edition ships without it**
- **05:37** `LIB_PUBLIC` / `main`: **install: hold the iGame3D Editor back (HOLD; owner 16 Nov: it ships as the standalone edition, LIB_GAMES ig3d-editor-standalone); a reinstall also removes folders it leaves empty. V: reinstalled: 49 titles; t27 expects 49 titles, 4 tools**
- **05:36** `LIB_GAMES` / `refs/tags/archive/ig3d-editor-standalone`: **Ig3dEditor standalone edition: plan (what the editor reaches outside itself, the template Data folder, steps, questions) and the asset checklist for the owner to mark. ig3d-editor-works keeps the edition we know works**
### Sunday, November 15

- **23:00** `LIB_PUBLIC` / `main`: **install: Game.FindFile and LAYOUT 5.2-5.4/5.10 in the model. vibeinstall.py installs the public games from LIB_GAMES install-findfile (main if gone; VIBE_PROJECTS overrides the projects path); libraryfolders.txt lists the other libraries, relative to the exe on its drive; portable.txt keeps Settings/Cache/Data beside the exe; 'manifests' rebuilds appmanifests from game.txt; the uninstaller keeps game folders holding files it didn't install; Public Desktop shortcut; a reinstall removes what the last one made and this one doesn't; set_data_root/data_root model LIB_DATA's forwarding line. Launcher reads relative library paths (t31). escape_sim rerun: dana, sam, riley, chris now WORK; ESCAPES_RESULTS.md, LAYOUT.md (built list, three new questions), README**
- **22:48** `LIB_DATA` / `main`: **Data.SetRoot leaves a forwarding line (Moved to: <folder>) in the default Documents/Data/ROOT.md; Data.Root follows it when data_root.txt is gone and saves the choice again; a missing forwarded folder falls back to Documents/Data with a reason in Data.Error. Data.ForwardedRoot; test hook Data.TestFolders. Headless test OXT-BEYOND/tests/t32_data_forwarding.txt (19 checks, OXT-Beyond and 9.6.3)**
- **22:39** `LIB_GAMES` / `vector-toss-dangle`: **VectorToss: Game.FindFile order (install/LAYOUT.md 5.1) in VT.FindFile: the script's own folder, Vibecode3D Common, the walk up, then the owner's WSL and Linux paths last (bNoWSL turns those off for tests). Test t30**
- **22:36** `LIB_GAMES` / `vector-toss-dangle`: **SquadBuggy: owner's note of 15 Nov 8:16 PM, 'things in two directions at once'. Buildings and water towers along the course (fixed places, never near a flag); snipers on a roof ahead fire slow rounds at the buggy (shoot them or their rounds; a hit throws a soldier off); while they are up the bombers come from behind. Reticle, jump and craters as they were (test t24).**
- **22:36** `LIB_GAMES` / `vector-toss-dangle`: **LightTrailArena: owner's note of 15 Nov 8:08 PM. Top-down stays the default; hold the right button and drag to swing the camera into 3D (it stops at four set angles on the way), let go and it eases back. C steps through the set angles and back to top-down, hold 1-4 for one, 0 for top-down. The play is unchanged (test t25: same ride with the camera swinging).**
- **22:16** `LIB_GAMES` / `vector-toss-dangle`: **GameNotes: every note is a tell for the AI, its own file in the player's Data folder: Data/Games/<Game>/LIB_LLM/tell_<YYYY-MM-DD_HHMMSS>.txt (game, when, state, note); the owner's inbox line only when the inbox exists; test hook Notes.TestRoot (owner, 15 Nov: 'it's the whole vibe')**
- **22:16** `LIB_PUBLIC` / `main`: **install: Data/Games/<key>/LIB_LLM for every game (the tells); data_root.txt in the simulated install points the engine at V:\Documents\Data; LAYOUT row for tells**
- **22:04** `LIB_PUBLIC` / `main`: **launcher: the stack built in OXT-Beyond and saved as Vibecode3D Library.exe; the installer copies the exe beside Vibecode3D.exe**
- **22:02** `LIB_GAMES` / `vector-toss-dangle`: **Antack Fresh: self-sustaining Antack, every terrain, hill and camera made from formulas (no data file, no finder); stubs gain MeshLathe and Xform.Object**
- **21:47** `LIB_PUBLIC` / `main`: **launcher: Vibecode3D Library app for the V: install (library window, Play/Show Folder/Verify, -game <folder> plays from Vibecode3D Common\Engine); installer ships the engine files and the launcher exe**
- **20:20** `LIB_PUBLIC` / `main`: **install: Steam-style Vibecode3D install on V: (vibeinstall.py, 50 titles), escape simulation for twelve personas plus real Windows probes (escape_sim.py), LAYOUT.md, results**
- **20:20** `LIB_USERS` / `main`: **personas: twelve made-up players with real habits and machine quirks, for the install escape simulation**
- **18:27** `LIB_GAMES` / `vector-toss-dangle`: **CraterCrawler: owner's notes of 15 Nov 3:49**
  Saucers cross the sky and fly off (from level 2 some from behind), so
  each passes over the rover once. One following another hangs back; two
  meeting head on collide and fall. A wreck landing ahead sits in a dent:
  jump it (100) or shoot it clear (300).
- **18:24** `LIB_GAMES` / `vector-toss-dangle`: **LightTrailArena: owner's notes of 15 Nov 3:18**
  Two bits always out; riding beside one takes it (reach 1 cell). Taking
  a bit breaks the trail cells within 5 of it (trails redrawn from what
  stands). Rivals hunt the nearest bit and speed up when they get one.
  Each bit has a 12-tick ring clock, flashes its last 3 s, then moves.
  Film lines in the HUD replaced with original ones.
- **18:20** `LIB_GAMES` / `vector-toss-dangle`: **SquadBuggy: owner's notes of 15 Nov 3:06**
  Mouse reticle aims the gun, click fires (hits bombers, bombs, walkers).
  Bombers cross the sky and drop bombs; bombs dig craters too steep to
  drive out of. SPACE jumps in light gravity; land on walkers to squash
  them. Standing still beside a fallen soldier picks him up.
- **18:14** `LIB_GAMES` / `vector-toss-dangle`: **VectorToss: only fatal falls count (owner note 15 Nov 4:44)**
  A fall a hang catches and climbs out of no longer counts toward
  the three falls that end the game.
- **16:41** `LIB_GAMES` / `vector-toss-dangle`: **BlockCityHustle: owner's notes of 15 Nov 1:35**
  E gets out of the car (booths need you on foot). Five booths spread over the city; the next to ring is never one of the last two and away from you when it can be. Every job runs on a clock (42 s, 4 s less a level, 20 at least; time left pays 10 a second; out of time: they hang up, heat +1). A green SPEED bolt (x1.6 for 10 s) turns up on the far half of the city from the package, then from the drop.
- **16:39** `LIB_GAMES` / `vector-toss-dangle`: **BounceRally: camera out a little (play plane 380 -> 480, more road drawn) and more speed (scroll x1.33) (owner's note 15 Nov 1:36)**
- **16:38** `LIB_GAMES` / `vector-toss-dangle`: **Vector Toss: the third fall into a hole ends the game (owner)**
  FALLS n OF 3 under each score; the third fall gets no hang. GAME OVER shows who fell, the level, the best rally and both scores; ENTER or R plays again. Game-over banter.
- **16:31** `LIB_GAMES` / `vector-toss-dangle`: **Vector Toss: shallow holes (5 deep, owner: the tall pit walls cluttered the map and drew below it), heroes dangle and sway on the ledge, catch messages and LEVEL/RALLY moved below the map (they covered the scores and hangs)**
- **16:12** `LIB_GAMES` / `vector-toss-dangle`: **Vector Toss phase 3: the floor breaks**
  From level 2 a dropped ball cracks the 40-unit floor tile it hits; a second hit breaks it into a hole (from level 4 one hit). Heroes who step in fall; a hang catches the edge (1.5 s) and climbs out onto the nearest whole tile (start with one, +1 every 10 points, shown as triangles by the score). With none the fall costs 3 points and the hero comes back. A ball falling through is a drop; its half's hero gets it back. The companion jumps holes in its way. Each new level mends the floor. Owner: walls stay as they are for now (they push the roof throw). Banter for cracks, hangs and falls.
- **16:00** `LIB_GAMES` / `vector-toss-dangle`: **Vector Toss phase 2: levels and walls; instructions stay until two tosses are down**
  Every 10 catches a level. From level 2 a wall rises in each half in front of its hero (x 120, 24 high) and closes in level by level (to x 70, 32 high: always jumpable). A bounce off a wall's inside +1, straight from one wall's inside to the other's +2 more. Heroes can't walk through a wall: SPACE jumps it into the middle; the companion jumps when its catch spot is across its wall. The ghost ball plays the flight out when walls stand. Level banter (4 exchanges).
- **15:47** `LIB_GAMES` / `vector-toss-dangle`: **Vector Toss: mouse aim and roof throws (owner's game notes 15 Nov 3:26-3:39)**
  A ghost ball follows the mouse on the partner's floor; hold the button for power, let go: the ball goes up, hits the roof and comes down on the ghost (aim past a side bound to bank). Run with WASD while aiming; SPACE jumps (catch higher, jump clip from the anims list); TAB toggles the landing ring for loose balls; aim dots removed. Scoring: roof +1, each side +1. Arena wider (720 x 320), slow level-1 throws, round instructions on screen 12 s, messages 4.5 s. Companion throws off the roof near the partner (PROMPT harder, banks more; GLAZE soft).
- **15:32** `LIB_GAMES` / `vector-toss-dangle`: **Vector Toss: high slow arcs (owner: go high, hit apex, come down), ball slower (gravity 0.32 -> 0.16, top speed 14.5 -> 11), heroes faster (4.2 -> 5.2); arc 0.7-1.45 rad, default 1.1; companion styles, easy one and preview retuned**
  The first, flatter tuning is commit 402b75f (owner: fun, but a different game).
- **15:16** `LIB_GAMES` / `vector-toss-dangle`: **Vector Toss phase 1 (core): arena, PROMPT and GLAZE, aim/power/throw/catch, bounces, scoring (flat throws score zero), companion AI, C swap, easy one, aim preview, banter**
  VectorToss/banter.txt holds the heroes' lines (owner-editable); Animations/VectorToss.anims.txt cuts throw, lob and catch from LIB_MOCAP clips (re-cut in the Inspector). Tested headless on OXT-Beyond (OXT-BEYOND/tests/t21_vector_toss.txt, 14 checks).
- **15:16** `xt3D_Raylib_Livecode_Bridge` / `rename-day`: **HUD font: ? , and ' glyphs (VectorText.Init override) for Vector Toss banter; engine regenerated**
- **13:51** `LIB_SYSTEM` / `main`: **TODO: A-84, A-86, A-87 done (not yet seen on screen)**
- **13:50** `LIB_DEV` / `main`: **Game Player: GL.LoadSkin puts a game's active skin (Skins/<Game>/ACTIVE.txt) into gV3DSkin before it starts (A-86)**
- **13:50** `LIB_GAMES` / `refs/tags/archive/editor-tools`: **Ig3dEditor: Window > Inspector, Edit > Replace With Model..., drag a Library model onto the floor (A-84/A-86/A-87)**
- **13:50** `LIB_MOCAP` / `main`: **anim_list: read a game's Animation List (the Inspector writes it) and its In-Out frames (A-84)**
- **13:50** `LIB_ig3d` / `release-checklist`: **Vibecode3D editor tools: Inspector (A-84: pages; Animation = clip preview, In/Out clipper, the game's Animation List), Replace With Model / Skins (A-86), v3d_models (wire previews for A-86/A-87)**
- **13:47** `xt3D_Raylib_Livecode_Bridge` / `rename-day`: **Editor hooks for the Vibecode3D editor (A-86/A-87): Engine.ScreenToFloor (drop point), Skins (Mesh.Define uses gV3DSkin models, scaled to the placeholder), Skin.WTFMesh; engine regenerated**
- **13:37** `LIB_SYSTEM` / `main`: **TODO: A-88 explained, A-89 done, A-90 answered (OXT-Beyond draws dark scroll bars)**
- **13:37** `LIB_ig3d` / `release-checklist`: **A-88: the game design document outline from GameOverViewData's tabs, explained, with Vector Toss as the example**
- **13:36** `LIB_THEME` / `main`: **Theme Studio: the theme menu readable in OXT-Beyond dark mode (option menus draw dark there)**
- **13:35** `LIB_THEME` / `main`: **Theme Studio (TODO A-89/A-90): edit and preview themes/*.txt live, save keeping comments; scrollbar options; Theme.Set; ignore *_dev_* stacks**
- **13:32** `LIB_GAMES` / `refs/tags/archive/ga-turns`: **GeneticAnomaly: turn based (ENTER ends the turn), the advancement economy (each town: recruit / research / train; research raises the Bureau), a big map (64 towns) to scroll and zoom (owner game note 11 14 8:13 PM)**
- **13:26** `LIB_DEV` / `main`: **Status_Browser: a click shows details only (Explorer from the right-click menu); Feedback drafts follow the selected file (also Game Browser)**
- **13:22** `LIB_TTRPG` / `main`: **NEXT: player client notes and the owner's ideas (scene strip, companions)**
- **13:19** `LIB_TTRPG` / `main`: **client: scene modes decide who acts (combat d20+Dex, talk d20+Persuasion/Deception, explore = click a face); stick figure coloured for magic and injuries replaces the big portrait**
- **13:12** `LIB_TTRPG` / `main`: **client: double-click a list line to do it at once (whole action sent to the log)**
- **13:11** `LIB_DEV` / `main`: **dev_version: place the new window where the old was, or centred when off screen; stamp with seconds; visible**
- **13:11** `LIB_TTRPG` / `main`: **client: /x runs xTalk from the chat like the Message Box (keeps the IDE's msg)**
- **13:08** `LIB_DEV` / `main`: **tools/xtalk/dev_version: Dev.NewVersion builds <concept>_dev_<stamp> stacks (owner's stack workflow, 15 Nov)**
- **13:08** `LIB_TTRPG` / `main`: **client: stack script moved to client/livecode/client_main.livecodescript (source of truth); tab reset on Init; ignore *_dev_* stacks**
- **12:56** `LIB_TTRPG` / `main`: **client: TTRPG_Client player window built in OXT-Beyond via the MCP bridge (party faces, skill/weapon/item/spell lists, DM text, log, /llm)**
- **11:32** `LIB_SYSTEM` / `main`: **STATUS: TTRPG resume point**
- **11:32** `LIB_TTRPG` / `main`: **NEXT.md: where TTRPG Studio stands and what comes next**
- **11:12** `LIB_TEST` / `main`: **LIB_TEST: TTRPG Studio rebuilt**
- **11:12** `LIB_TTRPG` / `main`: **TTRPG: asking a character stays talk even with a named skill; self-play 2 recorded (skills keep the story moving)**
- **11:10** `LIB_TEST` / `main`: **LIB_TEST: TTRPG Studio with skill buttons**
- **11:10** `LIB_TTRPG` / `main`: **TTRPG: skills drive the play: 18 D&D skills; a named skill is honoured, opens its own clue, or turns up a lead; named social skills press a secret; skill buttons + 18-skill sheet in the window; self-play player answers skill-first**
  Python reference stub-tested; LiveCode: self, skills, mock and UI tests pass headless. Not yet run with a real model.
