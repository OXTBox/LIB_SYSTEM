# ISSUES: tickets for problems, fixes and discoveries

Our own issue tracker as plain files (git has no issues of its own; GitHub's live on GitHub, and our
repos are local). Problems that touch every project (WSL, Windows, memory, antivirus, ports) live here
in LIB_SYSTEM/ISSUES. A problem in one project only goes in that project's own `ISSUES/` folder,
same layout.

## How
- One file a ticket: `NNNN_short_name.md`, numbered in order, never renumbered.
- Each ticket has: **Status**, **What we saw**, **Cause**, **Fix / workaround**, **Discoveries**, **Log** (dated lines).
- Status is one of: `open`, `workaround`, `fixed`, `won't fix`.
- Add a line to INDEX.md for every new ticket; change its status there too.
- Every session: read INDEX.md. Before hunting a bug, look for a ticket that already has it.
