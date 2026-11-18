# 0002: vmmem keeps ~4 GB of RAM with nothing running

**Status:** open (update + settings planned 18 Nov)
**Opened:** 18 Nov 2026 · **Area:** WSL / memory

## What we saw
With no terminal and no application doing anything, Windows Task Manager showed vmmem (the WSL2 virtual
machine) holding about 4 GB of RAM. The machine has 16 GB; Linux is given ~12 GB.

## Cause
Known WSL2 behaviour: Linux uses spare RAM as file cache and the virtual machine doesn't hand it back to
Windows. The old built-in WSL we run (see 0001) has no way to return it automatically.

## Fix / workaround
- Now: `wsl --shutdown` from a Windows terminal frees it all (closes every WSL window and session).
- Lasting, step 1: `wsl --update` (to the Store WSL). Then `wsl --version` should answer with version numbers.
- Lasting, step 2: a file `C:\Users\<you>\.wslconfig` with, for example:

      [wsl2]
      memory=8GB

      [experimental]
      autoMemoryReclaim=gradual

  `memory=` caps what WSL may take; `autoMemoryReclaim` gives cache back to Windows when Linux is idle
  (needs the updated WSL). Takes effect after `wsl --shutdown`. Pick the cap after seeing what the
  LLMs need (qwen 7B + 2B already use ~95% of RAM, see LIB_TTRPG notes): `8GB` may be too low then.

## Discoveries
- vmmem's size is not a leak in our programs; check `free -h` inside Linux: "buff/cache" is the part held.

## Log
- 18 Nov 2026: seen by the owner during the bug hunt; ticket opened. Owner to run `wsl --update` next.
