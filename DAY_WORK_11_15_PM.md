# Day work, 15 November 2026, later (Claude Fable): the BitEditor, from the owner's notes

Source: `LIB_LLMOUT/Read/LIB_BIT/editor/Bills_Notes_on_Editor_1115206.txt` (seven notes).
Branches (not merged): LIB_BIT `biteditor-feedback`, LIB_THEME `tabstrip`. The working files in
both folders ARE the new ones (main is checked out; the commits were made beside it), so
`Build.Editor` builds the new editor now.

| Note | State |
|---|---|
| Height makes a cube, does not extrude the shape | Done as a map option: Mesh > Extrude: Glyph Shape (`extrude glyph`, CELLMAP_V2.md 4b). LiveCode and Python give the same segments and walks. Default stays Whole Cell |
| Brush input (mouseStillDown) on the bitmap grid | Done, board and map: a stroke is followed every 15 ms, every cell on the way is painted |
| Mirror H / V toggles while drawing, and once | Done: Bit menu, guide lines on the board |
| Tab menus light grey on white: draw them | Done: `Theme.TabStrip` (LIB_THEME), used by the BitEditor |
| Paint in the 3D scene: a plan; Clutter brush in it | `LIB_BIT/editor/PLAN_3D_PAINT_AND_CLUTTER.md`. After the owner's answers the first part is BUILT: left button paints in the 3D preview (`CellMap.Pick`), right button held = camera mode (drag turns, W A S D R F move). Heights by drag and Clutter: still plan |
| Undo: each change its own index, each mouseDown one undo | Done: Edit menu, Ctrl+Z / Ctrl+Y, timed history, export as text |

Also: `Build.Editor` refuses a script that does not compile (the 07:54 "BUG!" stack: built
while the script was mid-edit); `editor/tests/run_headless.py` runs the LiveCode tests on the
LiveCode server in WSL with no window (found today: the server builds stacks, controls,
imageData; no snapshots, no mouse).

## Tested, and how
- `python3 -I editor/tests/py_v2_test.py`: ALL OK (old checks unchanged + 6 for extrude glyph).
- Headless LiveCode 9.6.3 server: `lc_v2_test` (segments and walks equal to Python's, both
  extrude modes), `lc_feedback_1115_test` (31 checks: tabs, strokes, mirrors, undo / redo,
  resize undo, extrude toggle saved, history file), `lc_layout2_test`; the last two in a copy.
- NOT tested: anything a real window shows or a real mouse does: the look of the drawn tabs,
  the guide lines, the feel and speed of a drag, the Ctrl+Z keys, the menu check marks on
  Windows. The owner's rebuild is the test.
- By mistake `LIB_BIT/tests/run_tests.py` was run once (it passed): it uses the LIB_MCP
  standalone, which may have opened on the owner's desktop.

## Waiting on the owner
Questions 1 and 2 answered (left paints / right camera with WASD RF; new maps Whole Cell).
Left: clutter kinds, clutter blocking, undo across maps, each with its default in the plan.
3D painting was tested headless only (the cell drawn at a point is the cell picked there, also
after turning and moving the camera; key codes; move directions). The real right button, the
keys held down and the speed are the owner's to try.
