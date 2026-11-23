# 0017 Two arrow keys held on the Genetic Anomaly star map crash the XT engine (key presses pile up as pending messages) (open, 22 Nov 2026)

**Found by:** play test 0001 (21 Nov 2026), from the owner's notes; logged by Claude (Fable), not yet looked into.

## What happened
Holding two arrow keys to scroll the Genetic Anomaly star map crashed Vibecode3D (the pure xTalk engine).
The owner's reading: key presses pile up in the message queue (the pendingMessages kind of trouble).

## Next
p1-05: one guard in the engine or Game Player (read keys once a frame, drop repeats still waiting), a held-key test with no window, then every game that reads keys by message (game_scan.py).
Plan: LIB_DEV/PriorityTube/PLAYTEST_0001_PLAN.md
