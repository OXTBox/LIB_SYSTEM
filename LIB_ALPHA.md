# LIB_ALPHA: read this first

Friday, November 13, 2026. Draft 1, written by Claude (Opus 5.5) from the owner's notes
(`LIB_LLMOUT/Read/LIB_SYSTEM/Notes To Claude 1207AM_11_13_2026.txt`, `LIB_ARRAY/Notes To Claude 756PM_11_12_2026.txt`)
and two days of working memory. The owner corrects it; every AI model, agent or person
working in `~/projects` reads it before any important task, and again whenever they lose the
thread. `LIB_OMEGA.md` holds the lessons that made these rules; `OPERATING_PROMPT.md` says how
the AIs run the work; `TODO.md` is the list; `STATUS.md` is today.

## 1. What this is

`~/projects` is one project, the **LIB_ARRAY**: game engines, games and the libraries they are
built from, made by the owner with AI models. Its goal: a complete, long-term suite of game
development, programming and AI-integration assets, each part usable alone and all of it
together, independent of external assets and code where possible.

The closing argument for every tool: **"Does it stand alone, and is it, as a whole, easy and
enjoyable enough to use to put away the old IDE?"**

Public framing: the engines (Vibecode3D, xt3d) are the interface to vibecoding; the LIB_* are
the parts the AI builds with; the language is **xTalk**, from the HyperCard family. Never
mention LiveCode 9.6.3 or the Community edition in public material (internally it is what runs).

## 2. The map

| Part | What it is |
|---|---|
| **Engines** | |
| `Vibecode3D` | the owner's 3D engine and editor in xTalk: vector wireframes, 1983 arcade look |
| `xt3D_Raylib_Livecode_Bridge` (xt3d) | xTalk drives the raylib 3D engine (C bridge) |
| `iGame3D_2026_CLAUDE` | writable copy of the 2008 iGame3D (Lua) for real-engine tests; physics broken, fake them |
| `xtalk_py` | xTalk runtime in Python + the script corpus (`corpus/INDEX.md`) |
| **Games** | |
| `LIB_GAMES` | small, teachable games and demos (Vibecode3D_Games, xt3d_Games); the Sequencer |
| `PROMPT_GLAZE` | the umbrella game: two heroes dropped into every game we build |
| **Libraries** | |
| `LIB_MCP` | lets Claude, a local model or any tool drive a running LiveCode (dev server, `tools/lcmcp`) |
| `LIB_XTJSON` | LiveCode stacks <-> JSON (harvest, rebuild, batch app) |
| `LIB_BIT` / `LIB_MAP` / `LIB_TRACE` | 1-bit grids / levels from grids / bitmap to shapes |
| `LIB_MOCAP` / `LIB_BVH` | video -> motion capture -> characters / the BVH motion library (local only: rights unsettled) |
| `LIB_DATA` | the one Data folder every app loads and saves through (`Documents/Data`) |
| `LIB_GAD` | Galactica (Ed Zavada) reference; GAD = Generic Any Data; our Genetic Anomaly Detector |
| `LIB_GENERICA` | a game's words as plain label files (Galactica's 533 labels; themes overlay a base): retheme by editing labels, not code |
| `LIB_SCRIPTBLOCKS` | harvest, manage and export script blocks: GAD's code palette as its own stack and library; edits examples and other stacks, never its own source |
| `LIB_ig3d` | where the worlds converge: glossary, procedures, engine categories |
| `LIB_PUBLIC` | the public page |
| `LIB_GLOBALS` | (planned) every global name, its use, and its Python equivalent |
| `LIB_USERS` | (planned) who is at the controls: owner, Claude, Spark, other agents |
| `LIB_SYSTEM` | this: the rules and the plan |
| `LIB_BIN` | third-party applications (e.g. LiveCode Server 9.6.3 Linux) in versioned folders; git keeps only README + MANIFEST; internal only |
| **Passing through** | |
| `LIB_LLMIN/<project>/` | the inbox: the owner drops anything for the AIs here |
| `LIB_LLMOUT/Read/<project>/` | read and acted on: items move here, never deleted |
| `LIB_TEST/` | (planned) what the owner should open and try now |
| `LIB_LOGS/` | (planned) saved test stacks and their results |
| `XTJSON/` | harvests of the owner's stacks (data, not a repository) |

## 3. Who works here

| Who | Use for |
|---|---|
| **The owner** | decisions, taste ("was it fun?"), playing tests, the IDE, saving stacks, anything only a person can judge |
| **Fable 5.2** | architecture, the grand scheme, hard design, reviewing plans; expensive: use for structure, not volume |
| **Opus 5.5** | the daily engineer: code, debugging, testing through LIB_MCP, reviews, writing |
| **Sonnet / Haiku 5.5** | mechanical, well-specified jobs: renames, format conversion, summaries, first-pass checks |
| **Spark** (local, LM Studio `spark-x2.6-4b`) | unmetered bulk: first-look catalogues and drafts, always reviewed before use |

Details and routing rules: `OPERATING_PROMPT.md`.

## 4. Rules

