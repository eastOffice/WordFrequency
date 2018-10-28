import re
import os
import sys
import nltk


def get_words(text): return re.findall('[a-z]+', text.lower())

def mode_c():
    pass

def mode_f(filename, n=0):
    ''' - filename: .txt to read
        - n: return the first n words, 0 returns all
    '''
    pass

