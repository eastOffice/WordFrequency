import os
import sys
import re

<<<<<<< HEAD
def get_words(text): return re.findall('[a-z]+[0-9a-z]*', text.lower())

def get_phrases(text , n):
    phrases = []
    if n < 2:
        sys.exit(2)
    reg_rule = '[a-z]+[0-9a-z]*'
    for i in range(n-1):
        reg_rule += '[\t \n\r]+[a-z]+[0-9a-z]*'
    rule = re.compile(reg_rule)
    while(1):
        target = rule.search(text)
        if target is None : 
            break
        target_span = target.span()
        target_str = text[target_span[0]:target_span[1]]
        phrases.append(target_str)
        del_point = re.search('[a-z]+[0-9a-z]*[\r\t\n ]+',target_str).span()[1] +\
            target_span[0]-1
        text = text[del_point:]
    return phrases
        
=======
def get_words(text): return re.findall('[a-z0-9]+', text.lower())
>>>>>>> e5b02af076a6abd149d84797bb3ab9fca4223f4e

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

