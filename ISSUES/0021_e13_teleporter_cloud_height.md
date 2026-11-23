# 0021 E13 test: the teleporter lands the hero at y 265, the test wants 231

- State: open (seen 23 Nov 2026; already on LIB_EDITOR main, not caused by lean-water-off)
- Where: LIB_EDITOR/tests/e13_test.sh line 9 of its output:
  `FAIL the teleporter sends the hero to a cloud: 15,4|y 265|... (wanted 15,4|y 231|path)`
- Same result with the lean-water-off change stashed, so the map (wizard_pool) or the walk rules moved
  since the test's number was written. Next: see whether 265 is the right cloud height now
  (wizard_pool's clouds) and update the test, or find what lifted the hero 34 hu.
