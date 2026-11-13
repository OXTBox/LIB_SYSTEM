# STATUS

Friday, November 13, 2026, 01:00. Rewritten at every milestone (OPERATING_PROMPT section 4).

## Running (no Claude usage)
| What | Where | State |
|---|---|---|
| Spark: iGame3D 2008 manifest | Spark's own window; log `LIB_GAMES/igame3D_2008_Texts/_manifest/spark/_run.log` | ~800 requests left (~9 h); `.fl` files skipped; Fluid/Mappers: 5 final builds only |

## Done today
- LIB_SYSTEM started: `LIB_ALPHA.md`, `LIB_OMEGA.md`, `OPERATING_PROMPT.md`, `TODO.md`, this file.
- XTJSON batch: 113 of 115 stacks harvested into `~/projects/XTJSON/batch/`, originals moved to
  `LIB_LLMOUT/LIB_XTJSON/`. Left: `Web_Collector_Watcher_..._newest.livecode` (crashes LiveCode,
  even sampled: A-11) and `Bezier.livecode/__MACOSX/._Bezier.livecode` (Mac junk, not a stack).
- Newest builds of each stack family listed: `XTJSON/batch/_NEWEST.md`; `XTJSON/newest/` links
  the 80 newest harvests (33 older builds left out) (A-13, first half).

## Waiting on the owner (with the default I'll take)
| ID | Question | Default |
|---|---|---|
| O-1 | Correct LIB_ALPHA / OPERATING_PROMPT | they stand as written |
| O-5 | LiveCode Server 9.6.3 Linux zip? | I'll look for it online when you say so |
| Q-1 | LIB_LOGS file name | `<intention>_<result>_<names>_<seconds>.lib_log` |
Full list: `TODO.md`, owner lane.

## Next (AI)
1. A-12: analyse the harvests, newest builds first; GAD/Generica as a reusable template.
2. A-13: move the inbox's non-stack files to LIB_LLMOUT once analysed.
3. A-14: document `customSample`; commit LIB_XTJSON (harvester, batch app, watchdog).
