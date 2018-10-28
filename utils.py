import os
import sys
import re

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
        

def get_stopwords(stop_words_file):
    with open(stop_words_file, 'r', encoding='utf-8') as f:
        stop_words = f.read().split('\n')
    return stop_words