# 0008: BitEditor erases the glyphs completely (BUGGED, parked)

**Status:** bugged (parked by the owner) · **Opened:** 18 Nov 2026 · **Area:** LIB_BIT/editor

## What we saw
- The owner, 18 Nov evening, after trying the heights work (branch `heights-floor-ceiling`,
  `LIB_BIT/editor/BitEditor_HEIGHTS_TRY.livecode`): "bit editor is completely erasing the glyphs".
- Not reproduced or looked into yet: which tab, which action (painting, From brush, opening a map)
  and whether the glyphs are lost from the map or only not drawn are unknown.

## Owner's word
"Let's put that as BUGGED and needs perhaps visual clarification in the future and we'll move on to
other things, our procedural levels are more valuable than making editing tools right now."

## When it is picked up again
- Ask him what he did just before (tab, tool, map), check whether the map file's [design] layer
  changed (data lost) or only the picture (drawing). Suspects: the Heights tab draws glyphs in the
  floor/ceiling colours, so a floor colour equal to the ceiling colour hides them; edFromMarks
  (new 18 Nov) overwrites rows of the cell picture.
- The branch `heights-floor-ceiling` (LIB_BIT, LIB_EDITOR) is not merged; the library part
  (bands, [from] layer) is tested and does not depend on the editor.
- "Visual clarification": how the Heights view shows glyphs, bands and From flags needs a rethink.
