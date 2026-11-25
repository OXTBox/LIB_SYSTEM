# 0022 xtalk_py: the fact "switch is case-sensitive" was wrong

- State: closed 25 Nov 2026 (fixed on xtalk_py branch `stack-runtime`, not merged yet)
- Found by: the Python stack runtime running LightCycles3 (Phase 2). The bike's front sensor never moved because
  `switch "right"` did not take `case "Right"` in our interpreter, so every game crashed at once.
- Measured in LiveCode 9.6.3 (standalone): `switch` compares as text and ignores case unless `the caseSensitive`
  is true; no number compare (`switch "1.0"` does not take `case 1`), no trim.
- The old line in xtalk_py/docs/LIVECODE_FACTS.md said "case-sensitively" (never measured). Fixed there, in the
  interpreter and translator, with two golden cases. Lesson: a fact goes in LIVECODE_FACTS only when LiveCode said it.
