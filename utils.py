import os
import sys
import re
import operator

rule_verb = '[a-z0-9]+'

def get_words(text): return re.findall(rule_verb, text.lower())

def get_sentences(text):
    return re.findall('[a-z0-9 \n\t\r]+', text)



def get_phrases(pre_list, n , verbs_file):

    def not_word(word):
        return word[0] <= '9' and word[0] >= '0'

    # def get_preverb(sentence):
    #     return re.split('[ \n\t\r]+', sentence.strip())
    
    result = []
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


def print_dic(freq, n):
    length = len(freq)
    count = 0
    if not n : n = 99999999
    while(count<length and count<n):
        min_str = freq[0][0]
        max_freq = freq[0][1]
        i = 0 
        target = 0 
        while(max_freq == freq[i+1][1]) :
            if operator.gt(min_str , freq[i+1][0])  :
               min_str = freq[i+1][0]
               target = i+1
            i = i+1
        print('%40s\t%d' % (freq[target][0], freq[target][1]))
        freq.pop(target)
        count += 1

def get_prepositions(prep_file):
    with open(prep_file, 'r', encoding='utf-8') as f:
        prep_file = f.read().strip().split('\n')
    return prep_file
