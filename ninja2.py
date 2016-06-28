#!/usr/bin/env python
"""
Usage:
    ninja2.py [--start=<start>] [--times=<times>]
    ninja2.py (-h | --help)

Options:
    --start=<start>   Where to start.    [default: 2]
    --times=<times>   No. of dice rolls. [default: 3]
    (-h | --help)     Show this page.
"""

import docopt
import sys
from fractions import Fraction
import newlinejson as nlj


def dist(N, p):
    def P(x, T={}):
        if x not in T:
            lower = max(N - 1, x - 6)
            upper = min(x - 1, 6 * (N - 1))
            bound = range(lower, upper + 1)
            T[x] = Fraction(1, 6) * sum(p(i) for i in bound)
        return T[x]
    return P


def P_1(x):
    return Fraction(1, 6)


def simulate(start, times):
    prev = P_1
    for n in range(2, times+1):
        P = dist(n, prev)
        if n >= start:
            for x in range(n, 6*n+1):
                yield n, x, P(x)
        prev = P


def main():
    args = docopt.docopt(__doc__)
    start = int(args['--start'])
    times = int(args['--times'])

    with nlj.open(sys.stdout, 'w') as dst:
        dst.write(['N', 'sum', 'prob'])
        for row in simulate(start, times):
            n, x, p = row
            dst.write([n, x, [p.numerator, p.denominator]])


if __name__ == '__main__':
    main()
