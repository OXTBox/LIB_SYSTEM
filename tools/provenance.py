#!/usr/bin/env python3
"""provenance.py - where every file is, what names it, which copies are the same (LIB_ALPHA 4b).

    python3 -I tools/provenance.py PROJECT ROOT [ROOT ...] [--scripts DIR ...] [--dedupe]

  PROJECT   name used for the record and the redundant folder (e.g. LIB_XTJSON)
  ROOT      folders to record (e.g. ~/projects/LIB_LLMIN/LIB_XTJSON ~/projects/LIB_LLMOUT/Read/LIB_XTJSON)
  --scripts folders of harvested scripts to search for each file's name ("named by")
  --dedupe  MOVE the older copies of identical files to ~/projects/LIB_LLMOUT/Read/<PROJECT>/_redundant/
            (same relative path), keeping the newest; never deletes

Writes ~/projects/LIB_LLMOUT/Read/<PROJECT>/provenance.tsv and PROVENANCE.md.
Images (png, jpg, gif, bmp, tif, webp, psd, ico) are listed by name and size only: never read
(the owner's rule, 2026-11-13). Without --dedupe nothing is moved.
"""
import hashlib, os, shutil, sys, time

PROJECTS = os.path.expanduser('~/projects')
IMAGES = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'tif', 'tiff', 'webp', 'psd', 'ico', 'icns', 'pict', 'pct'}


def sha(path):
    h = hashlib.sha1()
    with open(path, 'rb') as f:
        for block in iter(lambda: f.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()[:16]


def main():
    args = sys.argv[1:]
    if len(args) < 2 or args[0] in ('-h', '--help'):
        print(__doc__)
        return
    dedupe = '--dedupe' in args
    args = [a for a in args if a != '--dedupe']
    scripts = []
    if '--scripts' in args:
        i = args.index('--scripts')
        scripts, args = args[i + 1:], args[:i]
    project, roots = args[0], [os.path.expanduser(r) for r in args[1:]]
    out = os.path.join(PROJECTS, 'LIB_LLMOUT', 'Read', project)
    redundant = os.path.join(out, '_redundant')
    rows = []
    for root in roots:
        for d, dirs, files in os.walk(root):
            dirs[:] = [x for x in dirs if x != '_redundant']
            for f in files:
                if 'Zone.Identifier' in f or f in ('provenance.tsv', 'PROVENANCE.md'):
                    continue
                p = os.path.join(d, f)
                ext = f.rsplit('.', 1)[-1].lower() if '.' in f else '(none)'
                st = os.stat(p)
                rows.append({'root': root, 'rel': os.path.relpath(p, root), 'path': p, 'ext': ext, 'size': st.st_size,
                             'mtime': st.st_mtime, 'hash': '' if ext in IMAGES else sha(p), 'image': ext in IMAGES})
    # what names each file: its file name found in harvested scripts (names of 6+ chars only)
    named = {}
    texts = []
    for sd in scripts:
        for d, _, files in os.walk(os.path.expanduser(sd)):
            for f in files:
                if f.endswith('.livecodescript'):
                    texts.append((os.path.relpath(os.path.join(d, f), os.path.expanduser(sd)), open(os.path.join(d, f), encoding='utf-8', errors='replace').read()))
    for r in rows:
        base = os.path.basename(r['rel'])
        if len(base) >= 6 and texts:
            hits = sorted({t.split('/')[0] for t, body in texts if base in body})
            named[r['path']] = hits
    # identical content: the newest copy stays
    groups = {}
    for r in rows:
        if r['hash']:
            groups.setdefault(r['hash'], []).append(r)
    moved = 0
    for h, g in groups.items():
        if len(g) < 2:
            continue
        g.sort(key=lambda r: r['mtime'], reverse=True)
        keep = g[0]
        for r in g[1:]:
            r['dup_of'] = os.path.relpath(keep['path'], PROJECTS)
            if dedupe:
                dest = os.path.join(redundant, r['rel'])
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                shutil.move(r['path'], dest)
                r['moved_to'] = os.path.relpath(dest, PROJECTS)
                moved += 1
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, 'provenance.tsv'), 'w', encoding='utf-8') as f:
        f.write('path\text\tbytes\tmodified\tsha1_16\tnamed_by\tsame_as_newer\tmoved_to\n')
        for r in sorted(rows, key=lambda r: r['path']):
            f.write('\t'.join([os.path.relpath(r['path'], PROJECTS), r['ext'], str(r['size']),
                               time.strftime('%Y-%m-%d %H:%M', time.localtime(r['mtime'])), r['hash'] or '(image: not read)',
                               ', '.join(named.get(r['path'], [])), r.get('dup_of', ''), r.get('moved_to', '')]) + '\n')
    by_ext = {}
    for r in rows:
        e = by_ext.setdefault(r['ext'], [0, 0, 0])
        e[0] += 1
        e[1] += r['size']
        e[2] += 1 if r.get('dup_of') else 0
    with open(os.path.join(out, 'PROVENANCE.md'), 'w', encoding='utf-8') as f:
        f.write('# Provenance: %s\n\n%s. Made by `LIB_SYSTEM/tools/provenance.py` (LIB_ALPHA rule 4b).\n'
                'Roots: %s.\n\n%d files; %d copies identical to a newer one%s. Images listed, never read.\n'
                'Full list: `provenance.tsv` (path, kind, size, date, fingerprint, harvests naming it, newer copy, moved to).\n\n'
                '| kind | files | MB | redundant copies |\n|---|---|---|---|\n'
                % (project, time.strftime('%A, %B %d, %Y'), ', '.join(os.path.relpath(r, PROJECTS) for r in roots), len(rows),
                   sum(1 for r in rows if r.get('dup_of')), ' (moved to `_redundant/`)' if dedupe else ' (not moved: run with --dedupe)'))
        for ext, (n, size, dup) in sorted(by_ext.items(), key=lambda x: -x[1][0]):
            f.write('| %s | %d | %.1f | %d |\n' % (ext, n, size / 1048576, dup))
    print('%d files, %d redundant copies%s -> %s' % (len(rows), sum(1 for r in rows if r.get('dup_of')),
                                                    ', %d moved' % moved if dedupe else ' (dry run)', out))


if __name__ == '__main__':
    main()
