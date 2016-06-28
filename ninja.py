#!/usr/bin/env python
"""
Usage:
    ninja.py [--times=<times>]
    ninja.py (-h | --help)

Options:
    --times=<times>   No. of dice rolls. [default: 3]
    (-h | --help)     Show this page.
"""

import docopt
import sys
import newlinejson as nlj
from fractions import Fraction
from collections import defaultdict, namedtuple


NP = namedtuple('NP', 'n,p')


def dice(R=None, N=6):
    p = Fraction(1, N)
    if R is None:
        return {n: NP(1, p) for n in range(1, N+1)}

    r = defaultdict(lambda: NP(0, 0))
    for prev in R:
        for n in range(1, N+1):
            s = n + prev
            r[s] = NP(
                r[s].n + 1,
                r[s].p + R[prev].p * p
            )
    return r


def main():
    args  = docopt.docopt(__doc__)
    times = int(args['--times'])
    state = None

    with nlj.open(sys.stdout, 'w') as dst:
        dst.write(['N', 'sum', 'occ.', 'prob'])
        for n in range(1, times+1):
            state = dice(state)
            for num, info in state.items():
                occ, prob = info
                dst.write([
                    n, num, occ, (prob.numerator, prob.denominator)
                    ])


if __name__ == '__main__':
    main()
