#!/usr/bin/env bash
# remove_ig3d_assets.sh - take the iGame3D 2008 assets out of ~/projects (owner, 16 Nov 2026:
# "remove all the ig3D Assets floating around; everything that goes missing will be generated
# procedurally or reacquired at a later date").
#
#   bash ~/projects/LIB_SYSTEM/tools/remove_ig3d_assets.sh                list (changes nothing)
#   bash ~/projects/LIB_SYSTEM/tools/remove_ig3d_assets.sh --run          remove A and C
#   bash ~/projects/LIB_SYSTEM/tools/remove_ig3d_assets.sh --run --all    also B (not in any git)
#
# A  untracked copies whose content is safe in git: deleted
# B  untracked, in NO git anywhere: deleted only with --all (cannot be undone)
# C  tracked in a LIB's git: git rm + a commit on that LIB's current branch (history keeps them)
# Kept on purpose: programs and code (the LC6 iGame3D, iGame3D_2026_CLAUDE, XTJSON harvests), and
# the three motion clips the games use (reachhigh, throwtoss1, underHandThrow).

P=/home/igame3d/projects
RUN=false; ALL=false
for a in "$@"; do
   [ "$a" = "--run" ] && RUN=true
   [ "$a" = "--all" ] && ALL=true
done
KEEP_CLIPS="reachhigh throwtoss1 underHandThrow"
COAUTHOR="Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"

size() { du -sh "$1" 2>/dev/null | cut -f1; }
gone() {   # delete a folder (A, B)
   if [ -e "$1" ]; then
      echo "   $(size "$1")	$1"
      $RUN && rm -rf "$1" && echo "      removed"
   fi
}
keep_clip() {   # true if the name holds a kept clip
   local n=$1 k
   for k in $KEEP_CLIPS; do
      case "$n" in "iGame3D_$k"|"$k.bvh") return 0;; esac
   done
   return 1
}

echo "== A  untracked, safe in git (LIB_GAMES commit 5a62a5d, branch ig3d-editor-works)"
gone "$P/LIB_GAMES/igame3D_2008_Texts"
gone "$P/LIB_GAMES/TEMPLATES_DO_NOT_COMMIT/igame3D_2008_Texts"

echo "== B  untracked, in NO git (removed only with --run --all; cannot be undone)"
if $ALL; then
   gone "$P/LIB_GAMES/iGame3d_To_Recreate"
elif [ -e "$P/LIB_GAMES/iGame3d_To_Recreate" ]; then
   echo "   $(size "$P/LIB_GAMES/iGame3d_To_Recreate")	$P/LIB_GAMES/iGame3d_To_Recreate   (the 2008 Player builds, iGame3D_Aquarius_Chars, iGame3D_uDeadGame2009-master)"
fi

echo "== C  tracked: git rm + commit (recoverable from history)"
# LIB_MOCAP/library/iGame3D_* (the clips) and LIB_BVH/iGame3D* (their BVH sources)
cd "$P/LIB_MOCAP" || exit 1
M=$(ls -d library/iGame3D_* 2>/dev/null | while read d; do keep_clip "$(basename "$d")" || echo "$d"; done)
if [ -n "$M" ]; then
   echo "   LIB_MOCAP: $(echo "$M" | grep -c .) clip folders ($(du -shc $M 2>/dev/null | tail -1 | cut -f1)); keeping $KEEP_CLIPS"
else
   echo "   LIB_MOCAP: nothing left to remove (kept: $KEEP_CLIPS)"
fi
if $RUN && [ -n "$M" ]; then
   T=$(echo "$M" | xargs git ls-files --)
   if [ -n "$T" ]; then
      echo "$M" | xargs git rm -r -q --
      git commit -q -m "Remove the iGame3D clips no game uses (owner 16 Nov: remove the iGame3D assets; kept: $KEEP_CLIPS)

$COAUTHOR" && echo "      committed $(git log --oneline -1 | cut -c1-8) on $(git branch --show-current)"
   fi
   # what git ignores there: the generated *_stick.txt (made again from a BVH when needed)
   echo "$M" | xargs rm -rf -- && echo "      removed the folders' generated files too"
fi
cd "$P/LIB_BVH" || exit 1
B=$( (ls -d iGame3D_2008 iGame3D_DeadDays 2>/dev/null; ls iGame3D 2>/dev/null | while read f; do keep_clip "$f" || echo "iGame3D/$f"; done) )
echo "   LIB_BVH: $(echo "$B" | grep -c .) files/folders; keeping the BVH of $KEEP_CLIPS"
if $RUN && [ -n "$B" ] && [ -n "$(echo "$B" | xargs -d '\n' git ls-files --)" ]; then
   echo "$B" | xargs -d '\n' git rm -r -q --
   git commit -q -m "Remove the iGame3D BVH sources no game uses (owner 16 Nov: remove the iGame3D assets; kept: $KEEP_CLIPS)

$COAUTHOR" && echo "      committed $(git log --oneline -1 | cut -c1-8) on $(git branch --show-current)"
fi

echo "== Kept (programs and code, not assets)"
for d in "$P/LIB_BIN/igame3d_last_working_Livecode_6_version" "$P/iGame3D_2026_CLAUDE" "$P/XTJSON/batch/igame3d"; do
   [ -e "$d" ] && echo "   $(size "$d")	$d"
done
$RUN || echo; $RUN || echo "Nothing changed. --run removes A and C; --run --all removes B too."
