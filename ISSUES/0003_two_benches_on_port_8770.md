# 0003: Game Browser froze: two xt3d benches on port 8770 + shell() freezes

**Status:** fixed (18 Nov 2026)
**Opened:** 18 Nov 2026 · **Area:** ports / LIB_DEV / LIB_MCP · **Full notes:** Next_Steps_With_Claude/PORTS_AND_BROWSER_FREEZE_11_18_2026.md

## What we saw
The Game Browser stopped responding for ~30 s when a game was picked to play on xt3d.

## Cause
1. Two benches listened on port 8770; on Windows, LiveCode's `accept connections on port` succeeds even
   when the port is taken. The second copy overwrote the token file, so the first rejected every request.
2. The browser checked the bench with `shell("curl.exe -m 15 ...")`, which freezes the window.
3. Slow program starts from 0001 made every `shell()` 20-50 s.

## Fix
LIB_PORTS (registry, rules, Ports window); LIB_MCP `DevServer.Start` refuses a port in use; both bench
launchers close a second copy; the browser talks HTTP over its own socket and starts programs with
`open process ... for neither`.

## Discoveries
- Closing a socket that is still connecting lets its late error land on the next socket (error 10038).
  See LIB_PORTS/RULES.md rule 3.

## Log
- 18 Nov 2026: found, fixed, tested, merged (Opus); owner approved the rebuilt GAME_Browser.exe.
