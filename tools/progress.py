#!/usr/bin/env python3
"""progress.py - one page of everything that happened, newest first, from git.

    python3 -I tools/progress.py [DAYS]        (default 3)

Writes LIB_SYSTEM/PROGRESS.html (open it in a browser) and LIB_SYSTEM/PROGRESS.md:
  1. Waiting on the owner, and what is running (from STATUS.md)
  2. Branches waiting for review (not merged into main), per project
  3. Every commit of the last DAYS days in every project under ~/projects, newest first,
     with its project, branch, title and notes
Private folders (LIB_USERS/BILL) are never read.
"""
import html, os, re, subprocess, sys, time

PROJECTS = os.path.expanduser('~/projects')
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEP = '\x1f'


def git(repo, *args):
    r = subprocess.run(['git', '-C', repo] + list(args), capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else ''


def repos():
    out = []
    for name in sorted(os.listdir(PROJECTS)):
        p = os.path.join(PROJECTS, name)
        if os.path.isdir(os.path.join(p, '.git')):
            out.append((name, p))
    return out


def commits(days):
    rows = []
    since = '%d.days' % days
    for name, path in repos():
        log = git(path, 'log', '--all', '--source', '--since=' + since, '--date-order',
                  '--format=%H' + SEP + '%ct' + SEP + '%S' + SEP + '%s' + SEP + '%b' + '\x1e')
        for rec in log.split('\x1e'):
            rec = rec.strip('\n')
            if not rec:
                continue
            parts = rec.split(SEP)
            if len(parts) < 5:
                continue
            h, t, ref, title, body = parts[0], int(parts[1]), parts[2], parts[3], parts[4]
            ref = re.sub(r'^refs/(heads|remotes/[^/]+)/', '', ref)
            body = '\n'.join(l for l in body.strip().split('\n') if not l.startswith('Co-Authored-By'))
            rows.append({'repo': name, 'hash': h[:7], 'time': t, 'branch': ref, 'title': title, 'body': body.strip()})
    rows.sort(key=lambda r: -r['time'])
    return rows


def waiting_branches():
    out = []
    for name, path in repos():
        heads = git(path, 'for-each-ref', '--format=%(refname:short)', 'refs/heads').split()
        base = 'main' if 'main' in heads else ('master' if 'master' in heads else None)
        cur = git(path, 'branch', '--show-current').strip()
        for b in heads:
            if b == base:
                continue
            if base and subprocess.run(['git', '-C', path, 'merge-base', '--is-ancestor', b, base]).returncode == 0:
                continue        # already merged
            n = git(path, 'rev-list', '--count', b if not base else base + '..' + b).strip()
            last = git(path, 'log', '-1', '--format=%ct' + SEP + '%s', b).strip().split(SEP)
            out.append({'repo': name, 'branch': b, 'ahead': n or '?', 'checked_out': b == cur,
                        'time': int(last[0]) if last and last[0] else 0, 'title': last[1] if len(last) > 1 else ''})
    out.sort(key=lambda r: -r['time'])
    return out


def status_sections():
    p = os.path.join(HERE, 'STATUS.md')
    if not os.path.exists(p):
        return {}
    text = open(p, encoding='utf-8').read()
    out = {}
    for m in re.finditer(r'^## (.+?)\n(.*?)(?=^## |\Z)', text, re.S | re.M):
        out[m.group(1).strip()] = m.group(2).strip()
    return out


def when(t):
    return time.strftime('%a %b %d, %H:%M', time.localtime(t))


def md_page(days, rows, branches, st):
    o = ['# Progress, newest first', '',
         'Made %s by `LIB_SYSTEM/tools/progress.py` (run it again to refresh). Last %d days, every project.' % (time.strftime('%A, %B %d, %Y %H:%M'), days), '']
    for key in ('Waiting on the owner (with the default I\'ll take)', 'Running (no Claude usage)', 'Next (AI)'):
        if key in st:
            o += ['## ' + key, '', st[key], '']
    o += ['## Branches waiting for your review', '', '| last commit | project | branch | commits | latest |', '|---|---|---|---|---|']
    for b in branches:
        o.append('| %s | %s | `%s`%s | %s | %s |' % (when(b['time']), b['repo'], b['branch'], ' (checked out)' if b['checked_out'] else '', b['ahead'], b['title'].replace('|', '/')))
    o += ['', '## Every commit, newest first', '']
    day = None
    for r in rows:
        d = time.strftime('%A, %B %d', time.localtime(r['time']))
        if d != day:
            o += ['### ' + d, '']
            day = d
        o.append('- **%s** `%s` / `%s`: **%s**' % (time.strftime('%H:%M', time.localtime(r['time'])), r['repo'], r['branch'], r['title']))
        if r['body']:
            o += ['  ' + l for l in r['body'].split('\n') if l.strip()]
    return '\n'.join(o) + '\n'


def esc(s):
    return html.escape(s)


def md_inline(s):
    s = esc(s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    return s


def md_block(text):
    """small Markdown for STATUS sections: tables, bullets, paragraphs"""
    out, lines, i = [], text.split('\n'), 0
    while i < len(lines):
        l = lines[i]
        if l.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].startswith('|'):
                if not re.match(r'^\|[-| ]+\|$', lines[i]):
                    rows.append([c.strip() for c in lines[i].strip('|').split('|')])
                i += 1
            out.append('<table>' + ''.join('<tr>' + ''.join(('<th>' if n == 0 else '<td>') + md_inline(c) + ('</th>' if n == 0 else '</td>') for c in r) + '</tr>'
                                          for n, r in enumerate(rows)) + '</table>')
            continue
        if re.match(r'^\s*(-|\d+\.) ', l):
            items = []
            while i < len(lines) and (re.match(r'^\s*(-|\d+\.) ', lines[i]) or (lines[i].startswith('  ') and items)):
                if re.match(r'^\s*(-|\d+\.) ', lines[i]):
                    items.append(re.sub(r'^\s*(-|\d+\.) ', '', lines[i]))
                else:
                    items[-1] += ' ' + lines[i].strip()
                i += 1
            out.append('<ul>' + ''.join('<li>' + md_inline(x) + '</li>' for x in items) + '</ul>')
            continue
        if l.strip():
            out.append('<p>' + md_inline(l) + '</p>')
        i += 1
    return '\n'.join(out)


CSS = """
:root{--bg:#07090a;--panel:#0d1213;--ink:#cfe9e4;--dim:#7d9893;--green:#7CFF7C;--cyan:#40E0FF;--amber:#FFB000;--line:#1c2a2b}
@media (prefers-color-scheme: light){:root:not([data-theme="dark"]){--bg:#f6f8f7;--panel:#fff;--ink:#132020;--dim:#5b6b69;--green:#137a2a;--cyan:#006b84;--amber:#8a5a00;--line:#d6e0de}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.55 system-ui,-apple-system,Segoe UI,sans-serif}
main{max-width:1000px;margin:0 auto;padding:24px 16px 80px}
h1,h2,h3{font-family:"Space Mono",ui-monospace,Consolas,monospace;font-weight:700;letter-spacing:.02em}
h1{color:var(--green);font-size:26px;margin:.2em 0}h2{color:var(--cyan);font-size:18px;margin:2em 0 .6em;border-bottom:1px solid var(--line);padding-bottom:.3em}
h3{color:var(--amber);font-size:14px;margin:1.6em 0 .5em;text-transform:uppercase}
.meta{color:var(--dim);font-size:13px}code{font-family:ui-monospace,Consolas,monospace;font-size:.92em;color:var(--cyan)}
table{border-collapse:collapse;width:100%;font-size:14px;margin:.4em 0}th,td{border-bottom:1px solid var(--line);padding:6px 8px;text-align:left;vertical-align:top}th{color:var(--dim);font-weight:600}
.c{background:var(--panel);border:1px solid var(--line);border-left:3px solid var(--green);border-radius:6px;padding:10px 14px;margin:8px 0}
.c .h{display:flex;flex-wrap:wrap;gap:6px 12px;align-items:baseline}.c .t{font-weight:700}.c .w{color:var(--dim);font:13px ui-monospace,Consolas,monospace}
.tag{font:12px ui-monospace,Consolas,monospace;padding:1px 6px;border-radius:4px;border:1px solid var(--line);color:var(--cyan)}.br{color:var(--amber)}
.c pre{white-space:pre-wrap;margin:.5em 0 0;color:var(--ink);font:13px/1.5 ui-monospace,Consolas,monospace;opacity:.9}
ul{padding-left:1.2em}li{margin:.2em 0}
"""


def html_page(days, rows, branches, st):
    o = ['<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">',
         '<title>LIB_ARRAY Progress</title><style>%s</style></head><body><main>' % CSS,
         '<h1>Progress, newest first</h1><div class="meta">Made %s by <code>LIB_SYSTEM/tools/progress.py</code>; run it again to refresh. Last %d days, every project.</div>'
         % (esc(time.strftime('%A, %B %d, %Y %H:%M')), days)]
    for key, label in (('Waiting on the owner (with the default I\'ll take)', 'Waiting on you'), ('Running (no Claude usage)', 'Running'), ('Next (AI)', 'Next')):
        if key in st:
            o.append('<h2>%s</h2>%s' % (label, md_block(st[key])))
    o.append('<h2>Branches waiting for your review</h2><table><tr><th>last commit</th><th>project</th><th>branch</th><th>commits</th><th>latest</th></tr>')
    for b in branches:
        o.append('<tr><td class="meta">%s</td><td>%s</td><td><code>%s</code>%s</td><td>%s</td><td>%s</td></tr>'
                 % (esc(when(b['time'])), esc(b['repo']), esc(b['branch']), ' <span class="meta">(checked out)</span>' if b['checked_out'] else '', esc(str(b['ahead'])), esc(b['title'])))
    o.append('</table><h2>Every commit, newest first</h2>')
    day = None
    for r in rows:
        d = time.strftime('%A, %B %d', time.localtime(r['time']))
        if d != day:
            o.append('<h3>%s</h3>' % esc(d))
            day = d
        o.append('<div class="c"><div class="h"><span class="w">%s</span><span class="tag">%s</span><span class="tag br">%s</span><span class="t">%s</span></div>%s</div>'
                 % (time.strftime('%H:%M', time.localtime(r['time'])), esc(r['repo']), esc(r['branch']), esc(r['title']),
                    '<pre>%s</pre>' % esc(r['body']) if r['body'] else ''))
    o.append('</main></body></html>')
    return '\n'.join(o)


def main():
    if len(sys.argv) > 1 and sys.argv[1] in ('-h', '--help'):
        print(__doc__)
        return
    days = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    rows, branches, st = commits(days), waiting_branches(), status_sections()
    open(os.path.join(HERE, 'PROGRESS.md'), 'w', encoding='utf-8').write(md_page(days, rows, branches, st))
    open(os.path.join(HERE, 'PROGRESS.html'), 'w', encoding='utf-8').write(html_page(days, rows, branches, st))
    print('%d commits in %d projects, %d branches waiting -> %s/PROGRESS.html and PROGRESS.md'
          % (len(rows), len({r['repo'] for r in rows}), len(branches), HERE))


if __name__ == '__main__':
    main()
