# 0001: wsl.exe at ~60% CPU, Windows program starts 20-50 s

**Status:** workaround (cause: WSL; lasting fix = update WSL, see 0002)
**Opened:** 18 Nov 2026 · **Area:** WSL / Windows · **Full notes:** Next_Steps_With_Claude/WSL_CPU_11_18_2026.md

## What we saw
- Task Manager: "Windows Subsystem for Linux launcher" (wsl.exe) at a steady ~60% CPU, about 6 cores,
  4 h 37 min of CPU in total. Linux itself was idle (99.8% idle, load 0.04).
- That wsl.exe was the terminal of a long Claude Code session (started 00:24 in an old-style PowerShell console).
- Every Windows program started from WSL, and every `shell()` in LiveCode on Windows, took 20-50 s
  (`cmd /c echo` 20 s, `tasklist` 22 s). Normal is about 250 ms.

## How we found it
The owner closed our apps one at a time: OXT-Beyond, Game Player, the xt3d games bench, the LIB_MCP server.
No change after any of them. The bug hunt ended with the owner's verdict: **100% a WSL issue all around**,
none of our code.

## Cause
WSL: the wsl.exe that relays a long-running terminal session, on the old built-in WSL
(`wsl.exe --version` says "Invalid command line option", so this is the in-Windows WSL, not the
Store one; kernel 5.10.16.3). Antivirus (McAfee + Malwarebytes) checking new processes was a second
suspect for the slow starts; not needed to explain it in the end.

## Fix / workaround
- Now: close the terminal that runs the long session and start a fresh one (Windows Terminal preferred).
  `wsl --shutdown` from Windows clears everything.
- Lasting: `wsl --update` to the current WSL (planned 18 Nov, together with 0002).

## Discoveries
- Interactive xTalk must not depend on `shell()`: it freezes the window, and on a bad day each call costs 20-50 s.
  Use sockets or `open process ... for neither` (see 0003).
- When Windows feels slow, check wsl.exe in Task Manager first, before suspecting our apps.

## Log
- 18 Nov 2026 ~09:30: found and measured (Opus).
- 18 Nov 2026: owner confirmed WSL as the cause; ticket opened.
