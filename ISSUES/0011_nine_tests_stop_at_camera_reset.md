# 0011: nine headless tests stop at Camera.Reset before they test anything

**Status:** open
**Opened:** 18 Nov 2026 (night) · **Area:** OXT-BEYOND/tests

## What we saw
Run on the owner's folders as they are (nothing of the occlusion-culling work in them), OXT-Beyond engine:
t21 vector toss, t23 block city, t24 squad buggy, t25 light trail, t26 crater crawler, t33 aquarius,
t34 buildings, t35 props levels, t36 deaddays each give one line, `THREW: 573,..,Camera.Reset`
(573 = no such handler), from the game's `Game.OnStart`. 0 checks run in each.

## Cause
The same as t22 and t28 in issue 0006: these tests put the game on the stand-in engine
(`LIB_GAMES/tools/engine_stubs.livecodescript`), which does not have the Rename Day names
(`Camera.Reset`, `Mesh.Box` ...). The games use the new names since the merge.

## Fix (not done: found while checking that the culling work changed nothing)
As t22 and t28 do: add `LIB_ig3d/livecode/contract_aliases.livecodescript` after the stubs when the
test builds its stack script. For t33 to t36 the stubs part comes first and the real-engine part
after it, so the whole test stops before the real engine is reached.

## Why it matters
"Five games' headless tests still pass" cannot be said from t23 to t26 until this is fixed. For the
culling work (Vibecode3D branch `occlusion-culling`) the check was made another way: t22 and t28
(game stand-ins) and t18, t45, t48, t49 (real engine) give the same lines before and after, and eight
real games were played 200 frames on the real engine in each mode with no error.
