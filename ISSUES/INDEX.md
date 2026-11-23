# Issue index (LIB_SYSTEM)

| # | Status | Title | Opened |
|---|---|---|---|
| [0001](0001_wsl_exe_cpu_and_slow_program_starts.md) | workaround | wsl.exe at ~60% CPU, Windows program starts 20-50 s: it was WSL, not our apps | 18 Nov 2026 |
| [0002](0002_vmmem_holds_4GB_idle.md) | open | vmmem keeps ~4 GB of RAM with nothing running | 18 Nov 2026 |
| [0003](0003_two_benches_on_port_8770.md) | fixed | Game Browser froze: two xt3d benches on port 8770 + shell() freezes | 18 Nov 2026 |
| [0004](0004_gad_base_follows_squad.md) | fixed | GAD battles: your Base followed the squad instead of its point (click hit your unit, not the place) | 18 Nov 2026 |
| [0005](0005_t39_two_on_git_or_not_checks_fail.md) | open | t39: On Git or Not "grey chip" and "ignored popup groups" checks fail (87/89), already on main | 18 Nov 2026 |
| [0006](0006_stale_test_counts_after_merge.md) | open | after the merge: t46, t27, t17, t48 expect old counts (t22/t28 fixed: alias file) | 18 Nov 2026 |
| [0007](0007_lc_editor_test_rebuilds_real_biteditor.md) | open | lc_editor_test.txt rebuilds the real BitEditor.livecode in place (and throws at line 89); lc_feedback_1115 throws at Bit.Blank | 18 Nov 2026 |
| [0008](0008_biteditor_erases_glyphs.md) | bugged | BitEditor erases the glyphs completely (after the heights work); parked: procedural levels first | 18 Nov 2026 |
| [0009](0009_harvest_blocks_index_dropped_rows.md) | fixed | harvest_blocks rewrote the Data/Example index with only the last harvest (61 rows dropped) | 18 Nov 2026 |
| [0010](0010_shut_door_walkable_on_heights_branch.md) | fixed | a shut door (E07: ceiling at the floor) can be walked through with LIB_BIT on heights-floor-ceiling: green's meaning changed; doors now From Ceiling (LIB_EDITOR cards-heights) | 18 Nov 2026 |
| [0011](0011_nine_tests_stop_at_camera_reset.md) | open | nine headless tests (t21, t23-t26, t33-t36) stop at Camera.Reset: their stand-in engine lacks the Rename Day names (as t22/t28 did) | 18 Nov 2026 |
| [0012](0012_settings_menu_in_play_hunter.md) | parked | Settings menu does not show during play in Hunter; after Settings, Escape = pointer tool + Developer card (Canyon fine) | 19 Nov 2026 |
| [0013](0013_game_player_has_no_sound.md) | open | the Game Player plays no sound: Audio.Init makes players only in a "Viewport" group (found by LIB_HOWTO topic 16) | 19 Nov 2026 |
| [0014](0014_xtalk_names_pi_shadow.md) | fixed | a parameter named pI does not compile (it is the constant pi); a library that fails to compile only shows "can't find handler" | 19 Nov 2026 |
| [0015](0015_tab_key_games_vs_console.md) | closed | five games use Tab (Amazing_Couple, PromptAndGlazeMaze, VectorToss, PhotonBall, Thrmnlra) but Tab is now the console key; guard in (branch console-player): while a game plays Tab is the game's; keys picked 22 Nov (C swap, \\ Thrmnlra focus, Vector Toss ring always on) on LIB_GAMES branch tab-to-c; Photon Ball ring = per-match difficulty (LIB_COMFY photon-ring) | 22 Nov 2026 |
| [0016](0016_recursive_call_inside_call_args_loses_text.md) | workaround | a recursive function called inside another call's brackets lost the caller's text on OXT-Beyond (LIB_EMITTERS bolts lost their main line two branches deep); call it on its own line | 22 Nov 2026 |
| [0017](0017_held_keys_pile_up_crash_xt.md) | open | two arrow keys held on the Genetic Anomaly star map crash the XT engine (key presses pile up as pending messages) | 22 Nov 2026 |
| [0018](0018_amazing_couple_missing_library_installed.md) | open | Amazing Couple shows a missing Lib warning on the installed copy (tester's PC) | 22 Nov 2026 |
| [0019](0019_tabletop_racers_crash_new_level.md) | open | Tabletop Racers: a crash seen at a new level (not confirmed) | 22 Nov 2026 |
| [0020](0020_bat_duel_quits_on_arrow_keys.md) | fixed on branch arrow-keys-stay (waits for his play) | Bat Duel quits on the arrow keys: Left arrow went to card navigation (no arrowKey handler) | 22 Nov 2026 |
