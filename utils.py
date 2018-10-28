import os
import sys
import re

def get_words(text): return re.findall('[a-z]+[0-9a-z]*', text.lower())

def get_stopwords(stop_words_file):
    with open(stop_words_file, 'r', encoding='utf-8') as f:
        stop_words = f.read().split('\n')
    return stop_words