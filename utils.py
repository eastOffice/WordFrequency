import os
import sys
import re

def get_words(text): return re.findall('[a-z0-9]+', text.lower())

def get_stopwords(stop_words_file):
    with open(stop_words_file, 'r', encoding='utf-8') as f:
        stop_words = f.read().strip().split('\n')
    return stop_words

def get_verbs(verbs_file):
    with open(verbs_file, 'r', encoding='utf-8') as f:
        verbs = f.read().strip().split('\n')   
    verb_list = []
    for line in verbs:
        verb_list.append(get_words(line))
    verb_dict = {}
    for verb in verb_list:
        verb_dict[verb[1]] = verb[0]
        verb_dict[verb[2]] = verb[0]
        verb_dict[verb[3]] = verb[0]
    return verb_dict


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

def stem(words, verbs_file):
    verb_dict = get_verbs(verbs_file)
    for word in words:
        if word in verb_dict:
            word = verb_dict[word]
    return words

