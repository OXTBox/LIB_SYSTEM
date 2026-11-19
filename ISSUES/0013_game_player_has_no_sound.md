# 0013: the Game Player plays no sound: Audio.Init needs a "Viewport" group

**Status:** open (found, not fixed; the Game Player's issues are parked by the owner, see 0012)
**Opened:** 19 Nov 2026 · **Area:** Game Player (LIB_DEV/livecode/game_player + the generated
engine xt3D_Raylib_Livecode_Bridge/testbench/vibe_engine_xt3d.livecodescript, from Engine 1)

## What was seen
While testing LIB_HOWTO topic 16 (Sound) on the real engine through LIB_HOWTO/tests/play_step.sh
(the Game Player's window, game_launch.livecodescript):
- With a sound folder in place (testbench/Data/Sounds/zap/zap1.wav, zap2.wav; put there for the
  test only, then removed), `Audio.Init` ran with no error but made **0 players**.
- Cause in the engine: `Audio.EnsureGroup` exits when there is no group "Viewport"
  (`if there is not a group "Viewport" then exit`), and `Audio.MakePlayer` creates players
  `in group "AudioPlayers"`. The Game Player's card has no Viewport group, so every
  `Sound.Play` is silent (no error: "none" players).
- Also: the engine's sound folder is `StackDirectory() & "/Data/Sounds"`, i.e. next to the engine
  script (testbench/Data/Sounds for the Game Player), which does not exist there today.

## Not seen
Sound in the Vibecode3D editor stack (Engine 1 with its Viewport group) was not tried; there it
should work as before. Nothing was heard: the test only counted players.

## Fix ideas (not done)
- Audio.EnsureGroup: when there is no Viewport group, create "AudioPlayers" on the card itself.
- Let a game's own folder hold its sounds (Game.FindFile("Sounds/...")) as files already do.
