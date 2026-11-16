# Night shutdown: what to put to sleep when the owner is away

Monday, November 16, 2026. Draft 1, Claude (Opus 5.5), from the owner's note: "anything you have
check repeatedly get put to sleep while I'm asleep or away from keyboard" (27% of the week's
usage spent in under 15 hours).

Account usage is spent only when a Claude session takes a turn. An idle session costs nothing.
What costs is a session **waking**: every turn re-reads its whole conversation, and a long
`claude --continue` session has a large one.

## What can wake a session, and what to do with it

| Thing | What wakes it | Night rule |
|---|---|---|
| `OXT-BEYOND/sessions/wait_for_llm.sh` | a `/llm` line in TTRPG_Client | not armed while you're away |
| `LIB_DEV/tools/wait_for_tell.sh` | a Tell Claude click in Status_Browser | not armed while you're away |
| Scheduled wakeups (`/loop`, ScheduleWakeup) | a timer | none left armed at the end of a turn |
| Background jobs (escape_sim, headless tests) | they finish and notify the session | only while the session is working; none left running at the end |
| A second Claude session, idle | its own waiters | close it with `/exit` before a night run |
| A night run (NIGHT_PROMPT) | itself | the one session allowed; when it's done it writes its report, disarms everything and stops |

Uses CPU, never usage: the OXT-Beyond MCP bridge (node), LM Studio (Spark), OXT-Beyond itself.
Close them if the PC should rest; they never spend usage.

## Before you go to bed (or away)

```
bash ~/projects/LIB_SYSTEM/tools/night_shutdown.sh          # what is running
bash ~/projects/LIB_SYSTEM/tools/night_shutdown.sh --stop   # stop the waiters
```

Then close every Claude session it lists with `/exit`, except the one you leave a night prompt
with.

## What the AI does

- At the start of a session: no waiters until you're at the keyboard. The memory rule says to
  arm `wait_for_llm.sh` / `wait_for_tell.sh` "while a session is open"; that now means while
  you're there.
- When you say you're leaving, or a night prompt starts: stop its own waiters and wakeups, and
  arm none.
- A night run uses no wakeups for polling. It waits on its own jobs directly and finishes with
  nothing armed.
- Long sessions: start a fresh session (`/clear`) rather than `--continue` a very long one. A
  short context costs less every turn.
