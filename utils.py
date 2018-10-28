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
    try :
      while(len(pre_list) >= n):
        target_phrase = ""
        for i in range(n):
            if not_word(pre_list[i]):
                for j in range(i):
                    pre_list.pop(0)
                    break
            else:
                if target_phrase != "":
                    target_phrase += " "+pre_list[i]
                else:
                    target_phrase += pre_list[i]
        result.append(target_phrase)
        pre_list.pop(0)
    except:
        import ipdb
        ipdb.set_trace()
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