### Files and folders
1. Inputs arrive in `LIB_LLMIN/<project>/`. Once read AND acted on, MOVE them to
   `LIB_LLMOUT/Read/<project>/` (log where the work went). Never make `input/` folders in a project.
2. **Every `LIB_` folder is its own git repository** (the owner, 2026-11-13: "as if we might
   suddenly change base programming paradigms and lib it all over again"). A new LIB_ gets
   `git init -b main` and a first commit the day it is made. Passing or third-party bulk is
   ignored, not tracked: LIB_LLMIN/LIB_LLMOUT keep only their READMEs, LIB_GAD ignores the
   downloaded Galactica source trees.
2. Each project keeps a `README.md` (what, how to use) and, for AI notes, a `CLAUDE.md`.
3. Never leave loose scripts around `~/projects`: scripts belong to a project or the corpus.
4. **Images are ignored** (the owner, 2026-11-13, "SUPER_IMPORTANT"): PNG and every other image
   file are not opened, read or sent to any model, Spark included, unless absolutely necessary,
   until further notice. Count them, list their names if it matters; that is all.
4b. **Provenance, then dedupe** (same note): for every file kind (`*.ext`), record where each copy
   was, what required it, where it changed and where it came from (a record per project:
   `PROVENANCE.md` + a machine-readable `provenance.tsv`); then remove the OLDEST redundant
   copies (move them to `LIB_LLMOUT/Read/`, never delete), keeping the newest and the record.
5. Big data (harvests, captures, model files): query it with a script, never read it whole.

### Git
6. Foundation work (LIB_*, tools, shared docs) goes on `main`. Each game, concept or app gets
   its own branch; it merges only after the owner reviews it.
7. Commit as you go, on branches (the owner, 2026-11-13: "work to the five hour limits with branch
   commits"): each piece of work on a branch named after it; the owner reviews and merges.
   Never push; never merge to main yourself. If the owner has another branch checked out,
   commit with a temporary index (no checkout).
8. Commit messages end with the co-author line the session gives.

### LiveCode work
9. Compile-check every script change: `LIB_MCP/tools/lcmcp compile <file>`; lint too.
10. Test in the running app through LIB_MCP (`lcmcp run/eval/snap`); look at the screenshot.
11. Read `Vibecode3D/LiveCode_Claude_Kit/kit/docs/livecode-gotchas.md` before writing LiveCode.
12. Library code must not depend on the IDE; every app loads and saves through LIB_DATA.

### Windows the owner sees (from the owner's notes, 2026-11-13)
13. **Title of every window an AI, agent or person is driving:**
    `"<MCP NAME OR URL>" && "|" && <USERS> && <what is being tested>`, e.g.
    `127.0.0.1:8769 | CLAUDE | Do you see particle effects?`
14. **Title of a window the owner should try:** `"FOR" && <USERS> && "|" && <what to do first,
    which key or button for more>`, e.g. `FOR OWNER | Press Space to start, H for help`.
15. Anything the owner should open and try goes in `LIB_TEST/`. Once confirmed, it moves to
    `LIB_TEST/tested/` with its extension changed to its LIB name, in the commit that lands it.
16. Each test stack is saved with its result in `LIB_LOGS/LIB_<name>/` as
    `<intention>_<result>_<vocabulary names>.livecode` & the seconds & `.lib_log`
    (owner's spelling; the exact form is question Q-1 in TODO.md).
17. **Every stack has an About card**, and every LIB a one-page About for public git (LIB_ABOUT),
    always beginning with: the long date; the stack NAME; the stack title; what it is built to
    do; how to do it (keyboard/mouse-aware bullets); how to report success or failure, and
    whether another process is watching the result. The goal may simply be "was it fun?".

### In every test stack and game
18. **Escape first pauses every loop.** The pause has  in developer mode has developer options; this is to confgure defaults for common HUMAN use. Such as the game's speed, delay between texts/scenes.
19. A toggle opens an MCP command line inside the window, lower left (8/10 down).
20. Otherwise fall back to card `Developer` (card 1, blank for now); cards laid out on screen
    as a grid, like raylib's web examples page.
21. Games: THIS IS INSTRUCTION ONLY FOR THE THRMNCLR GAME: keep the player typing, but not much: answers grow by one letter per level
    (Y/N, then OK/NO, then YAY/NAY). Pace for fitness-of-service tests (a G.O.A.T.-style test),
    not speed: the owner found Thrmnlra "way too fast". Each game is going to have 

### Working with the owner
22. Plain words, short tables; no raw JSON dumps. Say what was tested and what wasn't.
23. Post the owner's tasks (and Spark's) far ahead of when they are needed (`TODO.md`).
24. Never sit idle waiting for an answer: ask, then work on something else (`OPERATING_PROMPT.md`).
25. Report outcomes faithfully: failures with the evidence, guesses labelled as guesses.

### FABLE 5 EATS ACCOUNT USAGE TIME 10x faster
26. Use the Fable 5 only for the most absolutely complex tasks , suggest what those are and when we'll need to run them ahead of time. Owner  got it wrong and chewed through 5 hours of AI assistance  access time  in just 11 minutes.
