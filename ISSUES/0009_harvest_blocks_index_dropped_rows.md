# 0009: harvest_blocks rewrote Data/Example's index with only the last harvest

**Status:** fixed (18 Nov 2026)
**Opened:** 18 Nov 2026 · **Area:** LIB_SCRIPTBLOCKS/tools/harvest_blocks.py · **Fix commit:** a55357f (LIB_SCRIPTBLOCKS)

## What we saw
Harvesting Scott Rossi's nine ball into LIB_GENERICA/Data/Example left index.tsv and INDEX.md with 10 rows;
the 61 rows from GAD_WORKING and GenericaProperties were gone (their files were still on disk).
Also, a block file (scriptBlocks/<Category>.txt) was rewritten with only the new stack's handlers,
although the help says a second harvest adds a section per source.

## Fix
The index is now rebuilt from every file's `--` header on disk, and a block file keeps the sections
from other sources. Tested on a copy: nine ball, then GAD again: 81 rows, Math keeps both sources (20 handlers).
