# How I run a project with AI helpers while I'm away (a template)

This is the setup Bill uses to keep a big hobby project (games, tools and libraries written in
LiveCode, an xTalk / HyperCard-style language) moving while he's away from the keyboard or busy
with other things. It's written as a template: swap in your own project and folder names.

Bill's setup has three kinds of worker, one inbox, one done pile, one review screen, and a handful
of rule files that every AI reads first. Nothing here needs anything exotic. It needs **one
folder, plain text files, git and some habits.**

---

## 1. The cast

| Who | What it is | What it's good for | Cost |
|---|---|---|---|
| **The owner (you)** | the human | ideas, taste, decisions, play-testing, merging finished work | your time |
| **Claude (Opus)** | Claude Code in a terminal, the everyday model | building, fixing, testing, writing docs, running the others | counts toward a 5-hour usage window and a weekly allowance |
| **Claude (Fable)** | the strongest model, used sparingly | architecture: designing the pieces everything else sits on | a smaller allowance: save it for the hard design jobs |
| **Spark** | a small local model in LM Studio on your own graphics card | bulk words: outlines, lists, level tables, first drafts | free, but it never writes working code and needs checking |

**The rule of thumb:** Spark drafts words in bulk, Opus builds and checks, Fable designs the
foundations, and you decide.

---

## 2. One folder, a few fixed places

Everything lives under one projects folder. Each sub-project is its own folder (Bill calls them
`LIB_SOMETHING`) and **its own git repository**, so nothing can tangle with anything else.

| Place | What goes there |
|---|---|
| `LIB_SYSTEM/` | **the rules every AI reads first** (see section 3) |
| `LIB_LLMIN/<project>/` | **the inbox.** You drop ideas, notes, screenshots, old files here, one sub-folder per project |
| `LIB_LLMOUT/Read/<project>/` | **the done pile.** Once the AI has read an inbox item AND acted on it, it moves it here (never deletes) |
| `LIB_LLMOUT/FOR_REVIEW.txt` | **the review list**: every file the AI made or changed, with notes |
| `Next_Steps_With_Claude/` | the current plan and the brief for the next session, so a new session starts informed |

**Why an inbox:** you never have to explain where things are. "There's something new in the
inbox" is enough. And the done pile means nothing is read twice.

---

## 3. The rule files (the AI's standing orders)

Every session, every AI reads these first. They are short, plain text and in your words.

- **`LIB_ALPHA.md` — the rules.** A map of the project, who does what, naming rules, testing rules,
  "every sub-project is its own git repo", "commit on a branch, the owner merges".
- **`LIB_OMEGA.md` — lessons learned.** A numbered table: *what went wrong* → *the rule that stops
  it happening again*. Example: "Tests passed but the picture was blank → a test of anything
  drawn checks the pixels, not just the size."
- **`STATUS.md`** — running / done / waiting on the owner / next. Rewritten at each milestone.
- **`TODO.md`** — the to-do lanes: the owner's lane (each item with a time guess), Spark's lane,
  the AI lane, and questions *with the default the AI will take if you don't answer*.
- **`OPERATING_PROMPT.md`** — how to run the work: session start, never sit idle, which model for
  which job, budget.

