import sys
import os


from modes import *


def main(args):
    if args.c:
        mode_c(args.c, args.n)
    elif args.f:
        mode_f(args.f, args.n, args.x)
    elif args.d:
        mode_d(args.d, args.s, args.n, args.x)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', type=str)
    parser.add_argument('-n', type=int, default=10)
    parser.add_argument('-p', type=int, default=10)
    parser.add_argument('-f', type=str)
    parser.add_argument('-d', type=str)
    parser.add_argument('-s', action='store_true')
    parser.add_argument('-x', type=str)
    parser.add_argument('-v', type=str)

    args = parser.parse_args()
    # unspecified args will be None
    main(args)