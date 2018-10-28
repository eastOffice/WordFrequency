import os
import sys
import re

def get_words(text): return re.findall('[a-z0-9]+', text.lower())

def get_stopwords(stop_words_file):
    with open(stop_words_file, 'r', encoding='utf-8') as f:
        stop_words = f.read().split('\n')
    return stop_words

def list_all_files(rootdir):
    _files = []
    _list = os.listdir(rootdir)
    for i in range(len(_list)):
           path = os.path.join(rootdir, _list[i])
           if os.path.isdir(path):
              _files.extend(list_all_files(path))
           if os.path.isfile(path):
              _files.append(path)
    return _files
