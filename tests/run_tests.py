#!/usr/bin/env python3
"""LIB_SYSTEM's check that runs without LiveCode (A-50): the progress page's small Markdown (bold,
code, HTML escaped) and provenance's file hash. Writes nothing.

    python3 -I tests/run_tests.py
"""
import os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import tempfile
import progress, provenance                 # noqa: E402

CHECKS, FAILS = [0], []


def check(name, ok, got=None):
    CHECKS[0] += 1
    if not ok:
        FAILS.append(name)
        print("FAIL  %s%s" % (name, "" if got is None else "  (got %r)" % (got,)))
    else:
        print("ok    %s" % name)


def done():
    print("\n%d of %d passed" % (CHECKS[0] - len(FAILS), CHECKS[0]))
    return 1 if FAILS else 0


def main():
    check('bold and code', progress.md_inline('**A-50** `run_tests.py`') == '<b>A-50</b> <code>run_tests.py</code>',
          progress.md_inline('**A-50** `run_tests.py`'))
    check('HTML is escaped', progress.md_inline('<b> & </b>') == '&lt;b&gt; &amp; &lt;/b&gt;')
    with tempfile.TemporaryDirectory() as d:
        a, b, c = (os.path.join(d, n) for n in 'abc')
        open(a, 'w').write('same'); open(b, 'w').write('same'); open(c, 'w').write('other')
        check('same content, same hash; different content, different hash',
              provenance.sha(a) == provenance.sha(b) != provenance.sha(c))
        check('the hash is 16 hex characters', len(provenance.sha(a)) == 16)
    return done()


if __name__ == '__main__':
    sys.exit(main())
