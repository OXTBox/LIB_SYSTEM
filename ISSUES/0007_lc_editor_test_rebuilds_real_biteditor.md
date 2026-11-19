# 0007: lc_editor_test.txt rebuilds the owner's real BitEditor.livecode

**Status:** open
**Opened:** 18 Nov 2026 · **Area:** LIB_BIT/editor/tests

## What we saw
- Running `LIB_BIT/editor/tests/lc_editor_test.txt` headless rebuilt and saved `BitEditor.livecode` in the
  real LIB_BIT/editor folder (a helper, tube bubble c1795033087850). It was put back at once from git;
  it matches the committed copy again.
- The test is also out of date: it throws at line 89, on main too.
- `lc_feedback_1115_test.txt` throws at `Bit.Blank` when run in a copy of the folder (main too).

## Cause / Fix
Not fixed. The test has no warning and no scratch-copy step. Until fixed: run it only in a copy of the
editor folder (`run_headless.py --root <copy>` / `oxt_headless.py --root <copy>`), never in place.
