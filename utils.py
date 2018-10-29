import os
import sys
import re


rule_verb = '[a-z0-9]+'

def get_words(text): return re.findall(rule_verb, text.lower())

def get_sentences(text):
    return re.findall('[a-z0-9 \n\t\r]+', text)



def get_phrases(sentence , n):

    def not_word(word):
        return word[0] <= '9' and word[0] >= '0'

    def get_preverb(sentence):
        result = re.split('[ \n\t\r]+', sentence)
        for item in result:
            if item == '':
                result.remove('')
        return result
    
    result = []
    pre_list = get_preverb(sentence)
    while(len(pre_list) >= n):
        target_phrase = []
        for i in range(n):
            if not_word(pre_list[i]):
                for j in range(i+1):
                    pre_list.pop(0)
                break
            else:
                target_phrase.append(pre_list[i])
        if len(target_phrase) == n :
            target_str = target_phrase[0]
            for i in range(n-1):
                target_str += " "+target_phrase[i+1] 
            result.append(target_str)
            pre_list.pop(0)
    return result     
        

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
        l = len(verb) - 1
        for i in range(l):
            verb_dict[verb[i+1]] = verb[0]
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

def print_dic(freq, n):
    length = len(freq)
    count = 0
    if not n : n = 99999999
    while(count<length and count<n):
#        while(1):
        min_str = freq[0](0)
        max_freq = freq[0](1)
        i = 0 
        while max_freq != freq[i+1](1) :
            if cmp(min_str) 
        print('%40s\t%d' % (str(key), val))
    else:
        count = 0
        for key, val in freq:
            if count == n: break
            print('%40s\t%d' % (str(key), val))
            count += 1

def get_prepositions(prep_file):
    with open(prep_file, 'r', encoding='utf-8') as f:
        prep_file = f.read().strip().split('\n')
    return prep_file
