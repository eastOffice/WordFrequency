import os
import sys
import re

rule_verb = '[a-z0-9]+'

def get_words(text): return re.findall(rule_verb, text.lower())

def get_sentences(text):
    return re.findall('[a-z0-9 \n\t\r]+', text)



def get_phrases(pre_list, n ):

    def not_word(word):
        return word[0] <= '9' and word[0] >= '0'

    # def get_preverb(sentence):
    #     return re.split('[ \n\t\r]+', sentence.strip())
    
    result = []
    for j in range(len(pre_list)+1-n):
        target_phrase = []
        for i in range(n):
            if not_word(pre_list[i+j]):
                j += i
                break
            else:
                target_phrase.append(pre_list[i+j])
        if len(target_phrase) == n :
            target_str = target_phrase[0]
            for i in range(n-1):
                target_str += " "+target_phrase[i+1] 
            result.append(target_str)
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
        verb_list.append(re.split(r'[ ,]', line))
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
    count = 0
    length = len(freq)
    if n == 0 : n = 99999
    seq_list = [freq[0]]
    for i in range(1,length):
        if freq[i][1] == seq_list[0][1] and i != length-1:
                seq_list.append(freq[i])
        else:
            seq_list.sort(key=lambda item:item[0],reverse=False)
            for key , var in seq_list:
                print('%40s\t%d' % (key, var))
                count += 1
            seq_list = [freq[i]]
        if count >= n:
            break


def get_prepositions(prep_file):
    with open(prep_file, 'r', encoding='utf-8') as f:
        prep_file = f.read().strip().split('\n')
    return prep_file
