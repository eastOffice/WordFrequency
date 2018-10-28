import os
import sys
import re

<<<<<<< HEAD
def get_words(text): return re.findall('[a-z]+[0-9a-z]*', text.lower())
=======
def get_words(text): return re.findall('[a-z0-9]+', text.lower())
>>>>>>> 76a07fc92f1a6b7db0d955dad46b06a106c04b92

def get_stopwords(stop_words_file):
    with open(stop_words_file, 'r', encoding='utf-8') as f:
        stop_words = f.read().split('\n')
    return stop_words