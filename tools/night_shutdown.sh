#!/usr/bin/env bash
# night_shutdown.sh - what can wake an AI session (and spend account usage) while the owner is away.
#
#   bash ~/projects/LIB_SYSTEM/tools/night_shutdown.sh          list it (changes nothing)
#   bash ~/projects/LIB_SYSTEM/tools/night_shutdown.sh --stop   stop the waiters; list sessions to close
#
# Account usage is spent only when a Claude session takes a turn. An idle session costs nothing,
# but a waiter that exits (a new /llm line, a Tell Claude click) or a scheduled wakeup starts a
# turn, and a long --continue session re-reads its whole conversation every turn.
# --stop kills only the waiter loops. Claude sessions are listed, never killed: close them with
# /exit (or Ctrl+C twice) so nothing is cut off mid-commit. See LIB_SYSTEM/NIGHT_SHUTDOWN.md.

STOP=false
[ "$1" = "--stop" ] && STOP=true

echo "== Claude sessions (each can wake on its own waiters or wakeups)"
ps -eo pid=,etime=,tty=,args= | grep -E "(^| )claude( |$)" | grep -v grep || echo "   none"

echo "== Waiters that wake a session when they exit"
W=$(ps -eo pid=,etime=,args= | grep -E "wait_for_llm\.sh|wait_for_tell\.sh|tail --pid|inotifywait" | grep -v grep)
if [ -z "$W" ]; then
   echo "   none"
else
   echo "$W"
   if $STOP; then
      for p in $(echo "$W" | awk '{print $1}'); do kill "$p" 2>/dev/null && echo "   stopped $p"; done
   fi
fi

echo "== Long background jobs (CPU only, no usage, but they finish and notify a session)"
ps -eo pid=,etime=,args= | grep -E "escape_sim\.py|oxt_headless\.py|run_headless\.py|livecode-community-server|Standalone -ui" | grep -v grep || echo "   none"

echo "== Use CPU, never usage (stop if the PC should rest)"
ps -eo pid=,etime=,args= | grep -E "mcpbridge|LM Studio|lms |llama" | grep -v grep || echo "   none"

echo "== Scheduled jobs"
crontab -l 2>/dev/null | grep -v '^#' || echo "   no crontab"

if $STOP; then
   echo
   echo "Waiters stopped. Close each Claude session above with /exit when it is idle."
fi