Claude also keeps its own **memory** (small notes it writes for itself: your preferences, where
things are, corrections you've given). That's how "remember to always do X" survives from one
day to the next.

**The single most useful rule:** *never block on a question.* The AI asks, writes down the
default it will use if you don't answer, and keeps working. You can correct it later.

---

## 4. A working day

**Starting a session (you, 1 minute):** open Claude Code in the projects folder and say something
like *"Good morning, let's look at the to-do list and work on what needs doing. Tell me if I have
files to look at."* The AI reads the rules, the status, the plan, your inbox and your review
notes, then tells you what it found and gets going.

**While it works:** it commits each finished piece **on a branch** (never straight into the main
line), and puts every file it makes on your review list with notes: what it did, what it hasn't
tested, which branch it's on.

**When you're away:** it keeps going until the job is done or the usage window runs out. It writes
plans to files *before* big steps, so a cut-off loses nothing.

**Before a break or a bigger model:** ask it to write the next plan or a brief (Bill's:
`Next_Steps_With_Claude/FABLE_BRIEF_...md`). The next session, or the stronger model, reads that
first instead of spending usage rediscovering the project.

---

## 5. Keeping up with what it makes: the review browser

AI produces files faster than anyone can follow, so Bill has a small window (a LiveCode stack,
run as its own little app so it survives closing LiveCode):

- **Left:** every file waiting for review, newest first. `o` waiting, `+` reviewed, `*` has a note.
- **Click a name:** the AI's notes appear (what it did, warnings, caveats, full path) and Explorer
  opens with that file selected.
- **Right-click:** *Reviewed* / *Not Reviewed*. If the AI changes a file after you reviewed it,
  it goes back to waiting by itself.
- **Feedback box + Submit:** your comment, date-stamped, goes into the AI's inbox.
- **Tell Claude button:** one click asks the AI to read your reviews right now. (It writes a line
  to a small file; while a session is open the AI watches that file and wakes up when it changes.
  Between sessions the click waits there, and the next session checks it first.)

Any tool works for this: a spreadsheet, a notes app, a shared doc. What matters is the loop:
**AI lists its work → you mark it → your notes go back to the AI's inbox.**

---

## 6. Getting the local model (Spark) to do its share

Spark is a small model running on your own computer in **LM Studio** (free; it uses the graphics
card). It's good at filling in a shape it is shown: lists, tables, outlines, short descriptions.
It's bad at code and at anything spatial, so Claude always checks its work.

**How Bill runs it, step by step:**
1. **Claude prepares the job:** a prompt file (with a worked example of the answer it wants) and a
   small Python runner that sends Spark one small question at a time and saves each answer to a
   file. Small, closed questions with a word limit work best.
2. **You start it with one double-click:** a `.bat` file such as `START_SPARK_GAME_DESIGNS.bat`.
   It starts LM Studio, loads the model and runs the job in its own window. Close the window to
   stop; double-click again to resume (finished answers are skipped).
3. **It paces itself:** a `pace.txt` beside the runner says how many minutes to work and how many
   seconds to rest, so the computer doesn't run hot for hours. You can edit it while it runs.
4. **You can feed it ideas without Claude:** for example, add a line `Title | what happens` to
   `LIB_LLMIN/LIB_SPARK/GAME_IDEAS.txt`, double-click the bat, and Spark writes a game concept and
   five level tables into its output folder.
5. **Claude reviews and builds:** next session, Claude reads Spark's drafts, keeps what's good,
   fixes what's wrong, and turns them into real work.

**A trick that doubles Spark's quality:** if its first pass is weak, Claude writes ONE answer by
hand and puts it in the prompt as "an example of the level of detail wanted". Spark copies a
shape it is shown very well. (Bill's tutorial outline went from unusable to a good draft that way.)

**Never send pictures to Spark,** and don't ask it for code.

---

## 7. Budget: making the usage last

- Usage comes in **5-hour windows** plus a **weekly allowance**. Let the AI work right up to each
  window's limit; it commits as it goes, so nothing is lost when it stops.
- **Bulk words → Spark** (free). **Everyday building → Opus.** **Hard design → Fable,** with a
  written brief so none of its allowance goes on catching up.
- Ask before big jobs: *"Is there anything the strong model should power through?"* Good answers
  are foundations: a data format everything depends on, a plan for merging lots of branches.

---

## 8. Safety habits

- **Branches, not main.** The AI never merges into the main line; you merge after you've looked.
- **Nothing deleted.** Inbox items move to the done pile. Old versions stay in git.
- **Test what you'll see.** A passing test that never looked at the screen can still be wrong.
- **Hidden programs:** if Windows says a file is "in use", look on Task Manager's *Details* tab;
  a hidden copy of a little app may still be running.
- **Private things stay private.** Personal notes are kept out of git; the AI doesn't send your
  details to outside services.

---

## 9. Starter kit (copy this)

```
projects/
  LIB_SYSTEM/      LIB_ALPHA.md  LIB_OMEGA.md  STATUS.md  TODO.md  OPERATING_PROMPT.md
  LIB_LLMIN/       <project>/ ...          (your inbox)
  LIB_LLMOUT/      Read/<project>/ ...     (the done pile)   FOR_REVIEW.txt
  Next_Steps_With_Claude/                  (plans and briefs between sessions)
  LIB_<your first project>/                (its own git repo)
```

**First message to Claude in a new setup:**
> Read LIB_SYSTEM first. This folder layout is how we work: inbox in LIB_LLMIN, done pile in
> LIB_LLMOUT/Read, every file you make goes on LIB_LLMOUT/FOR_REVIEW.txt, commit on branches,
> never block on a question (write down your default and keep going). Start by helping me write
> LIB_ALPHA.md for my project: <one paragraph about your project>.

**Every session after that:**
> Good morning: read the rules, the status and my inbox, tell me if I have files to look at,
> then work on what needs doing.
