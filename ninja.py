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
from collections import defaultdict


def dice(R=None):
    p = Fraction(1, 6)
    if R is None:
        return {n: p for n in range(1, 7)}

    r = defaultdict(Fraction)
    for prev in R:
        for n in range(1, 7):
            r[n + prev] += R[prev] * p
    return r


def main():
    args = docopt.docopt(__doc__)
    times = int(args['--times'])
    state = None

    with nlj.open(sys.stdout, 'w') as dst:
        dst.write(['N', 'sum', 'prob'])
        for n in range(1, times+1):
            state = dice(state)
            for num, prob in state.items():
                dst.write([
                    n, num, (prob.numerator, prob.denominator)
                    ])


if __name__ == '__main__':
    main()
