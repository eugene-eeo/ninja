#!/usr/bin/env python
"""
Usage:
    ninja2.py [--start=<start>] [--times=<times>]
    ninja2.py (-h | --help)

Options:
    --start=<start>   Where to start.    [default: 1]
    --times=<times>   No. of dice rolls. [default: 3]
    (-h | --help)     Show this page.
"""

import docopt
import sys
from fractions import Fraction
import newlinejson as nlj


def dist(N, P, x):
    if N == 1:
        return Fraction(1, 6)
    lower = max(N - 1, x - 6)
    upper = min(x - 1, 6 * (N - 1))
    bound = range(lower, upper + 1)
    return Fraction(1, 6) * sum(P[i] for i in bound)


def simulate(times):
    p = None
    for N in range(1, times+1):
        P = {}
        for x in range(N, 6*N+1):
            P[x] = dist(N, p, x)
            yield N, x, P[x]
        p = P


def main():
    args = docopt.docopt(__doc__)
    start = int(args['--start'])
    times = int(args['--times'])

    with nlj.open(sys.stdout, 'w') as dst:
        dst.write(['N', 'sum', 'prob'])
        for row in simulate(times):
            n, x, p = row
            if n < start:
                continue
            dst.write([n, x, [p.numerator, p.denominator]])


if __name__ == '__main__':
    main()
