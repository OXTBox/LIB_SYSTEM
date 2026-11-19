# 0005: t39 board test: two On Git or Not checks fail

**Status:** open
**Opened:** 18 Nov 2026 · **Area:** LIB_DEV boards (On Git or Not) / OXT-BEYOND/tests/t39_board_canvas.txt

## What we saw
t39 passes 87 of 89 checks. The two that fail are On Git or Not's "grey chip" and "ignored popup groups".
They fail the same way on LIB_MENU main, before the menu-folders change, so the menu work did not cause them.
Found by the helper doing the "Menu folders your way" bubble.

## Cause
Not looked at yet. Maybe the test still expects an older board, or the board changed.

## Fix
None yet.
