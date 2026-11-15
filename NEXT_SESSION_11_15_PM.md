# Next session prompt (2026-11-15, later): the BitEditor, from the owner's feedback

Paste everything below the line into a fresh Claude Code session in `~/projects`.

---

Read `LIB_SYSTEM/LIB_ALPHA.md`, then `LIB_SYSTEM/DAY_WORK_11_15.md` (what happened this morning)
and `LIB_BIT/editor/README.md`. Run `git status` in LIB_BIT before touching it. Keep a progress
file `LIB_SYSTEM/DAY_WORK_11_15_PM.md`, add every file you make with
`python3 -I ~/projects/LIB_DEV/tools/for_review.py add <path> "work done"`, and keep
`bash LIB_DEV/tools/wait_for_tell.sh` running in the background (restart it each time it exits).

## The focus: the owner's feedback on the BitEditor (layout 2)

This morning the owner built Fable's layout 2 of the BitEditor for the first time
(`Build.Editor`, from `LIB_BIT/editor/livecode/build_editor.livecodescript`) and said "Wow that
looks amazing". He is now testing it by hand. **Everything this session is about his notes on
it**: read them first, fix them in order, ask when a note is unclear, and say plainly what was
tested and how.

### Where his notes arrive
1. `python3 -I ~/projects/LIB_DEV/tools/for_review.py feedback`: the review list (entries for
   `LIB_BIT/editor/BitEditor.livecode`, `editor_stack.livecodescript`, `build_editor.livecodescript`,
   `CELLMAP_V2.md`, maps). Only lines after 2026-11-15 06:00 are new.
2. `LIB_LLMIN/LIB_DEV/TELL_CLAUDE.txt` (his "Tell Claude" button) and anything new in
   `LIB_LLMIN/LIB_BIT/` or `LIB_LLMIN/LIB_EDITOR/` (move each to `LIB_LLMOUT/Read/<project>/` when done).
3. What he types in the session.
Log each note and what you did about it in `LIB_LLMOUT/Read/LIB_DEV/FEEDBACK_HANDLED.txt`.

### Older BitEditor notes to check against layout 2 (14 Nov; were they fixed?)
- 10:33 "BUG: the menus are all light gray on white ... a style sheet to run once before building
  any stacks? LIB_THEME?" (LIB_THEME exists; `build_editor` calls `Theme.Begin`; check it on screen).
- 11:08 a menu of the 1-bit 16x16 graphics (the Aquarius font: L corners, slopes, box-drawing
  glyphs); paint glyphs to cells in 1bit mode; the 1bit view as one big PBM of the glyphs.
- 11:24 "the fonts don't show up in the list and I can't paint on the map with them".
- 11:57 the Heights paint mode (floor / ceiling greys, red down, green / blue up): built 14 Nov.
- 5:31 (15 Nov) LiveCode's white scrollbars spoil the dark look (TODO A-90; A-89 a theme stack).
Say which of these layout 2 already answers, as he sees it.

### How the editor is made (edit the text, never the saved stack)
- `editor/livecode/editor_stack.livecodescript`: the stack script (layout 2; its header says
  what each part does). `editor/livecode/build_editor.livecodescript`: builds the stack from
  scratch and saves `editor/BitEditor.livecode`. `editor/livecode/lib_cellmap.livecodescript`:
  cellmap v2 (the Python twin `editor/python/cellmap.py` must give the same answers; its tests
  are in `LIB_BIT/tests` and `editor/tests`).
- The owner rebuilds with two lines in the message box (close any open "BitEditor" first; his
  old one is saved as `editor/BitEditor_GUI_to_Be_CHANGED.livecode`):
  ```
  start using stack "//wsl$/Ubuntu/home/igame3d/projects/LIB_BIT/editor/livecode/build_editor.livecodescript"
  Build.Editor "//wsl$/Ubuntu/home/igame3d/projects/LIB_BIT/editor"
  ```
- Work on a branch `biteditor-feedback` in LIB_BIT (he may have main checked out: commit with a
  temporary index if so). Never merge it yourself.

### Checking your changes
- **Compile, with no window:** `python3 -I ~/projects/LIB_MCP/python/lib_mcp/compile_headless.py
  <files>` (the LiveCode 9.6.3 server in WSL; found this morning; syntax only). Do it on every
  change. Lint too: `lcmcp lint` (pure Python).
- **Running it:** ask the owner first whether you may open windows. Options, in order:
  (a) **OXT-Beyond**, the owner's dark-mode xTalk IDE, which he is installing during his break as
  YOUR edition so you don't share his IDE. Ask for its path. Set it up: a launcher that starts
  the LIB_MCP dev server inside it on **port 8768** (his IDE is 8766, the standalone 8767), stack
  titles by LIB_ALPHA rules 13/14, `gNoMouse`-style care, and ask him to put it on a second Windows
  desktop (Win+Ctrl+D; he has one monitor). OXT is a fork of the 9.6.3 engine: treat a pass there as
  likely, and keep the last word on his 9.6.3 (headless compile + his own look).
  (b) The LIB_MCP standalone (`lcmcp`, port 8767): only with his OK; close it when done.
  (c) Ask him to rebuild and look, and tell him exactly what to click.
- Headless smoke test that already exists: `editor/tests/lc_layout2_test.txt` (builds in a copy,
  paints, hovers, turns, saves, exports a snapshot).
- Images: do not open screenshots unless absolutely necessary (LIB_ALPHA rule 4). Prefer reading
  state back (`Ed.State()`, field "Status").

### Then, if his notes are done
1. Spark: the procedural entity pilot (`LIB_SPARK/entities`). Round 2 (recipes with y up,
   checked RELATIONS, ground objects set down, last recipe read) ran this morning: review
   `entities/out/*/` against round 1 (`out/round1`), write the verdicts into
   `LIB_SPARK/entities/REVIEW.md`, and if most pass, queue the next 12 from the game designs.
   Spark keeps the pace in `LIB_SPARK/arcade/pace.txt` (10 900) and the shared work clock.
2. Waiting from this morning (owner's word needed): Amazing Couple's Q/E kicks and F pick-up
   (branch `couple-cellmap`, compiles, not played); Fuel Line's lighter traffic (`spark-roadtrip`,
   compiles, not played); the engine's tArray renames (Vibecode3D branch `clear-names`, compiles);
   the 58 DeadDays BVH (rotation order to be seen moving); TTRPG Studio is Fable's (prompt in
   `Next_Steps_With_Claude/FABLE_PROMPT_TTRPG_STUDIO_11_15_2026.md`): don't start it yourself.
