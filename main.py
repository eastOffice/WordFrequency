import sys
import os

from modes import *

def get_stopwords(stop_words_file):
    with open(stop_words_file, 'r', encoding='utf-8') as f:
        stop_words = f.read().split('\n')
    return stop_words

def main(args):
    if args.c:
        ''' TODO:
            step-0: character frequency
        '''
        # should call like this: mode_c(args.c)
        pass
    elif args.f:
        pass
        

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
    main(args)