import sys
import os
import time

from modes import *




def main(args):
    if args.file_name is None:
        print("Input a File")
        sys.exit(0)
    if args.c:
<<<<<<< HEAD
        mode_c(args.file_name , args.n)
=======
        mode_c(args.c, args.n)
>>>>>>> e5b02af076a6abd149d84797bb3ab9fca4223f4e
    elif args.f:
        mode_f(args.file_name, args.n, args.x)
    elif args.d:
        mode_d(args.d, args.s, args.n, args.x)
    elif args.p:
        mode_p(args.file_name, args.n, args.p)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
<<<<<<< HEAD
    parser.add_argument('-c', action='store_true')
    parser.add_argument('-n', type=int, default=0)
    parser.add_argument('-p', type=int)
    parser.add_argument('-f', action='store_true')
=======
    parser.add_argument('-c', type=str)
    parser.add_argument('-n', type=int, default=10)
    parser.add_argument('-p', type=int, default=10)
    parser.add_argument('-f', type=str)
>>>>>>> e5b02af076a6abd149d84797bb3ab9fca4223f4e
    parser.add_argument('-d', type=str)
    parser.add_argument('-s', action='store_true')
    parser.add_argument('-x', type=str)
    parser.add_argument('-v', type=str)
<<<<<<< HEAD
    parser.add_argument('file_name', type=str)
=======
    parser.add_argument('-q', type=str)
>>>>>>> e5b02af076a6abd149d84797bb3ab9fca4223f4e

    args = parser.parse_args()
    # unspecified args will be None
    main(args)