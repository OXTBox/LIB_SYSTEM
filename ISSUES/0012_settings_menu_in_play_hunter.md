# 0012: the Settings (Options) menu during play: missing in Hunter, Escape goes to the Developer card

**Status:** parked (owner, 19 Nov: "we'll return to that whole Vibecode player and its issues at another time")
**Opened:** 19 Nov 2026 · **Area:** Vibecode3D GUI stack (VIBECODE3D_GUI_v1), LIB_GAMES Hunter

## What the owner saw (19 Nov, after the HIDING tab went in)
- The Settings group with the new HIDING tab showed once on the Title card.
- **Canyon:** the Settings menu shows during play. Fine.
- **Hunter:** the Settings menu does not show during play. After using Settings, Escape puts the
  IDE on the pointer tool and goes to the Developer card, instead of closing Settings and going
  back to the game.
- The culling itself looks great (the owner).

## Leads (not chased)
- Hunter's `opencard` hides `OptionsGroup` and `PauseMenuGroup` (Vibecode3D_Play_Hunter.livecodescript ~871).
- Hunter's `Hunter.Move` reads Escape from `the keysDown` every tick (~433): releases the mouse,
  sets bPaused true / bPlaying false, `choose "pointer tool"`, then `Reselect.browse` in 600 ms.
  This runs alongside the engine's own Escape (pause menu, again = Developer card), so with a menu
  open one Escape can do both. Canyon has no such block.
- Menus are copies of the templates made by Menu.Open on the current card; Menu.Purge deletes
  hidden copies on Play.* cards (closeCard).

## Not a culling problem
The hiding code (gCullMode / gCullDefault, Cull.*) does not touch menus or keys; the tab code only
shows/hides controls inside the Options group.
