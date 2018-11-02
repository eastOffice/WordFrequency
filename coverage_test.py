import sys
import os
import time

from modes import *

file_name = 'pride-and-prejudice.txt'
dir_name = './data'

class Args():
    def __init__(self, c=False, f=False, s=False, x=None, v=None, n=0, p=0, q=None, file_name=None):
        self.s = s
        self.c = c
        self.f = f
        self.x = x
        self.v = v
        self.n = n
        self.p = p
        self.q = q
        self.file_name=file_name

def main():
    # test without mode-d
    mode_c(file_name, 10)
    mode_f(file_name, 10, 'stopwords.txt')
    mode_p(file_name, 10, 2, 'verbs.txt')
    mode_q(file_name, 'prepositions.txt', 10, 'verbs.txt')

    #test with mode-d
    args = Args(c=True, n=10, file_name=dir_name)
    mode_d(args)
    args = Args(c=True, n=0, file_name=dir_name)
    mode_d(args)
    args = Args(f=True, s=True, x='stopwords.txt', n=10, file_name=dir_name)
    mode_d(args)
    args = Args(p=2, v='verbs.txt', x='stopwords.txt', n=10, file_name=dir_name)
    mode_d(args)
    args = Args(q='prepositions.txt', v='verbs.txt', n=10, file_name=dir_name)
    mode_d(args)
    # test with wrong usage -q
    args = Args(q='prepositions.txt', n=10, file_name=dir_name)
    mode_d(args)

if __name__ == '__main__':
    main()