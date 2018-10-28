import sys
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from modes import *


def main(args):
    if args.c:
        ''' TODO:
            step-0: character frequency
        '''
        # should call like this: mode_c(args.c)
        pass
    elif args.f:
        mode_f(args.f, args.n)
    elif args.d:
        mode_d(args.d, args.s, args.n)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', type=str)
    parser.add_argument('-n', type=int, default=0)
    parser.add_argument('-p', type=int, default=10)
    parser.add_argument('-f', type=str)
    parser.add_argument('-d', type=str)
    parser.add_argument('-s', action='store_true')
    parser.add_argument('-x', type=str)
    parser.add_argument('-v', type=str)

    args = parser.parse_args()
    main(args)