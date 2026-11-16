Overnight, 15-16 Nov 2026. The owner is asleep: no input until morning.

Read memory first: MEMORY.md, then vibe-install-sim.md, spark-roadtrip.md,
headless-livecode-tests.md, oxt-beyond.md, git-branch-workflow.md, review-dashboard.md,
game-notes-inbox.md. Then LIB_SYSTEM/LIB_ALPHA.md, LIB_PUBLIC/install/LAYOUT.md (section 5 is the
plan) and LIB_PUBLIC/launcher/README.md.

Rules:
- Run only ONE Claude session. Check with `ps -eo pid,etime,args | grep claude`; if another
  is running, stop and write that down rather than working alongside it.
- Commit only on branches, using a temporary index (read-tree / update-index / commit-tree /
  update-ref), so the owner's working copies stay as they are. Never merge or push.
- Open no windows in OXT-Beyond and run nothing on the owner's screen. Test headless only:
  OXT-BEYOND/tests/oxt_headless.py --engine beyond, plus xtalk_lint.py.
- Add every file you make or change to the review list (LIB_DEV/tools/for_review.py).
- The owner decides the questions in LAYOUT.md section 6: list them, don't decide them.
- Keep the in-game note box (GameNotes, ` or F2) working in every game: tells go to
  Data/Games/<Game>/LIB_LLM/tell_<timestamp>.txt (branch game-tell, test t29).

Work, in order:

1. The owner's game notes of 15 Nov evening (LIB_LLMIN/LIB_GAMES/GAME_NOTES.txt), on LIB_GAMES
   branch spark-roadtrip. Each change gets a headless test added to t25 or t24, and t22 (smoke)
   still has to pass.
   a. LightTrailArena (8:08 PM): keep the straight top-down 2D view as the default. Right-click
      swings the camera into 3D (drag to pivot), and it can stop at set cinematic angles; add a
      few preset angles on a key (number keys or C to cycle). Releasing it or a key brings it
      back to top-down. The owner loves this game ("work of art"): don't change how it plays.
      The game is the owner's homage to light-cycle games: keep its words and look original,
      never names or lines from TRON or GLTron.
   b. SquadBuggy (8:16 PM): "you need things in two directions at once". Add buildings and
      water towers along the course. Enemies stand on them when they're ahead of you, and while
      you deal with those, bombers attack from behind. Keep the reticle, the jump and the
      craters as they are. The owner said "this IS AMAZING": add to it, don't rework it.
   Once the notes are acted on, move the handled lines to LIB_LLMOUT/Read/LIB_GAMES/ and leave
   GAME_NOTES.txt in place, empty. The CraterCrawler and BlockCityHustle notes are praise: note
   them and move them out too.
2. Game.FindFile (LAYOUT 5.1). Antack, uDead, Thrmnlra, Face, GeneticAnomaly, Amazing_Couple
   and Ig3dEditor (LIB_GAMES main), and VectorToss (branch vector-toss), look in this order:
   the script's own folder (LIB_GAMES/Vibecode3D_Games/X/... becomes <script folder>/X/...),
   then <library>/common/Vibecode3D Common/<path>, then today's walk up, and the wsl$ fallback
   last. Keep each game's own handler name. Branch: install-findfile off main; for VectorToss,
   commit on vector-toss. Headless test t30_install_findfile.txt: load each script from its
   folder on V:, add a test hook that blocks the wsl$ fallback, and check that every file is
   found. Then make vibeinstall.py install from install-findfile, rerun install and verify,
   and check that "data today" is ok.
3. LIB_PUBLIC branch vibe-install (the launcher is there too: read it, don't break t27). In
   vibeinstall.py and escape_sim.py:
   - library paths written relative to the exe on the same drive;
   - portable.txt honoured in the model;
   - appmanifests rebuilt from game.txt;
   - the uninstaller keeps game folders holding files it didn't install;
   - a Public Desktop shortcut.
   Rerun escape_sim.py (~10 min; run it in the background) and update ESCAPES_RESULTS.md.
4. LIB_DATA (branch data-forwarding): when Data.SetRoot moves the Data folder, leave a
   forwarding line in the default Documents/Data/ROOT.md, and have Data.Root follow it when
   data_root.txt is gone. Add a headless test.

To finish: write LIB_SYSTEM/NIGHT_WORK_11_15.md, short and in plain words. Say what was done,
the branch and commit for each piece, what was tested and how, what wasn't (nothing played on
screen), and the open questions. Put "what to play first" at the top, the key for each new
thing included. Then update the memory (spark-roadtrip, vibe-install-sim).
