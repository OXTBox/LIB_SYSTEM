# 0004: GAD battles: your Base's units followed the squad instead of their point

**Status:** fixed, waits for the owner's play (18 Nov 2026)
**Opened:** 18 Nov 2026 · **Area:** LIB_GAD/battles (branch gad-battles) · **Fix commit:** 97646fb

## What we saw (owner)
Clicked my Base, sent its units to an arbitrary point, clicked the squad, sent it to the enemy: the Base
took the same target as the squad instead of keeping the point.

## Cause (most likely; his game was closed, so its state could not be read)
A click looks for units first, then X marks, then Bases. When the Base's second click lands where your
own units are standing (on the point or the X), it hits the unit, not the place. The Base's send-to
became that unit, so when the unit's squad marched off, the Base's new units followed it. Seen in the
headless test: clicking the X with a squad waiting on it gave the squad.
The rules alone (Base -> point, squad -> enemy) keep the point: checked headless.

## Fix
gad_battles_ui `GADUI.Click`: a Base sent onto one of your own units or squads takes that spot, or the
X it stands on; it never follows a unit. Enemy units are still followed. Two checks in t_gad_battles (73 PASS, 0 FAIL).

## Discoveries
Rule of thumb for map UIs: a Base's target is a place; only units chase things.
