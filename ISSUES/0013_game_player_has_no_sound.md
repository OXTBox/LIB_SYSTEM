# 0013: the Game Player plays no sound: Audio.Init needs a "Viewport" group

**Status:** fixed 23 Nov 2026 on branches `sound-kit` (Vibecode3D, xt3D bridge, LIB_DEV, LIB_SFX), waits for the owner's ears
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

## Fixed (23 Nov 2026, p1-09)
- Audio.EnsureGroup: no Viewport group -> an invisible "AudioPlayers" group on the card.
- Audio.Roots: sounds/music from the game's own `Vibecode3D_Games/Audio/<Game>/`, the stack's
  `Data/`, `Vibecode3D Common/`, then the shared kit `LIB_SFX/kit` (42 LIB_SFX sounds in 20
  types, 5 chip songs). Audio.Init runs again for each new window (it used to run once only).
- Game Player: Player.SoundStart before Game.OnStart, music starts with the game, pauses with
  Escape, stops on quit; Engine.Has("sound") / ("music") true when loaded.
- Test: OXT-BEYOND/tests/t78_sound_back.txt 16/16 (players counted, nothing heard).
- Still: only Canyon and Hunter call Sound.Play; the other 59 games have music but no effects yet.
