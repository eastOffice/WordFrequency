import nltk
import re
from collections import Counter
from functools import wraps

from utils import *

def fn_timer(function): 
    @wraps(function)
    def function_timer(*args, **kwargs):
        import time
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print('%s costs %s (s)' %(function, t1 - t0))
        return result
    return function_timer

def mode_c(file_name , n=0):
    rule = re.compile(r"[^a-z]")
    counter = Counter()
    with open(file_name, encoding="utf-8") as f:
        for line in f:
            line_result = rule.sub("" ,line.lower())
            counter.update(line_result)
    sum = 0 
    for charactor  in counter:
        frequency = counter[charactor]
        sum += frequency
    count = 0 
    if n == 0:
        n = 26
    for charactor , frequency in counter.most_common():
        if count == n:
            break
        print('%40s\t%f' % (charactor, frequency/sum))
        count += 1


#@fn_timer
def mode_d(args):
    directory = args.file_name
    if args.s:
        # here returns the final path
        file_list = list_all_files(directory)
    else:
        # here is only the relative path, need path.join
        fl = os.listdir(directory)
        file_list = []
        for i in range(len(fl)):
            t = os.path.join(directory, fl[i])
            if os.path.isfile(t):
                file_list.append(t)

    for file in file_list:
        print('File: %s' % file)
        if args.f:
            mode_f(file, args.n, args.x)
        elif args.p:
            mode_p(file, args.n, args.p, args.v, args.x)
        elif args.q:
            mode_q(file, args.q, args.n, args.v)

#@fn_timer
def mode_f(filename, n=0, stop_words_file=None):
    ''' - filename: .txt to read
        - n: return the first n words, 0 returns all
    '''
    with open(filename, 'r', encoding='utf-8') as f:
        words = get_words(f.read())
    word_freq = nltk.FreqDist(words)
    
    if stop_words_file is not None:
        stop_words = get_stopwords(stop_words_file)
        key_list = list(word_freq.keys())
        for key in key_list:
            if key in stop_words:
                word_freq.pop(key)

    word_freq = sorted(word_freq.items(), key=lambda item:item[1], reverse=True)
    print_dic(word_freq, n)

#@fn_timer
def mode_p(file_pth , n , length, verb_file=None, stop_words_file=None):

    # import time
    # t0 = time.time()
    with open(file_pth, 'r' , encoding='utf-8') as f:
        sentences = get_sentences(f.read().lower())
    
    # t1 = time.time()
    # print('get_sentences costs %s (s)' %(t1 - t0))

    stop_words = get_stopwords(stop_words_file) if stop_words_file is not None else []

    if verb_file is not None:
        verbs = get_verbs(verb_file)
    phrases = []
    for sentence in sentences:
        pre_list = re.split('[ \n\t\r]+', sentence.strip())
        if stop_words_file is not None:
            pre_list = [word for word in pre_list if word not in stop_words]
        if verb_file is not None:
            for i in range(len(pre_list)):
                if pre_list[i] in verbs:
                    pre_list[i] = verbs[pre_list[i]]
        phrases.extend(get_phrases(pre_list, length))
        
    # t2 = time.time()
    # print('get_phrases costs %s (s)' %(t2 - t1))

    phrases_freq = nltk.FreqDist(phrases)
    phrases_freq = sorted(phrases_freq.items(), \
        key=lambda item:item[1], reverse=True)
    print_dic(phrases_freq, n)


#@fn_timer
def mode_q(file_name, prep_file, n, verb_file):
    if verb_file is None:
        print('Please use -q along with -v.')
        return

    # import time
    # t0 = time.time()

    verbs = get_verbs(verb_file)
    preps = get_prepositions(prep_file)

    with open(file_name, 'r' , encoding='utf-8') as f:
        sentences = get_sentences(f.read().lower())

    # t1 = time.time()
    # print('get_sentences costs %s (s)' %(t1 - t0))

    phrases = []
    for sentence in sentences:
        pre_list = re.split('[ \n\t\r]+', sentence.strip())
        for i in range(len(pre_list)-1):
            if pre_list[i] in verbs:
                if pre_list[i+1] in preps:
                    pre_list[i] = verbs[pre_list[i]]
                    phrases.append(pre_list[i]+' '+pre_list[i+1])
                else:
                    continue
            else:
                continue
                
    # t2 = time.time()
    # print('get_phrases costs %s (s)' %(t2 - t1))

    phrases_freq = nltk.FreqDist(phrases)
    phrases_freq = sorted(phrases_freq.items(), \
        key=lambda item:item[1], reverse=True)
    print_dic(phrases_freq, n)
