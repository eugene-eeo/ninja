#!/usr/bin/env python
"""
Usage:
    htmlify.py [--title=<title>]
    htmlify.py (-h | --help)

Options:
    --title=<title>   Title of HTML file.
    (-h | --help)     Show this page.
"""

import docopt

import sys
from collections import defaultdict
from fractions import Fraction
import newlinejson as nlj
import tablib


TEMPLATE = '''
<!doctype html>
<html>
<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.6.0/katex.min.css">
<style>
body   {{ font-size: 20px; width: 80%; margin: auto; }}
flex   {{ display: -webkit-flex; display: flex; flex-direction: row; flex-wrap: wrap; }}
table  {{ border: 1px solid #000; border-collapse: collapse; border-spacing: 0; }}
td, th {{ border: 1px solid #000; padding: 0.2em; text-align: center; }}
.stack {{ float: left; margin: 0 1em; }}
</style>
</head>
<body>
<center>
<h1>{title}</h1>
<div class='flex'>
{content}
</div>
</center>
</body>
</html>
'''

TABLE = '''
<div class='stack'>
<h2>{N} roll(s)</h2>
{table}
</div>
'''


format_frac = lambda f: r'\frac{%d}{%d}' % (f.numerator, f.denominator)


def main():
    args = docopt.docopt(__doc__)
    title = args['--title']
    title = '(%s)' % title if title else ''

    with nlj.open(sys.stdin) as src:
        headers = next(src)[1:]
        data = defaultdict(lambda: tablib.Dataset(headers=headers))
        for row in src:
            N, num, P = row
            data[N].append(
                [num, format_frac(Fraction(*P))],
            )

    content = ''.join([
        TABLE.format(N=N, table=D.html) for N, D in data.items()
    ])
    print(TEMPLATE.format(
        title='dice rolls ' + title,
        content=content,
        ))


if __name__ == '__main__':
    main()
