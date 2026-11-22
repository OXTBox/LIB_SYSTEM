# 0015 Games that use Tab, now that Tab belongs to the console (open, 22 Nov 2026)

**Owner, 22 Nov:** "we may still have games using the TAB key for game interaction that will need to have
that key replaced."

Tab is now the console's key (the menu of words): in iGame3D XT's Window > Console, and in the xt3d Games
bench, where the console is always under the view and **a Tab anywhere in the bench opens the console's
menu** (the bench's stack `on tabKey`, added so Tab works after the line loses the keyboard).

## The games that use Tab (found 22 Nov by searching for 65289 / tabKey)
| game | what Tab does | how it reads it |
|---|---|---|
| Amazing_Couple | switch between the two characters (Couple.Switch) | keysDown 65289 or 9 |
| PromptAndGlazeMaze | swap the active one (3 - sActive) | keysDown 65289 |
| VectorToss | show / hide the landing mark (sShowLand) | keysDown 65289 |
| PhotonBall | show / hide the landing mark (sShowLand) | keysDown 65289 |
| Thrmnlra | cycle the focus among the enemy missiles (+2 doom ticks) | card `on tabKey` |

All in `LIB_GAMES/Vibecode3D_Games/Vibecode3D_Play_<name>.livecodescript`.

## What happens today
- Game Player (XT engine): no console there yet, so these games are unchanged.
- xt3d Games bench: the keysDown games still see Tab, but the bench's stack `tabKey` also pops the console
  menu over the game. Thrmnlra's card `tabKey` comes first (the card is before the stack), so it keeps Tab.

## To do (owner's call which key)
1. Pick a replacement key for each game's Tab action (one key for all "switch / swap" would be easiest).
2. Change the five games; keep the old Tab working in the Game Player until the console reaches it?
3. Meanwhile, a cheap guard is possible: the bench's `tabKey` passes Tab on while a game plays (sGameOn)
   unless the console line has the keyboard.
