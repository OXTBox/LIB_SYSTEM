# LIB_OMEGA: what we learned the hard way

Each entry: what went wrong, then the commandment it wrote into LIB_ALPHA (or into a
project's notes). Newest at the bottom. Add to it whenever something costs a debugging round.

## LiveCode (xTalk) engine

| # | Transgression | Commandment |
|---|---|---|
| 1 | Clip code loaded with `start using` could not call engine handlers ("can't find handler") | Code that must reach a card and the engine is a **behaviour** of a control on that card, not a library. Libraries stay engine-free. |
| 2 | Text drawn in a new group was invisible: a locked group clips its children to its rect, and an empty group is tiny | Size a holding group to the card while it is still empty (setting its rect later moves its contents). |
| 3 | `the number of keys of sBits` does not exist; the error blamed another line | Count array keys with `the number of lines of the keys of X`. Error line numbers in script-only stacks are off by one (the `script` line). |
| 4 | `"\\"` in LiveCode is two backslashes (no escape sequences) | Write a single backslash as `"\"`; normalise `\\wsl$\...` paths with `replace "\" with "/"`. |
| 5 | `tExt` would not compile: it reads as the keyword `text` | Avoid names that read as keywords: `engine`, `pi`, `size`, `mode`, `text`. Lint catches it. |
| 6 | `"+0.5"` may count as a number, so a relative time read as absolute | Test special prefixes before `is a number`. |
| 7 | The engine HUD font is upper case only, one colour; `>`, `[`, `?` missing | The Sequencer's `Term` layer draws its own vector text in any colour. |
| 8 | The engine's camera position is private to the stack script | A card that projects points keeps its own camera constants and sets the camera itself. |
| 9 | LiveCode hung for good on some stacks (1.5 GB, no answer) and one batch stopped dead | Long batches run with an outside watchdog, or one process per item with a `timeout`, and log START before each item so a crash is known on restart. |

## Tools and shell

| # | Transgression | Commandment |
|---|---|---|
| 10 | `pgrep -f run_spark.sh` matched my own command line and killed my shell | Find processes with `ps ... | awk '/[r]un_spark/'` or by saved PID, never a bare pattern that the command itself contains. |
| 11 | Edits to a runner did nothing: the running process had read its prompt at start | Know when a program reads its config; restart it (resumable) to apply changes. |
| 12 | `check_drafts.py --help` ran the whole check and rewrote REVIEW.md | Every tool answers `--help` without side effects. |
| 13 | Another session switched a repo to another branch mid-work | Check the branch before any git step; commit with a temporary index instead of switching the owner's checkout. |
| 14 | A tracked folder sat on someone's feature branch with uncommitted work | Leave other people's branches alone; ask. |

## Spark and other models

| # | Transgression | Commandment |
|---|---|---|
| 15 | Spark copied the prompt's background examples (`loadLevel`, `Data/`) into its notes as facts | Background in a prompt leaks: mark it as background and check drafts against the source (`check_drafts.py`). |
| 16 | Spark argued with an ambiguous rule inside its answer ("Wait, the instructions say...") | Decide in code what you can (top-level or not, long-function continuation) and tell the model; retry once on self-talk. |
| 17 | Folder notes ran out of tokens in open-ended list sections | Cap every list field (words per line, number of items). |
| 18 | Spark spent hours on 17 iteration copies of one tool | Look for families of versions first; send only the final build of each. |

## Games and the owner

| # | Transgression | Commandment |
|---|---|---|
| 19 | The first recall key was 33 characters: "way too hard" | Start easy; difficulty grows by small steps (one letter more per level). |
| 20 | Real-time timeouts closed the recall window while the owner read; keys "stopped working" | No real-time timeouts on typing tasks by default; the world can run on keystrokes. |
| 21 | A stray key blocked YES/NO for good | Any input clip must recover from unexpected keys; keys nobody wants show STAND BY; keep a key log. |
| 22 | The console at the bottom: "stuck looking DOWN ... it hurts the neck" | Important, changing text goes at the TOP; the action fills the screen. |
| 23 | Target numbers in a list looked like menu keys | Don't number things the player must type by name. |
| 24 | Thrmnlra runs "way too fast" | Pace tests for the player, not the machine. |

## Budget

| # | Transgression | Commandment |
|---|---|---|
| 25 | A long request to Fable hit the 5-hour limit mid-task and the session stopped (2026-11-12, 19:37) | Keep an hour of every 5-hour window for the owner; hand bulk work to Spark; checkpoint plans to files before big steps so a cut-off loses nothing. |

## Testing

| # | Transgression | Commandment |
|---|---|---|
| 26 | The BitEditor passed every test (image sizes, cell counts) while its palette and 1-bit map were blank: LiveCode reads PBM (P1) text only with spaces between the bits and silently makes a blank 128 x 32 image otherwise (2026-11-14) | Test what the owner will SEE, not just sizes: a test of anything drawn checks pixels (e.g. count lit bytes in `the imageData`). |
| 27 | The BitEditor script would not compile ("missing end if") with nothing visibly wrong: a one-line `if x then y` sat on the line just before an `else`, and LiveCode gave the `else` to it (2026-11-14) | The last statement before an `else` is never a one-line `if`: write that one as a block (`if ... then` / `end if`). |
| 28 | Six walking tests failed on the first run, all from distances worked out by hand; and a 20 hu step could not be climbed because the raised glyph on it (6) pushed it over the 25 limit | Take test distances from the game's own numbers (State shows the step size), and test limits that add up (step + relief) together, in the sample map, before fixing the defaults. |

## Git

| # | Transgression | Commandment |
|---|---|---|
| 29 | Twenty-two unmerged branches in eight repositories; LIB_EDITOR's main only works while LIB_BIT has a branch checked out, and its tests read a file out of a LIB_GAMES branch by name (2026-11-14) | Say in the commit or the plan when work in one repository needs a branch of another; a branch is merged or dropped within two sessions (proposed: the owner decides). The merge plan lists such ties. |
| 30 | STATUS said Spark was stopped; the owner had started a design run minutes earlier and it was writing its log in the very folder being merged (it finished seconds before; nothing was lost, by luck) (2026-11-14) | Before changing files in a working folder, look at the newest file times there (`ls -lt`) and for a runner process; if something wrote in the last minutes, wait or leave that folder for last. |
