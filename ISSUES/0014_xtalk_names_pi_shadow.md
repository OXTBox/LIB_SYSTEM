# 0014: a parameter named pI does not compile (it is the constant pi)

**Status:** fixed (discovery)

**What we saw:** lib_ttrpg_world would not load; `start using` failed quietly and the test said
"can't find handler". Compiling by `set the script` gave `170,662,46,pI` (and before that `219,49,4,tHere`).

**Cause:** xTalk names are case-blind, so `pI` is the built-in constant `pi`. A local named `tHere` was
also refused by the 9.6.3 server (cause not pinned down; renaming it fixed it).

**Fix / workaround:** renamed to `pIt` and `tMyFile`. To see a script-only library's compile error,
`set the script of` a throw-away stack to its text (first line removed) and read `the result`.

**Discoveries:** names to avoid for p/t/s variables: anything that spells a constant (`pi`, `tab`,
`quote`, `comma`, `space`, `empty`, `return`, `up`, `down`) and, to be safe, `tHere`.

**Log**
- 19 Nov 2026: found while porting the TTRPG world code (LIB_TTRPG branch ttrpg-world-code).
