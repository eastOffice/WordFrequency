import sys
import os
import time

from modes import *




def main(args):
    if args.file_name is None:
        print("Input a File")
        sys.exit(0)
    
    if args.d:
        mode_d(args)
    else: 
        if args.c:
            mode_c(args.file_name, args.n)
        elif args.f:
            mode_f(args.file_name, args.n, args.x)
        elif args.p:
            mode_p(args.file_name, args.n, args.p)
        elif args.d:
            mode_d(args.file_name, args.s, args.n, args.x)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', action='store_true')
    parser.add_argument('-n', type=int, default=0)
    parser.add_argument('-p', type=int)
    parser.add_argument('-f', action='store_true')
    parser.add_argument('-d', action='store_true')
    parser.add_argument('-s', action='store_true')
    parser.add_argument('-x', type=str)
    parser.add_argument('-v', type=str)
    parser.add_argument('file_name', type=str)

    args = parser.parse_args()
    # unspecified args will be None
    main(args)